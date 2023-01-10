import PySimpleGUI as sg
import cv2
from ImageEditing import ChangeBrightness,ChangeSaturation,ImageSharpen,ImageFlip
from ImageFilters import OilPainting, Water , BlackAndWhite,GrayScale
'''
Requirements
    - PySimpleGUI
    - OpenCV (specifically pip install opencv-contrib-python, if error persists uninstall both opencv-contrib-python  and opencv-python(if installed) and "pip install --no-cache-dir opencv-contrib-python")

'''


def main():

    # sg.theme("Reddit")
    sg.theme("DarkBrown2")
    column = [
        sg.Column([
            [
            sg.Radio("Oil Painting", "Radio", size=(10, 1), key="-OIL-",font=("Cascadia Code SemiBold", 12)),
            sg.Slider(
                (1, 50),
                # add 50 ticks to the slider
                tick_interval=0.1,                
                orientation="h",
                size=(20, 15),
                key="-OIL SLIDER SIZE-",
            ),
            sg.Slider(
                (1, 100),
                tick_interval=0.1,
                orientation="h",
                size=(20, 15),
                key="-OIL SLIDER LEVEL-",
            )
            ],
            [
                sg.Radio("Water Color", "Radio", size=(10, 1), key="-WATER-",font=("Cascadia Code SemiBold", 12)),
                sg.Slider(
                    (1, 400),
                    orientation="h",
                    size=(20, 15),
                    key="-WATER SLIDER SIZE-",
                ),
                sg.Slider(
                    (1, 100),
                    orientation="h",
                    size=(20, 15),
                    key="-WATER SLIDER LEVEL-",
                )
            ],
            [
                sg.Radio("Brightness", "Radio", size=(10, 1), key="-BRIGHTNESS-",font=("Cascadia Code SemiBold", 12)),
                sg.Slider(
                    (0, 100),
                    orientation="h",
                    size=(40, 15),
                    key="-BRIGHTNESS SLIDER-",
                ),
            ],
            [
                sg.Radio("Saturation", "Radio", size=(10, 1), key="-SATURATION-",font=("Cascadia Code SemiBold", 12)),
                sg.Slider(
                    (0, 100),
                    orientation="h",
                    size=(20, 15),
                    key="-SATURATION SLIDER-",
                )
            ],
            [
                sg.Radio("Blur", "Radio", size=(10, 1), key="-BLUR-",font=("Cascadia Code SemiBold", 12)),
                sg.Slider(
                    (1, 100),
                    orientation="h",
                    size=(40, 15),
                    key="-BLUR SLIDER-",
                ),
            ],
            [
                sg.Radio("Hue", "Radio", size=(10, 1), key="-HUE-",font=("Cascadia Code SemiBold", 12)),
                sg.Slider(
                    (0, 225),
                    orientation="h",
                    size=(40, 15),
                    key="-HUE SLIDER-",
                ),
            ],
            [
                sg.Radio("enhance", "Radio", size=(10, 1), key="-ENHANCE-",font=("Cascadia Code SemiBold", 12)),
                sg.Slider(
                    (1, 255),
                    orientation="h",
                    size=(40, 15),
                    key="-ENHANCE SLIDER-",
                ),
            ],
            [
                sg.Radio("GrayScale", "Radio", size=(10, 1), key="-GRAYSCALE-", font=("Cascadia Code SemiBold", 12)),
            ],

            [sg.Button("Exit", size=(10, 1), font=("Cascadia Code SemiBold", 12))],
    ],scrollable=True,vertical_scroll_only=True)
]

    # Define the window layout
    layout = [
        [
        sg.Column(
            [
                [sg.Text("Image Editing", font=("Cascadia Code SemiBold", 25))],
                [sg.Image(filename="", key="-IMAGE-", size=(800, 800))]],element_justification='center')
            ]
            ,
            column
        ]

    # Create the window and show it without the plot
    window = sg.Window("OpenCV Integration", layout, location=(400, 0),grab_anywhere=True,resizable=True,size=(600, 1000) )

    cap = cv2.VideoCapture(0)
    

    while True:
        event, values = window.read(timeout=20)

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        ret, frame = cap.read()

        if values["-BRIGHTNESS-"]:
            frame = ChangeBrightness(frame, values["-BRIGHTNESS SLIDER-"])
        elif values["-SATURATION-"]:
            frame = ChangeSaturation(frame, values["-SATURATION SLIDER-"])
        elif values["-BLUR-"]:
            frame = ImageSharpen(frame, values["-BLUR SLIDER-"])
        elif values["-HUE-"]:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            frame[:, :, 0] += int(values["-HUE SLIDER-"])
            frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
        elif values["-ENHANCE-"]:
            enh_val = values["-ENHANCE SLIDER-"] / 40
            clahe = cv2.createCLAHE(clipLimit=enh_val, tileGridSize=(8, 8))
            lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
            lab[:, :, 0] = clahe.apply(lab[:, :, 0])
            frame = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
        elif values["-OIL-"]:
            frame = OilPainting(
                frame,
                values["-OIL SLIDER SIZE-"],
                values["-OIL SLIDER LEVEL-"],
            )
        elif values["-WATER-"]:
            frame = Water(
                frame,
                NeighbourhoodSize = values["-WATER SLIDER SIZE-"],
                Range = values["-WATER SLIDER LEVEL-"]
            )
        elif values["-GRAYSCALE-"]:
            frame = GrayScale(frame)
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)
        
    window.close()

if __name__ == "__main__":
    main()


