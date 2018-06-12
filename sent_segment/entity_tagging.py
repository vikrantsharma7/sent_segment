# -*- coding: utf-8 -*-

# TAG_PREFIX = '<!'
# TAG_SUFFIX = '!>'

TAG_PREFIX = 'QQQTAG'
TAG_SUFFIX = 'TAGQQQ'

BANKING_TAG = TAG_PREFIX + 'BANKINGTERM' + TAG_SUFFIX
BANK_TAG = TAG_PREFIX + 'BANKNAME' + TAG_SUFFIX
CITY_TAG = TAG_PREFIX + 'CITYNAME' + TAG_SUFFIX
LOCALITY_TAG = TAG_PREFIX + 'LOCALITYNAME' + TAG_SUFFIX
AIRPORT_CODES_TAG = TAG_PREFIX + 'AIRPORTNAME' + TAG_SUFFIX
RETAIL_STORES_TAG = TAG_PREFIX + 'RETAILSTORE' + TAG_SUFFIX
RETAIL_BRANDS_TAG = TAG_PREFIX + 'RETAILBRAND' + TAG_SUFFIX
RETAIL_CATEGORIES_TAG = TAG_PREFIX + 'RETAILCATEGORY' + TAG_SUFFIX
RETAIL_PRODUCT_TYPE_TAG = TAG_PREFIX + 'RETAILPRODUCTTYPE' + TAG_SUFFIX
WEBSITE_TAG = TAG_PREFIX + 'WEBSITENAME' + TAG_SUFFIX
COMMON_TECHNICAL_TERMS_TAG = TAG_PREFIX + 'COMMONTECHTERM' + TAG_SUFFIX
SERVICE_PROVIDERS_TAG = TAG_PREFIX + 'SERVICEPROVIDER' + TAG_SUFFIX
AIRLINE_NAMES_TAG = TAG_PREFIX + 'AIRLINENAME' + TAG_SUFFIX
COMPANY_NAMES_TAG = TAG_PREFIX + 'COMPANYNAME' + TAG_SUFFIX

# Tags used by Machine Translation
MT_TAG_MAPPING = {'brand': 'RETAILBRAND',
                  'category': 'RETAILCATEGORY',
                  'sub_category': 'RETAILSUBCATEGORY',
                  'product_type': 'RETAILPRODUCTTYPE',
                  'banking_term': 'BANKINGTERM',
                  'city': 'CITYNAME',
                  'locality': 'LOCALITYNAME',
                  'airport': 'AIRPORTNAME',
                  'retail_store': 'RETAILSTORE',
                  'bank': 'BANKNAME',
                  'website': 'WEBSITENAME',
                  'common_tech_term': 'COMMONTECHTERM',
                  'service_provider': 'SERVICEPROVIDER',
                  'airline': 'AIRLINENAME',
                  'company': 'COMPANYNAME'
                  }

# We are not going to use all spacy tags. Based on experiments,
# the below work well with spacy for our datasets.
SPACY_TAGS_TO_USE = ['QUANTITY', 'GPE', 'PERSON', 'DATE', 'ORG']

SHORT_FORMS_REGEX = {
    r'\b(acc|act)\b': r'account',
    r'\b(t\s*n\s*c|t\s*&\s*c)s?\b': r'terms and conditions',
    r'\b(min\*order)\b': r'minimum order',
    r'\b(XX+)(To)\b': r'\1 \2',
    r'\b(o\s*/\s*s)\b': r'outstanding',
    r'\b(avlbl|avl)\b': r'available',
    r"\b(appx|approx)\b": r"approximately",
    r'\b(txn|trxn|tcn)\b': r'transaction',
    r'\b(plz|pls)\b': r'please',
    r'\b(pvt\.?)\b': r'private',
    r'\b(ltd\.?)\b': r'limited',
    r'\b(pn?ts)\b': r'points',
    r'\b(regd\.?)\b': r'registered',
    r'\b(no\.|num)\s?[:\-]?\b':r'number ',
    r'\b(wef|w\.e\.f)\b': r'with effect from',
    r"\b(wi\s*fi|wi\-fi)\b": r"WIFI",
    r'\b(rd\.?)\b': r"road",
    r'\b(ref.?|reference)\s+(number|no.?|num.?)\b': r'reference number ',
    r'\b(e\.g\.)': u'for example',
    r'\b(i\.e\.)': u'that is',
    r'\b(etc)\b': u'and other things'
}

COMMON_ABBREVS = {
    'vld': 'valid',
    'bal': 'balance',
    'cpn': 'coupon',
    'amt': 'amount',
    'mins': 'minutes',
    'hrs': 'hours',
    'appln': 'application',
    'invstmt': 'investment',
    'wrth': 'worth',
    'cust': 'customer',
    'ack': 'acknowledgement',
    'incl': 'inclusive',
    'jnctn': 'junction',
    'ref': 'reference',
    'curr': 'current',
    'mpinto': 'mpin to',
    'clr': 'clear',
    'bglr': 'bangalore',
    'tca': '. terms and conditions apply.',
    'awb': 'air way bill',
    'invsmt': 'investment',
    'avlble': 'available',
    'b4': 'before',
    'cant': 'cannot',
    'immdtly': 'immediately',
    'abt': 'about',
    'wef': 'with effect from',
    'estmt': 'estimate',
    'uptil': 'uptill',
    'tkt': 'ticket',
    'mkt': 'market',
    'frm': 'from',
    'apts': 'Apartments',
    'spl': 'special',
    'blr': 'Bengaluru',
    'blore': 'Bangalore',
    'govt': 'government',
    'dtls': 'details',
    'val': 'validity',
    'builtin': 'built in',
    'utr': 'UTR',
    'tue': 'tuesday',
    'paidif': 'paid if',
    'easyemi': 'easy EMI',
    'thru': 'through',
    'eod': 'end of day',
    'txns': 'transactions',
    'sep': 'september',
    'onetime': 'one time',
    'dom': 'domestic',
    'veg': 'vegetarian',
    'vs': 'versus',
    'sept': 'september',
    'tranx': 'transaction',
    'lmt': 'limit',
    'jul': 'july',
    'aug': 'august',
    'jun': 'june',
    'flt': 'flight',
    'nov': 'november',
    'dont': 'do not',
    'jan': 'january',
    'apr': 'april',
    'feb': 'february',
    'dec': 'december',
    'oct': 'october',
    'upto': 'up to',
    'gonna': u'going to',
    'gotta': u'got to'
}

COMMON_SHORT_FORMS = {
    "ain't": "am not",
    "amn't": "am not",
    "aren't": "are not",
    "can't": "can not",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "he had not have",
    "hasn't": "has not",
    "hasn't've": "has not have",
    "haven't": "have not",
    "he'd": "he had",
    "he'd'n't": "he had not",
    "he'd'n't've": "he had not have",
    "he'd've": "he would have",
    "he'll": "he shall",
    "he's": "he has",
    "he'sn't": "he has not",
    "how'd": "how did",
    "how'll": "how will",
    "how's": "how has",
    "i'd": "I had",
    "i'd'n't": "I had not",
    "i'd'n't've": "I had not have",
    "i'd've": "I would have",
    "i'll": "I shall",
    "i'm": "I am",
    "i've": "I have",
    "i'ven't": "I have not",
    "isn't": "is not",
    "it'd": "it had",
    "it'd'n't": "it had not",
    "it'd'n't've": "it had not have",
    "it'd've": "it would have",
    "it'll": "it shall",
    "it's": "it has",
    "it'sn't": "it has not",
    "let's": "let us",
    "ma'am": "madam",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "might've": "might have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "must've": "must have",
    "needn't": "need not",
    "not've": "not have",
    "ol'": "old",
    "oughtn't": "ought not",
    "oughtn't've": "ought not to have",
    "shan't": "shall not",
    "she'd": "she had",
    "she'd'n't": "she had not",
    "she'd'n't've": "she had not have",
    "she'd've": "she would have",
    "she'll": "she shall",
    "she's": "she has",
    "she'sn't": "she has not",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "somebody'd": "somebody had",
    "somebody'd'n't": "somebody had not",
    "somebody'd've": "somebody would have",
    "somebody'dn't've": "somebody had not have",
    "somebody'll": "somebody shall",
    "somebody's": "somebody has",
    "someone'd": "someone had",
    "someone'd'n't": "someone had not",
    "someone'd'n't've": "someone had not have",
    "someone'd've": "someone would have",
    "someone'll": "someone shall",
    "someone's": "someone has",
    "something'd": "something had",
    "something'd'n't": "something had not",
    "something'd'n't've": "something had not have",
    "something'd've": "something would have",
    "something'll": "something shall",
    "something's": "something has",
    "'sup": "what is up",
    "that'll": "that will",
    "that's": "that has",
    "there'd": "there had",
    "there'd'n't": "there had not",
    "there'd'n't've": "there had not have",
    "there'd've": "there would have",
    "there're": "there are",
    "there's": "there has",
    "they'd": "they had",
    "they'dn't": "they had not",
    "they'dn't've": "they had not have",
    "they'd've": "they would have",
    "they'd'ven't": "they would have not",
    "they'll": "they shall",
    "they'lln't've": "they will not have",
    "they'll'ven't": "they will have not",
    "they're": "they are",
    "they've": "they have",
    "they'ven't": "they have not",
    "'tis": "it is",
    "'twas": "it was",
    "wanna": "want to",
    "wasn't": "was not",
    "we'd": "we had",
    "we'd've": "we would have",
    "we'd'n't": "we had not",
    "we'dn't've": "we had not have",
    "we'll": "we will",
    "we'lln't've": "we will not have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'd": "what did",
    "what'll": "what shall",
    "what're": "what are",
    "what's": "what has",
    "what've": "what have",
    "when's": "when has",
    "where'd": "where did",
    "where's": "where has",
    "where've": "where have",
    "who'd": "who would",
    "who'd've": "who would have",
    "who'll": "who shall",
    "who're": "who are",
    "who's": "who has",
    "who've": "who have",
    "why'd": "why did",
    "why'll": "why will",
    "why're": "why are",
    "why's": "why has",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd've": "you all would have",
    "y'all'dn't've": "you all would not have",
    "y'all'll": "you all will",
    "y'all'on't": "you all will not",
    "y'all'll've": "you all will have",
    "y'all're": "you all are",
    "y'all'll'ven't": "you all will have not",
    "you'd": "you had",
    "you'd've": "you would have",
    "you'll": "you shall",
    "you're": "you are",
    "you'ren't": "you are not",
    "you've": "you have",
    "you'ven't": "you have not"
}

LOCALIZATION_STRATEGY = {
    'BRAND': 'transliteration',
    'EMPLOYER': 'transliteration',
    'COMPANY': 'transliteration',
    'PRODUCTTYPE': 'translation',
    'LOCALITY': 'transliteration',
    'SUBCATEGORY': 'translation',
    'CATEGORY': 'translation',
    'CITY': 'transliteration',
    'TOWN': 'transliteration',
    'SALARY': 'unchanged',
    'COUNTRY': 'transliteration',
    'RETAILSTORE': 'transliteration',
    'BANK': 'translation',
    'BANKINGTERM': 'translation',
    'COMMONTECHNICALTERM': 'translation',
    'SERVICEPROVIDER': 'translation'
}

"""RMT Localization Strategy"""
RMT_LOCALIZATION_STRATEGY = {'QQQTAGACCOUNTNUMBERTAGQQQ': {'category_id': '42',
                                                           'pos_tag': 'NNP',
                                                           'strategy': 'UN',
                                                           'trans_category': '0'},
                             'QQQTAGACTORTAGQQQ': {'category_id': '20',
                                                   'pos_tag': 'NNP',
                                                   'strategy': 'T13N',
                                                   'trans_category': '2'},
                             'QQQTAGAIRLINETAGQQQ': {'category_id': '13',
                                                     'pos_tag': 'NNP',
                                                     'strategy': 'T13N',
                                                     'trans_category': '7'},
                             'QQQTAGAIRPORTTAGQQQ': {'category_id': '30',
                                                     'pos_tag': 'NNP',
                                                     'strategy': 'UN',
                                                     'trans_category': '0'},
                             'QQQTAGALNUMTAGQQQ': {'category_id': '31',
                                                   'pos_tag': 'NNP',
                                                   'strategy': 'UN',
                                                   'trans_category': '9'},
                             'QQQTAGAMOUNTTAGQQQ': {'category_id': '33',
                                                    'pos_tag': 'CD',
                                                    'strategy': 'UN',
                                                    'trans_category': '0'},
                             'QQQTAGBANKINGTERMTAGQQQ': {'category_id': '10',
                                                         'pos_tag': 'NNP',
                                                         'strategy': 'T13N',
                                                         'trans_category': '6'},
                             'QQQTAGBANKTAGQQQ': {'category_id': '28',
                                                  'pos_tag': 'NNP',
                                                  'strategy': 'T13N',
                                                  'trans_category': '6'},
                             'QQQTAGBRANDTAGQQQ': {'category_id': '1',
                                                   'pos_tag': 'NNP',
                                                   'strategy': 'T13N',
                                                   'trans_category': '7'},
                             'QQQTAGCARDINALTAGQQQ': {'category_id': '46',
                                                      'pos_tag': 'CD',
                                                      'strategy': 'T13N',
                                                      'trans_category': '10'},
                             'QQQTAGCATEGORYTAGQQQ': {'category_id': '26',
                                                      'pos_tag': 'NNP',
                                                      'strategy': 'T9N',
                                                      'trans_category': '7'},
                             'QQQTAGCITYTAGQQQ': {'category_id': '6',
                                                  'pos_tag': 'NNP',
                                                  'strategy': 'T13N',
                                                  'trans_category': '9'},
                             'QQQTAGCODETAGQQQ': {'category_id': '43',
                                                  'pos_tag': 'NNP',
                                                  'strategy': 'UN',
                                                  'trans_category': '0'},
                             'QQQTAGCOMMONTECHNICALTERMTAGQQQ': {'category_id': '27',
                                                                 'pos_tag': 'NNP',
                                                                 'strategy': 'T9N',
                                                                 'trans_category': '7'},
                             'QQQTAGCOMPANYNAMETAGQQQ': {'category_id': '16',
                                                         'pos_tag': 'NNP',
                                                         'strategy': 'T13N',
                                                         'trans_category': '7'},
                             'QQQTAGCOMPANYTAGQQQ': {'category_id': '3',
                                                     'pos_tag': 'NNP',
                                                     'strategy': 'T13N',
                                                     'trans_category': '7'},
                             'QQQTAGCOUNTRYTAGQQQ': {'category_id': '8',
                                                     'pos_tag': 'NNP',
                                                     'strategy': 'T13N',
                                                     'trans_category': '9'},
                             'QQQTAGDATETAGQQQ': {'category_id': '36',
                                                  'pos_tag': 'CD',
                                                  'strategy': 'T13N',
                                                  'trans_category': '16'},
                             'QQQTAGDATETIMETAGQQQ': {'category_id': '37',
                                                      'pos_tag': 'CD',
                                                      'strategy': 'T13N',
                                                      'trans_category': '16'},
                             'QQQTAGDIRECTORTAGQQQ': {'category_id': '21',
                                                      'pos_tag': 'NNP',
                                                      'strategy': 'T13N',
                                                      'trans_category': '2'},
                             'QQQTAGEMAILIDTAGQQQ': {'category_id': '40',
                                                     'pos_tag': 'NNP',
                                                     'strategy': 'UN',
                                                     'trans_category': '0'},
                             'QQQTAGEMPLOYERTAGQQQ': {'category_id': '2',
                                                      'pos_tag': 'NNP',
                                                      'strategy': 'T13N',
                                                      'trans_category': '2'},
                             'QQQTAGGENRETAGQQQ': {'category_id': '19',
                                                   'pos_tag': 'NNP',
                                                   'strategy': 'T13N',
                                                   'trans_category': '0'},
                             'QQQTAGHASHTAGTAGQQQ': {'category_id': '41',
                                                     'pos_tag': 'NNP',
                                                     'strategy': 'UN',
                                                     'trans_category': '0'},
                             'QQQTAGHTMLENTITYTAGQQQ': {'category_id': '51',
                                                        'pos_tag': 'SYM',
                                                        'strategy': 'UN',
                                                        'trans_category': '0'},
                             'QQQTAGHTMLTAGTAGQQQ': {'category_id': '49',
                                                     'pos_tag': 'SYM',
                                                     'strategy': 'UN',
                                                     'trans_category': '0'},
                             'QQQTAGINDUSTRYTAGQQQ': {'category_id': '14',
                                                      'pos_tag': 'NNP',
                                                      'strategy': 'T13N',
                                                      'trans_category': '7'},
                             'QQQTAGLOCALITYTAGQQQ': {'category_id': '4',
                                                      'pos_tag': 'NNP',
                                                      'strategy': 'T13N',
                                                      'trans_category': '9'},
                             'QQQTAGNAMEDENTITYTAGQQQ': {'category_id': '17',
                                                         'pos_tag': 'NNP',
                                                         'strategy': 'T13N',
                                                         'trans_category': '0'},
                             'QQQTAGNDWTAGQQQ': {'category_id': '18',
                                                 'pos_tag': 'NNP',
                                                 'strategy': 'T13N',
                                                 'trans_category': '0'},
                             'QQQTAGNUMBERTAGQQQ': {'category_id': '45',
                                                    'pos_tag': 'CD',
                                                    'strategy': 'UN',
                                                    'trans_category': '0'},
                             'QQQTAGORDINALTAGQQQ': {'category_id': '48',
                                                     'pos_tag': 'CD',
                                                     'strategy': 'T13N',
                                                     'trans_category': '21'},
                             'QQQTAGPERCENTTAGQQQ': {'category_id': '44',
                                                     'pos_tag': 'CD',
                                                     'strategy': 'UN',
                                                     'trans_category': '0'},
                             'QQQTAGPERIODTAGQQQ': {'category_id': '47',
                                                    'pos_tag': 'CD',
                                                    'strategy': 'T13N',
                                                    'trans_category': '13'},
                             'QQQTAGPHONENUMBERTAGQQQ': {'category_id': '38',
                                                         'pos_tag': 'NNP',
                                                         'strategy': 'UN',
                                                         'trans_category': '0'},
                             'QQQTAGPLACEHOLDERTAGQQQ': {'category_id': '50',
                                                         'pos_tag': 'NNP',
                                                         'strategy': 'UN',
                                                         'trans_category': '0'},
                             'QQQTAGPRODUCTTYPETAGQQQ': {'category_id': '25',
                                                         'pos_tag': 'NNP',
                                                         'strategy': 'T9N',
                                                         'trans_category': '7'},
                             'QQQTAGQUANTITYTAGQQQ': {'category_id': '32',
                                                      'pos_tag': 'NNP',
                                                      'strategy': 'UN',
                                                      'trans_category': '0'},
                             'QQQTAGRESTAURANTTAGQQQ': {'category_id': '12',
                                                        'pos_tag': 'NNP',
                                                        'strategy': 'T13N',
                                                        'trans_category': '9'},
                             'QQQTAGRETAILSTORETAGQQQ': {'category_id': '9',
                                                         'pos_tag': 'NNP',
                                                         'strategy': 'T13N',
                                                         'trans_category': '0'},
                             'QQQTAGSALARYTAGQQQ': {'category_id': '29',
                                                    'pos_tag': 'CD',
                                                    'strategy': 'UN',
                                                    'trans_category': '0'},
                             'QQQTAGSERVICEPROVIDERTAGQQQ': {'category_id': '11',
                                                             'pos_tag': 'NNP',
                                                             'strategy': 'T13N',
                                                             'trans_category': '7'},
                             'QQQTAGSOURCETAGQQQ': {'category_id': '24',
                                                    'pos_tag': 'NNP',
                                                    'strategy': 'T13N',
                                                    'trans_category': '0'},
                             'QQQTAGSPLHYPHENATEDTERMTAGQQQ': {'category_id': '15',
                                                               'pos_tag': 'NNP',
                                                               'strategy': 'T13N',
                                                               'trans_category': '7'},
                             'QQQTAGSUBCATEGORYTAGQQQ': {'category_id': '5',
                                                         'pos_tag': 'NNP',
                                                         'strategy': 'T13N',
                                                         'trans_category': '7'},
                             'QQQTAGTIMETAGQQQ': {'category_id': '34',
                                                  'pos_tag': 'CD',
                                                  'strategy': 'T13N',
                                                  'trans_category': '16'},
                             'QQQTAGTIMEZONETAGQQQ': {'category_id': '35',
                                                      'pos_tag': 'NNP',
                                                      'strategy': 'UN',
                                                      'trans_category': '0'},
                             'QQQTAGTITLETAGQQQ': {'category_id': '23',
                                                   'pos_tag': 'NNP',
                                                   'strategy': 'T13N',
                                                   'trans_category': '0'},
                             'QQQTAGTOWNTAGQQQ': {'category_id': '7',
                                                  'pos_tag': 'NNP',
                                                  'strategy': 'T13N',
                                                  'trans_category': '9'},
                             'QQQTAGUNICODESTRINGTAGQQQ': {'category_id': '52',
                                                           'pos_tag': 'NNP',
                                                           'strategy': 'UN',
                                                           'trans_category': '0'},
                             'QQQTAGURLTAGQQQ': {'category_id': '39',
                                                 'pos_tag': 'NNP',
                                                 'strategy': 'UN',
                                                 'trans_category': '0'},
                             'QQQTAGUNKNOWNTAGQQQ': {'category_id': '53',
                                                     'pos_tag': 'NNP',
                                                     'strategy': 'UN',
                                                     'trans_category': '0'},
                             'QQQTAGDOMAINPHRASETAGQQQ': {'category_id': '54',
                                                          'pos_tag': 'NNP',
                                                          'strategy': 'T13N',
                                                          'trans_category': '0'},
                             'QQQTAGLANGUAGETAGQQQ': {'category_id': '54',
                                                      'pos_tag': 'NNP',
                                                      'strategy': 'T13N',
                                                      'trans_category': '0'},
                             'QQQTAGWRITERTAGQQQ': {'category_id': '22',
                                                    'pos_tag': 'NNP',
                                                    'strategy': 'T13N',
                                                    'trans_category': '2'}}

# Miscellaneous
COMMON_HONORIFICS = ['Mr', 'Ms', 'Mrs', 'Dr', 'Miss', 'Sir', 'General', 'Captain',
                     'Father', 'Doctor', 'Earl', 'Master', 'Mx', 'Madam', 'Dame',
                     'Lord', 'Lady', 'Esq', 'Prof', 'Professor']

COMMON_UNITS = ['°c', '°f', 'k', '°ré', '°n', '°ra', 'm³', 'dm³', 'cm³', 'l', 'dl', 'cl', 'ml', 'fl oz', 'fl oz', 'in³',
                'ft³', 'yd³', 'gal', 'gal', 'bbl', 'pt(imp)', 'pt(us fl)', 'pt(us dry)', 'km', 'm', 'dm', 'cm', 'mm',
                'mi', 'in', 'ft', 'yd', 'nautical mile', 't', 'kg', 'hg', 'g', 'dg', 'cg', 'mg', 'µg', 'carat', 'grain',
                'oz (av)', 'lb (av)', 'cwt', 'cwt', 'ton', 'ton', 'st', 'km²', 'm²', 'dm²', 'cm²', 'mm²', 'ha', 'a',
                'ca', 'mile²', 'in²', 'yd²', 'ft²', 'ro', 'acre', 'nautical mile²', 'kmph', 'km/h', 'mps', 'm/s', 'mph',
                'mi/h', 'knot', 'nautical mile/h', 'ma', 'b', 'b', 'kb', 'bytes', 'h', 'min', 's', 'ms', 'µs',
                'nanosecond', 'picosecond', 'femtosecond', 'attosecond', 'hz', 'khz', 'mhz', 'ghz', 'atm', 'bar',
                'mbar', 'pa', 'hpa', 'psi', 'torr', 'j', 'kj', 'cal', 'kcal', 'wh', 'kwh', 'btu', 'thm', 'ft-lb',
                'celsius', 'fahrenheit', 'kelvin', 'reaumur', 'newton', 'rankine', 'cubic meter', 'cubic decimeter',
                'cubic centimeter', 'liter', 'deciliter', 'centiliter', 'milliliter', 'fluid ounce', 'fluid ounce',
                'cubic inch', 'cubic foot', 'cubic yard', 'gallon uk', 'gallon us', 'petroleum barrel', 'pint',
                'fluid pint', 'dry pint', 'kilometer', 'meter', 'decimeter', 'centimeter', 'millimeter', 'mile', 'inch',
                'foot', 'yard', 'nautical mile', 'tonne', 'kilogram', 'hectogram', 'gram', 'grams', 'decigram',
                'centigram', 'mah', 'feet', 'square feet', 'gb', 'mb', 'kb', 'tb', 'mp', 'megapixel', 'mega pixel',
                'milligram', 'microgram', 'carat', 'grain', 'ounce avoirdupois', 'pound avoirdupois', 'v', 'volt', 'w',
                'watt', 'kilowatt', 'hz', 'kilo hertz', 'mega hertz', 'liter', 'litre',
                'long hundredweight', 'short hundredweight', 'long ton', 'short ton', 'stone', 'square kilometer',
                'square meter', 'square decimeter', 'square centimeter', 'square millimeter', 'hectare', 'are',
                'centiare', 'square mile', 'square inch', 'square yard', 'square foot', 'rood', 'acre',
                'square nautical mile', 'kilometer per hour', 'meter per second', 'mile per hour', 'knot', 'mac', 'bit',
                'byte', 'kilobyte', 'megabyte', 'gigabyte', 'terabyte', 'petabyte', 'exabyte', 'zettabyte', 'yottabyte',
                'hour', 'minute', 'second', 'millisecond', 'microsecond', 'nanosecond', 'picosecond', 'femtosecond',
                'attosecond', 'hertz', 'kilohertz', 'megahertz', 'gigahertz', 'atmosphère', 'bar', 'millibar', 'pascal',
                'hectopascal', 'pounds per square inch', 'torr', 'joule', 'kilojoule', 'calorie', 'kilocalorie',
                'watt-hour', 'kilowatt-hour', 'british thermal unit', 'therm américain', 'foot-pound']
