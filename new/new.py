from xtconfig import config

import nextpy as xt
import nextpy as xt
import pyjokes


docs_url = "https://nextpy.org/nextpy/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

class State(xt.State):
    joke: str = "Click the button to get a joke!"

    def generate_joke(self):
        self.joke = pyjokes.get_joke()

def index():
    layout = xt.vstack(
        xt.text(State.joke, font_size="2em"),
        xt.button("Generate Joke", on_click=State.generate_joke),

        spacing="1em",
        align_items="center",
        justify_content="center",
        height="100vh",
   )
    return layout

app = xt.App()
app.add_page(index)
