import PySimpleGUI as ps

AppLayout = [
    [
        ps.Input(key ='-INPUT-'), 
        ps.Spin(['km to m','m to km','kg to grams','grams to kg', 'sec to min', 'min to sec'],key ='-UNITS-'), 
        ps.Button('Convert',key='-CONVERT-')    
    ],

    [ps.Text('Output',key='-OUTPUT-')]
]

if __name__ == '__main__':

    window = ps.Window('My Converter', AppLayout)
    while True:
        event, values = window.read()
        if event == ps.WIN_CLOSED:
            break
        if event == '-CONVERT-':
            input_value = values['-INPUT-']
            if input_value.isnumeric():
                match values['-UNITS-']:
                    case 'km to m':
                        output = round(float(input_value) * 1000, 2)
                        output_string = f'{input_value} km equals {output} m.'
                    case 'm to km':
                        output = round(float(input_value) / 1000, 2)
                        output_string = f'{input_value} km equals {output} m.'
                    case 'kg to grams':
                        output = round(float(input_value) * 1000, 2)
                        output_string = f'{input_value} kg equal {output} g.'
                    case 'grams to kg':
                        output = round(float(input_value) / 1000 , 2)
                        output_string = f'{input_value} g equal {output} kg.'
                    case 'min to sec':
                        output = round(float(input_value) * 60,2)
                        output_string = f'{input_value} minutes equal {output} seconds.' 
                    case 'sec to min':
                        output = round(float(input_value) / 60,2)
                        output_string = f'{input_value} seconds equal {output} minutes.' 

                window['-OUTPUT-'].update(output_string) # updating the output with the answer
            else:
                window['-OUTPUT-'].update('Please enter a valid number!(round decimals to nearest whole numbers.)') # Updating the output with the error message

    window.close()

