# qt_image_manipulation

I followed these steps to build this project.
1. Installed PyQt6
2. Designed UI using Qt Designer. The design file is available in this repo as first.ui
3. Converted the .ui file to python code using `pyuic6 first.ui -o demo.py`
4. Updated demo.py as required.
5. In order to run this on ypur machine,
    Create a python virtual environment
    Install dependencies through requirements.txt
    Navigate to this directory and run `python3 demo.py`
    By default the UI will launch with `lena.png` that is available in project directory.
    In case you want to pass path of custom image as cmd-argument like, then run `python3 demo.py custom_image.png`
6. On UI, you will see buttons for opening and saving image, two vertical sliders for size and contrast control and a check button the switch between optimized opencv resize and custom python resize implementation.
7. Interact with UI through sliders and observe output.





References:

[1] Basics of Qt Designer and PyQt:  https://pyshine.com/Make-GUI-for-OpenCv-And-PyQt5/

[2] Contrast enhancement: https://www.dfstudios.co.uk/articles/programming/image-programming-algorithms/image-processing-algorithms-part-5-contrast-adjustment/

[3] Image resize from scratch:  https://meghal-darji.medium.com/implementing-bilinear-interpolation-for-image-resizing-357cbb2c2722
