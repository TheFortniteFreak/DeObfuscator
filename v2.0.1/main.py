# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import PySide6.QtWidgets as qw
import PySide6.QtCore as qc
import PySide6.QtGui as qg
from PySide6.QtWebEngineWidgets import QWebEngineView

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

import os
import json
import shutil
import threading
import time
import sys
from pathlib import Path
import importlib.util
import subprocess
import socket
import stat
import tkinter as tk


suppath = os.path.join(os.environ["LOCALAPPDATA"], "BRO_Obfuscated")
os.makedirs(suppath, exist_ok=True)

update_window = None

def show_update_window():
    global update_window

    update_window = tk.Tk()
    update_window.title("Updater")
    update_window.geometry("300x100")
    update_window.resizable(False, False)
    update_window.attributes("-topmost", True)

    label = tk.Label(
        update_window,
        text="Updating module...",
        font=("Arial", 14)
    )
    label.pack(expand=True)

    update_window.protocol(
        "WM_DELETE_WINDOW",
        lambda: None
    )

    update_window.mainloop()


def close_update_window():
    global update_window

    if update_window:
        try:
            update_window.after(
                0,
                update_window.destroy
            )
        except:
            pass


threading.Thread(
    target=show_update_window,
    daemon=True
).start()

time.sleep(0.5)


def has_internet():
    try:
        socket.create_connection(
            ("8.8.8.8", 53),
            timeout=3
        )
        return True
    except OSError:
        return False


def remove_readonly(func, path, exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


try:

    if has_internet():

        for item in os.listdir(suppath):
            item_path = os.path.join(
                suppath,
                item
            )

            try:
                if os.path.isdir(item_path):
                    shutil.rmtree(
                        item_path,
                        onerror=remove_readonly
                    )
                else:
                    os.chmod(
                        item_path,
                        stat.S_IWRITE
                    )
                    os.remove(item_path)

            except Exception as e:
                print(
                    f"Failed to delete {item_path}: {e}"
                )


    destination = os.path.join(
        suppath,
        "editor"
    )

    repo = (
        "https://github.com/"
        "TheFortniteFreak/"
        "upddeobf.git"
    )

    temp = os.path.join(
        suppath,
        "upddeobf"
    )

    subprocess.run(
        [
            "winget",
            "install",
            "--id",
            "Git.Git",
            "--accept-source-agreements",
            "--accept-package-agreements",
        ],
        check=False,
    )

    result = subprocess.run(
        ["git", "--version"],
        capture_output=True,
        text=True
    )

    if not os.path.exists(temp) and result.returncode == 0:
        subprocess.run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                repo,
                temp
            ],
            check=True
        )


    source_editor = os.path.join(
        temp,
        "editor"
    )


    shutil.copytree(
        source_editor,
        destination,
        dirs_exist_ok=True
    )


finally:
    close_update_window()



url = Path(
    destination,
    "index.html"
).as_uri()

main_path = os.path.join(
    destination,
    "Main",
    "Main.py"
)


main_dir = os.path.dirname(main_path)
sys.path.insert(
    0,
    main_dir
)


spec = importlib.util.spec_from_file_location(
    "Main",
    main_path
)

module = importlib.util.module_from_spec(
    spec
)

spec.loader.exec_module(module)


Main = module.Main


def obf(script):
    args = []

    if prettyprint.isChecked():
        args.append("--pretty")

    if vfix.isChecked():
        args.append("--fixv")

    if parse:
        args.append("--parse")

    script = Main(
        script,
        *args
    )

    js = f"""
    if (typeof monaco !== 'undefined' && monaco.editor) {{
        monaco.editor.getModels()[0].setValue({json.dumps(script)});
    }} else if (typeof editor !== 'undefined' && editor.setValue) {{
        editor.setValue({json.dumps(script)});
    }}
    """

    outp.page().runJavaScript(js)


def obf_button(*args):
    inp.page().runJavaScript(
        "getText()",
        obf
    )


def settings(*args):
    if toplevel.isVisible():
        toplevel.hide()
    else:
        toplevel.show()
app = qw.QApplication([])
app.setStyle("Fusion")
main = qw.QMainWindow()
main.setWindowTitle("DeObfuscate")
main.resize(1043, 617)
main.setStyleSheet(f"""
		QMainWindow {{
			background-color: rgb(8,0,10);
		}}
""")
screen = qg.QGuiApplication.primaryScreen().availableGeometry()
screen_w = screen.width()
screen_h = screen.height()
win_w = main.width()
win_h = main.height()

geometryX = (screen_w // 2) - (win_w // 2)
geometryY = (screen_h // 2) - (win_h // 2)
geometryX += 0
geometryY += 0
main.move(geometryX, geometryY)

main.menuBar().setVisible(False)

layoutcontainer = qw.QVBoxLayout()
layoutcontainer.setDirection(qw.QBoxLayout.TopToBottom)
layoutcontainer.setContentsMargins(6, 6, 6, 6)
layoutcontainer.setSpacing(8)
main_central_widget = qw.QWidget()
main.setCentralWidget(main_central_widget)
main_central_widget.setLayout(layoutcontainer)
main_central_widget.setStyleSheet(f"""
		QMainWindow {{
			background-color: rgb(8,0,10);
		}}
""")

frame = qw.QFrame()
frame = qw.QFrame()
frame.setStyleSheet(f"""
		QFrame {{
			background-color: rgb(8,0,10);
			border-radius: 2px;
		}}	""")
frame.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Expanding)
layoutcontainer.addWidget(frame, 0)

layoutcontainer1 = qw.QHBoxLayout()
layoutcontainer1.setDirection(qw.QBoxLayout.LeftToRight)
layoutcontainer1.setContentsMargins(6, 6, 6, 6)
layoutcontainer1.setSpacing(8)
frame.setLayout(layoutcontainer1)

frame1 = qw.QFrame()
frame1 = qw.QFrame()
frame1.setStyleSheet(f"""
		QFrame {{
			background-color: rgba(237,236,236,0);
			border-radius: 2px;
		}}	""")
frame1.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Preferred)
frame1.setMinimumSize(80, 30)
layoutcontainer1.addWidget(frame1, 0)

layoutcontainer2 = qw.QHBoxLayout()
layoutcontainer2.setDirection(qw.QBoxLayout.LeftToRight)
layoutcontainer2.setContentsMargins(6, 6, 6, 6)
layoutcontainer2.setSpacing(8)
frame1.setLayout(layoutcontainer2)

inp = QWebEngineView()
inp.setUrl(qc.QUrl(""+url+""))
inp.setStyleSheet("""
		QWebEngineView{

		}	""")
inp.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Preferred)
inp.setMinimumSize(80, 30)
layoutcontainer2.addWidget(inp, 0)

frame2 = qw.QFrame()
frame2 = qw.QFrame()
frame2.setStyleSheet(f"""
		QFrame {{
			background-color: rgba(237,236,236,0);
			border-radius: 2px;
		}}	""")
frame2.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Preferred)
frame2.setMinimumSize(80, 30)
layoutcontainer1.addWidget(frame2, 0)

layoutcontainer3 = qw.QHBoxLayout()
layoutcontainer3.setDirection(qw.QBoxLayout.LeftToRight)
layoutcontainer3.setContentsMargins(6, 6, 6, 6)
layoutcontainer3.setSpacing(8)
frame2.setLayout(layoutcontainer3)

outp = QWebEngineView()
outp.setUrl(qc.QUrl(""+url+""))
outp.setStyleSheet("""
		QWebEngineView{

		}	""")
outp.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Preferred)
outp.setMinimumSize(80, 30)
layoutcontainer3.addWidget(outp, 0)

frame3 = qw.QFrame()
frame3 = qw.QFrame()
frame3.setStyleSheet(f"""
		QFrame {{
			background-color: rgba(237,236,236,0);
			border-radius: 2px;
		}}	""")
frame3.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Preferred)
frame3.setMinimumSize(80, 30)
layoutcontainer.addWidget(frame3, 0)

layoutcontainer4 = qw.QHBoxLayout()
layoutcontainer4.setDirection(qw.QBoxLayout.LeftToRight)
layoutcontainer4.setContentsMargins(6, 6, 6, 6)
layoutcontainer4.setSpacing(8)
frame3.setLayout(layoutcontainer4)
layoutcontainer4.setAlignment(qc.Qt.AlignHCenter | qc.Qt.AlignTop)

sett = qw.QPushButton("Settings", )
sett.setStyleSheet(f"""
		QPushButton {{
			background-color: rgba(228,226,226,0);
			color: rgb(255,255,255);
			border: 1px solid rgb(255,255,255);
			border-radius: 2px;
			font-size: 15px;
			font-weight: bold;
		}}

		QPushButton:hover {{
			color: #000;
			background: #cfcaca;
			background-color: #cfcaca;
		}}
""")
sett.clicked.connect(lambda _: settings(sett))

sett.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Preferred)
sett.setMinimumSize(80, 30)
layoutcontainer4.addWidget(sett, 0)

obfuscates = qw.QPushButton("DeObfuscate", )
obfuscates.setStyleSheet(f"""
		QPushButton {{
			background-color: rgba(228,226,226,0);
			color: rgb(255,255,255);
			border: 1px solid rgb(255,255,255);
			border-radius: 2px;
			font-size: 15px;
			font-weight: bold;
		}}

		QPushButton:hover {{
			color: #000;
			background: #cfcaca;
			background-color: #cfcaca;
		}}
""")
obfuscates.clicked.connect(lambda _: obf_button(obfuscates))

obfuscates.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Preferred)
obfuscates.setMinimumSize(80, 30)
layoutcontainer4.addWidget(obfuscates, 0)


toplevel = qw.QDialog(main)
toplevel.setWindowTitle("Settings")
toplevel.resize(329, 172)
toplevel.setAttribute(qc.Qt.WA_StyledBackground, True)
toplevel.setStyleSheet(f"""
		QDialog {{
			background-color: rgb(8,0,10);
		}}
""")
screen = qg.QGuiApplication.primaryScreen().availableGeometry()
screen_w = screen.width()
screen_h = screen.height()
win_w = toplevel.width()
win_h = toplevel.height()

geometryX = (screen_w // 2) - (win_w // 2)
geometryY = (screen_h // 2) - (win_h // 2)
geometryX += 0
geometryY += -60
toplevel.move(geometryX, geometryY)


layoutcontainer5 = qw.QVBoxLayout()
layoutcontainer5.setDirection(qw.QBoxLayout.TopToBottom)
layoutcontainer5.setContentsMargins(6, 6, 6, 6)
layoutcontainer5.setSpacing(8)
toplevel.setLayout(layoutcontainer5)

prettyprint = qw.QCheckBox("Pretty Print", )
prettyprint.setStyleSheet("""
		QCheckBox{
			background-color: rgba(255, 255, 255, 0);
			color: rgb(255,255,255);
			border-radius: 2px;
			font-size: 18px;
			font-weight: bold;
		}

		QCheckBox::indicator{
			width: 12px;
			height: 12px;
			border: 2px solid #D9D9D9;
			border-radius: 1px;
			background: #08000a;
		}

		QCheckBox::indicator:checked{
			background: #0b74de;
			border-color: #D9D9D9;
		}

		QCheckBox::indicator:hover{
			background: #0a3a74;
		}	""")
prettyprint.setChecked(True)
prettyprint.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Preferred)
prettyprint.setMinimumSize(80, 30)
layoutcontainer5.addWidget(prettyprint, 0)

parse = qw.QCheckBox("Parse", )
parse.setStyleSheet("""
		QCheckBox{
			background-color: rgba(255, 255, 255, 0);
			color: rgb(255,255,255);
			border-radius: 2px;
			font-size: 18px;
			font-weight: bold;
		}

		QCheckBox::indicator{
			width: 12px;
			height: 12px;
			border: 2px solid #D9D9D9;
			border-radius: 1px;
			background: #08000a;
		}

		QCheckBox::indicator:checked{
			background: #0b74de;
			border-color: #D9D9D9;
		}

		QCheckBox::indicator:hover{
			background: #0a3a74;
		}	""")
parse.setChecked(True)
parse.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Preferred)
parse.setMinimumSize(80, 30)
layoutcontainer5.addWidget(parse, 0)

vfix = qw.QCheckBox("Variable fix", )
vfix.setStyleSheet("""
		QCheckBox{
			background-color: rgba(255, 255, 255, 0);
			color: rgb(255,255,255);
			border-radius: 2px;
			font-size: 18px;
			font-weight: bold;
		}

		QCheckBox::indicator{
			width: 12px;
			height: 12px;
			border: 2px solid #D9D9D9;
			border-radius: 1px;
			background: #08000a;
		}

		QCheckBox::indicator:checked{
			background: #0b74de;
			border-color: #D9D9D9;
		}

		QCheckBox::indicator:hover{
			background: #0a3a74;
		}	""")
vfix.setChecked(True)
vfix.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Preferred)
vfix.setMinimumSize(80, 30)
layoutcontainer5.addWidget(vfix, 0)


toplevel.hide()


main.show()
app.exec()
