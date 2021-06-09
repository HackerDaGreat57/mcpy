#
# An example of a Win32 window and an OpenGL context for rendering graphics
#
# Visit https://devs.site for more
#

# import the Win32 api
import winxpgui as win32gui
# import Win32 constants
import win32con

# import OpenGL's good stuff
from OpenGL.GL import *
from OpenGL.WGL import *

# import standard modules
import struct

# constants
PFD_TYPE_RGBA = 0
PFD_MAIN_PLANE = 0
PFD_DRAW_TO_WINDOW = 0x00000004
PFD_SUPPORT_OPENGL = 0x00000020

# This class represents a normal window
class NormalWindow:
    # Window constructor
    def __init__(self):
        # window class name
        className = "OpenglWindow"

        # system messages mapping
        message_map = {
            win32con.WM_DESTROY: self.OnDestroy
        }

        # set window class properties
        # https://docs.microsoft.com/en-us/windows/desktop/api/winuser/ns-winuser-tagwndclassa
        wc = win32gui.WNDCLASS()
        wc.hInstance = win32gui.dllhandle
        wc.lpszClassName = className
        wc.style = win32con.CS_OWNDC
        wc.hCursor = win32gui.LoadCursor( 0, win32con.IDC_ARROW )
        wc.hbrBackground = win32con.COLOR_WINDOW + 1
        wc.lpfnWndProc = message_map
        wc.cbWndExtra = win32con.DLGWINDOWEXTRA + struct.calcsize("Pi")

        # try to register the class
        try:
            classAtom = win32gui.RegisterClass(wc)
        except win32gui.error as err_info:
            if err_info.winerror!=winerror.ERROR_CLASS_ALREADY_EXISTS:
                raise

        # create the window
        # https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-createwindowa
        self.hwnd = win32gui.CreateWindow(
            className,
            "OpenGL Window",
            win32con.WS_OVERLAPPEDWINDOW,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            800,
            600,
            0,
            0,
            win32gui.dllhandle,
            None
        )

        # update
        win32gui.UpdateWindow(self.hwnd)

        # and show
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOW)

    # create OpenGL context
    def InitOpengl(self):
        # get window's device context
        hdc = win32gui.GetDC(self.hwnd)

        # context properties
        # https://docs.microsoft.com/en-us/windows/desktop/api/wingdi/ns-wingdi-tagpixelformatdescriptor
        pfd = PIXELFORMATDESCRIPTOR();
        pfd.dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL
        pfd.iPixelType = PFD_TYPE_RGBA
        pfd.iLayerType = PFD_MAIN_PLANE
        pfd.cColorBits = 32
        pfd.cDepthBits = 24

        # create pixel format for context
        pixelformat = ChoosePixelFormat(hdc, pfd)
        SetPixelFormat(hdc, pixelformat, pfd)

        # create context
        hglrc = wglCreateContext(hdc)
        wglMakeCurrent(hdc, hglrc)

        # set backgrounnd color
        glClearColor(1.0, 0.5, 0.5, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # return
        glFinish()

    # window being destroyed
    def OnDestroy(self, hwnd, msg, wparam, lparam):
        # get and delete opengl context
        hrc = wglGetCurrentContext()
        wglMakeCurrent(0, 0)
        if hrc: wglDeleteContext(hrc)

        win32gui.PostQuitMessage(0)
        return True

# Entry point
if __name__=='__main__':
    # create window
    w = NormalWindow()
    # init opengl
    w.InitOpengl()

    # messages loop to keep window open
    win32gui.PumpMessages()
