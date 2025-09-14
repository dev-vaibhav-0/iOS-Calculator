from flet import *

def main(page: Page):
    BG = "#000000"
    FG = "#1C1C1E"
    FWG_NUMBER = "#333333"
    FWG_OPERATOR = "#FF9500"
    FWG_FUNCTION = "#A6A6A6"

    page.title = "Calculator"
    page.bgcolor = BG

    # Display
    display_text = Text("0", size=48, color="white", text_align="right")

    def on_button_click(e):
        value = e.control.text

        if value == "AC":
            display_text.value = "0"
        elif value == "=":
            try:
                display_text.value = str(eval(display_text.value.replace("×", "*").replace("÷", "/")))
            except:
                display_text.value = "Error"
        elif value == "+/-":
            if display_text.value.startswith("-"):
                display_text.value = display_text.value[1:]
            else:
                if display_text.value != "0":
                    display_text.value = "-" + display_text.value
        elif value == "%":
            try:
                display_text.value = str(float(display_text.value) / 100)
            except:
                display_text.value = "Error"
        else:
            if display_text.value in ["0", "Error"]:
                display_text.value = value
            else:
                display_text.value += value

        page.update()

    def make_button(label, bgcolor, color="white", expand=1):
        return ElevatedButton(
            label,
            bgcolor=bgcolor,
            color=color,
            expand=expand,    # makes it fill space like phone buttons
            height=80,
            on_click=on_button_click,
            style=ButtonStyle(shape=RoundedRectangleBorder(radius=40))
        )

    # Layout
    page.add(
        Column(
            [
                Container(
                    content=display_text,
                    expand=1,
                    alignment=alignment.center_right,
                    padding=20,
                ),
                Column(
                    [
                        Row(
                            [
                                make_button("AC", FWG_FUNCTION, "black"),
                                make_button("+/-", FWG_FUNCTION, "black"),
                                make_button("%", FWG_FUNCTION, "black"),
                                make_button("÷", FWG_OPERATOR),
                            ],
                            expand=1,
                            spacing=10
                        ),
                        Row(
                            [
                                make_button("7", FWG_NUMBER),
                                make_button("8", FWG_NUMBER),
                                make_button("9", FWG_NUMBER),
                                make_button("×", FWG_OPERATOR),
                            ],
                            expand=1,
                            spacing=10
                        ),
                        Row(
                            [
                                make_button("4", FWG_NUMBER),
                                make_button("5", FWG_NUMBER),
                                make_button("6", FWG_NUMBER),
                                make_button("-", FWG_OPERATOR),
                            ],
                            expand=1,
                            spacing=10
                        ),
                        Row(
                            [
                                make_button("1", FWG_NUMBER),
                                make_button("2", FWG_NUMBER),
                                make_button("3", FWG_NUMBER),
                                make_button("+", FWG_OPERATOR),
                            ],
                            expand=1,
                            spacing=10
                        ),
                        Row(
                            [
                                make_button("0", FWG_NUMBER, expand=2),  # double-width 0
                                make_button(".", FWG_NUMBER),
                                make_button("=", FWG_OPERATOR),
                            ],
                            expand=1,
                            spacing=10
                        ),
                    ],
                    expand=3,
                    spacing=10
                ),
            ],
            expand=True,
            spacing=10
        )
    )

app(target=main)
