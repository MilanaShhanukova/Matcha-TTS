""" from https://github.com/keithito/tacotron

Defines the set of symbols used in text input to the model.
"""
_pad = "_"
_punctuation = ';:,.!?¡¿—-…"«»“” '
_stress_symbol = "'"
_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
russian_lowercase = ''.join(chr(i) for i in range(ord('а'), ord('я') + 1))
russian_uppercase = ''.join(chr(i) for i in range(ord('А'), ord('Я') + 1))


# _letters = russian_lowercase + russian_uppercase + _letters
# _letters_ipa = (
#     "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"
# )

_letters_ipa = ['k', 'l', 's:', 'ʒ', 't~ɕ', 'j', "'ɐ", 'iː', 'fʲ:', 'ɹ', "'ʉ", 'v', "'ɵ", 'ə+r', 'd͡ʒ', 'ʊ', 'ɫ', 'ɪ', 'oː', 'jɵ', 'ɔː', 'ɚ', 'j:', 'dʲ:', 'ʔ', 'sʲ', 'ɛː', 'u', 'nʲ:', 'ʃ', 'd~zʲ', "'je", 't~s', 'ɑː', 'mʲ', 'ɵ', 'ɡʲ', 'jə', 'd:', 'jʊ', 'ɛ', 'k:', 'vʲ:', 'x', 'nʲ', 'n', 'jɪ', 'zʲ', 'ɐ', 'æː', 'n:', 'pʲ:', 'v:', 'r', 'l̩', 't~ɕ:', "'ju", 'xʲ', "'jæ", "'ɪ", 'ɕ', 'b', 'aː', 'o', 'kʲ:', "'ə", 'ɕ:', 'dʲ', 'rʲ', 'd~ʐ', "'ji", 'tʲ:', 'w', 'bʲ', 'p:', 'r:', 'ɝ', 'eː', 'ə', 't', "'ja", "'ʊ", 'b:', 'mʲ:', "'jʉ", "'u", 'z', 'ju', 't~sʲ', 'ɣ', 'z:', 'jæ', 'ð', 'je', 'ʐ', 'ʂ:', 'ɜː', 'ʐ:', 'ʑ:', 'lʲ', 'ɡ:', 'ɨ', 'ji', 'pʲ', 'ɒ', 'ɪː', 'zʲ:', 'ɔ', 'θ', 'ɫ:', 'fʲ', 'p', 'vʲ', 'i', 't~ʂ', "'i", "'a", 'ŋ', 'ɜ', 'ʊ̯', 'ɪ̯', 'n̩', 'kʲ', "'o", 'uː', 'f', 'jʉ', "'ɛ", 's+_', 'ɡ', "'æ", 'ʉ', 'm', 's', 'a', "'e", 'æ', 'tʲ', 'h', 'ɪ+rʲ', 'm:', 'ɑ', 'e', "'jɵ", 'd', 'sʲ:', 'ʌ', 'd~z', 'lʲ:', 't~s+_', 'm̩', 'ʂ', 'ja', 't~s:', 'ɝː', "'ɨ", 'ʍ', 't:', 't͡ʃ', "'jɪ", 'rʲ:']

# Export all symbols:
symbols = [_pad] + [_stress_symbol] + list(_punctuation) + _letters_ipa 

# Special symbol ids
SPACE_ID = symbols.index(" ")
