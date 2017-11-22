import unicodedata
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])



greek_to_latin={'α': 'a', 'β': 'v', 'γ': 'g', 'δ': 'd', 'ε': 'e', 'ζ': 'z',
                'η': 'h', 'θ': 'th', 'ι': 'i', 'κ': 'k', 'λ': 'l', 'μ': 'm',
                'ν': 'n', 'ξ': 'j', 'ο': 'o', 'π': 'p', 'ρ': 'r', 'σ': 's', 'ς':'s',
                'τ': 't', 'υ': 'u', 'φ': 'f', 'χ': 'ch', 'ψ': 'ps', 'ω': 'w',
                'Α': 'A', 'Β': 'V', 'Γ': 'G', 'Δ': 'D', 'Ε': 'E', 'Ζ': 'Z',
                'Η': 'H', 'Θ': 'TH', 'Ι': 'I', 'Κ': 'K', 'Λ': 'L', 'Μ': 'M',
                'Ν': 'N', 'Ξ': 'J', 'Ο': 'O', 'Π': 'P', 'Ρ': 'R', 'Σ': 'S',
                'Τ': 'T', 'Υ': 'U', 'Φ': 'F', 'Χ': 'X', 'Ψ': 'PS', 'Ω': 'W'}


def translate(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([greek_to_latin.get(c) if c in greek_to_latin else c for c in nfkd_form if not unicodedata.combining(c)])

