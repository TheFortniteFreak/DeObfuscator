# DeObfuscate

A Lua deobfuscation tool built with **Python**, **PySide6**, and **Monaco Editor**.

DeObfuscate provides a desktop interface for analyzing and cleaning obfuscated Lua code. The application uses Python modules for the deobfuscation engine and Monaco Editor as the code editing interface.

The editor interface and required processing modules are provided through:

**Modules / Editor Repository:**  
https://github.com/TheFortniteFreak/upddeobf

---

# Features

- Lua Deobfuscation
  - Processes obfuscated Lua scripts using Python-based deobfuscation modules.
  - Converts difficult-to-read Lua code into cleaner and more understandable code.

- Monaco Editor Interface
  - Uses Monaco Editor for an advanced code editing experience.
  - Provides syntax highlighting and editor functionality.
  - Embedded inside the PySide6 application using Qt WebEngine.

- Processing Options
  - Pretty Print
    - Formats output code for improved readability.
  - Parse
    - Enables parser-based processing.
  - Variable Fix
    - Attempts to improve variable handling and clean generated structures.

- Desktop Application
  - Built with PySide6.
  - Runs as a native Windows application.
  - Uses Python modules as the processing backend.

- Automatic Module Updates
  - Downloads the latest editor and processing modules automatically.
  - Keeps required components synchronized with the modules repository.

---

# Installation

## Latest Release

The latest version of DeObfuscate can be downloaded from the GitHub Releases page:

https://github.com/TheFortniteFreak/DeObfuscator/releases/latest

Download the latest `.exe` release and run it.

The release version includes everything required to run DeObfuscate:

- DeObfuscate application
- PySide6 runtime
- Monaco Editor interface
- Python deobfuscation modules
- Required dependencies

No Python installation or additional setup is required when using the release version.

---

# Developer Installation

This section is only required if you want to run or modify the source code.

## Requirements

- Windows 10/11
- Python 3.10+
- Git installed and available in PATH

## Install Dependencies

```bash
pip install PySide6 PySide6-WebEngine
