from generator import Generator
from sequencer import Sequencer

hailstones = Sequencer.fibonacci_series(300)
stream = Generator.gen_note_stream(hailstones)
Generator.gen_midi(stream, "Output")

    



    
