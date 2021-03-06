"""Motifs in Dictionaries.

Here you can define the name of the motif and the series of midi-notes that
make up that motif.
Way more efficient than an unjustified class.

TODO: re-order to have a config loader before execution of prototypes, etc...
"""

import configparser
import os

currentpath = os.path.dirname(os.path.abspath(__file__))
projectdir = os.path.abspath(os.path.join(currentpath, os.pardir))

config = configparser.ConfigParser()
config.read(projectdir + '/default_setup.ini', encoding='utf8')

try:
    motif_1 = config['snippets midi mapping'].get('motif_1').split(',')
    motif_2 = config['snippets midi mapping'].get('motif_2').split(',')
    mini_motif_1_low = config['snippets midi mapping'].get('mini_motif_1_low').split(',')
    mini_motif_2_low = config['snippets midi mapping'].get('mini_motif_2_low').split(',')
    mini_motif_3_low = config['snippets midi mapping'].get('mini_motif_3_low').split(',')
    mini_motif_1_mid = config['snippets midi mapping'].get('mini_motif_1_mid').split(',')
    mini_motif_2_mid = config['snippets midi mapping'].get('mini_motif_2_mid').split(',')
    mini_motif_3_mid = config['snippets midi mapping'].get('mini_motif_3_mid').split(',')    
    mini_motif_1_hi = config['snippets midi mapping'].get('mini_motif_1_hi').split(',')
    mini_motif_2_hi = config['snippets midi mapping'].get('mini_motif_2_hi').split(',')
    conditional_1 = config['snippets midi mapping'].get('conditional_1').split(',')
    conditional_2 = config['snippets midi mapping'].get('conditional_2').split(',')
    conditional_3 = config['snippets midi mapping'].get('conditional_3').split(',')
    conditional_result_1 = config['snippets midi mapping'].get('conditional_result_1').split(',')
    conditional_result_2 = config['snippets midi mapping'].get('conditional_result_2').split(',')
    conditional_result_3 = config['snippets midi mapping'].get('conditional_result_3').split(',')
    conditional_result_4 = config['snippets midi mapping'].get('conditional_result_4').split(',')
    conditional_result_5 = config['snippets midi mapping'].get('conditional_result_5').split(',')

    #all are lists
    identity_midi = config['lambda'].get('identity_midi').split(',')
    evaluate_function = config['lambda'].get('evaluate_function').split(',')
    select_first = config['lambda'].get('select_first_midi').split(',')
    select_second = config['lambda'].get('select_second_midi').split(',')
    successor = config['lambda'].get('successor_midi').split(',')
    predecessor = config['lambda'].get('predecessor_midi').split(',')
    add_midi = config['lambda'].get('add_midi').split(',')
    substract_midi = config['lambda'].get('substract_midi').split(',')
    mult_midi = config['lambda'].get('mult_midi').split(',')
    division_midi = config['lambda'].get('division_midi').split(',')
    equal_than_midi = config['lambda'].get('equality_midi').split(',')
    greater_than_midi = config['lambda'].get('greater_than_midi').split(',')
    less_than_midi = config['lambda'].get('less_than_midi').split(',')

except KeyError:
    raise LookupError('Missing key information in the config file.')

motifs = {}
motifs_lambda = {}

# motippets
motifs['motif_1'] = list(map(int, motif_1))
motifs['motif_2'] = list(map(int, motif_2))
motifs['mini_motif_1_low'] = list(map(int, mini_motif_1_low))
motifs['mini_motif_2_low'] = list(map(int, mini_motif_2_low))
motifs['mini_motif_3_low'] = list(map(int, mini_motif_3_low))
motifs['mini_motif_1_mid'] = list(map(int, mini_motif_1_mid))
motifs['mini_motif_2_mid'] = list(map(int, mini_motif_2_mid))
motifs['mini_motif_3_mid'] = list(map(int, mini_motif_3_mid))
motifs['mini_motif_1_hi'] = list(map(int, mini_motif_1_hi))
motifs['mini_motif_2_hi'] = list(map(int, mini_motif_2_hi))

motifs['conditional_1'] = list(map(int, conditional_1))
motifs['conditional_2'] = list(map(int, conditional_2))
motifs['conditional_3'] = list(map(int, conditional_3))
motifs['conditional_result_1'] = list(map(int, conditional_result_1))
motifs['conditional_result_2'] = list(map(int, conditional_result_2))
motifs['conditional_result_3'] = list(map(int, conditional_result_3))
motifs['conditional_result_4'] = list(map(int, conditional_result_4))
motifs['conditional_result_5'] = list(map(int, conditional_result_5))

# lambda calculus
motifs_lambda['eval'] = list(map(int, evaluate_function))
motifs_lambda['zero'] = list(map(int, identity_midi))
motifs_lambda['true'] = list(map(int, select_first))
motifs_lambda['false'] = list(map(int, select_second))
motifs_lambda['successor'] = list(map(int, successor))
motifs_lambda['predecessor'] = list(map(int, predecessor))
motifs_lambda['addition'] = list(map(int, add_midi))
motifs_lambda['substraction'] = list(map(int, substract_midi))
motifs_lambda['multiplication'] = list(map(int, mult_midi))
motifs_lambda['division'] = list(map(int, division_midi))
motifs_lambda['equal'] = list(map(int, equal_than_midi))
motifs_lambda['greater'] = list(map(int, greater_than_midi))
motifs_lambda['less'] = list(map(int, less_than_midi))
