from Scopul import Scopul, Note, Part
import random
import music21
import os
import music21.midi.translate
import music21.stream.streamStatus
from settings import STONE2STD, OCTAVE_LOWER_LIMIT, OCTAVE_UPPER_LIMIT, START_OCTAVE,NOTE_LENGTH 

class Generator:
    @classmethod
    def gen_stone_note(self, last_stone, stone, last_octave):
        octave = last_octave
        note = STONE2STD[stone % 12]
        if last_stone > stone:
            octave -= 1
        else:
            octave += 1
        
        
        if octave > OCTAVE_UPPER_LIMIT:
            octave -= 2
        
        if octave < OCTAVE_LOWER_LIMIT:
            octave += 2
            
        note = f"{note}{octave}"
        obj = music21.note.Note(pitch=note)
        obj.quarterLength = NOTE_LENGTH
        return {"note":obj, "octave":octave}
    
    @classmethod
    def gen_midi(self, stream, name="output"):
        name = f"{name}.mid"
        mf = music21.midi.translate.streamToMidiFile(stream)
        if os.path.isfile(name):
            os.remove(name)
            
        mf.open(name, "wb")
        mf.write()
        mf.close()
    
    @classmethod
    def gen_note_stream(self, sequence):
        sequence_notes = music21.stream.Stream()
        start_note = music21.note.Note(pitch=STONE2STD[sequence[0]%12]+str(START_OCTAVE))
        start_note.quarterLength = NOTE_LENGTH
        sequence_notes.append(start_note)
        last_stone = sequence[0]
        last_octave = START_OCTAVE
        for stone in sequence[1:]:
            note = self.gen_stone_note(last_stone, stone, last_octave)
            sequence_notes.append(note["note"])
            last_stone = stone
            last_octave = note["octave"]
        return sequence_notes
    
    