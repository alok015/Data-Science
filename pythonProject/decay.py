import pandas as pd
def create_decay(var_to_decay,data):
    for i in range(1,10):
        decay_col = var_to_decay + '_' + str(i*10)
        data[decay_col] = 0.0
        data[decay_col][0] = data[var_to_decay][0]
        for index in range (1,len(data[var_to_decay])):
            decay_factor = i * 0.1
            data[decay_col][index] = (decay_factor * data[decay_col][index-1]) + (1 - decay_factor)*data[var_to_decay][index]

def data_prepare():
    data = pd.read_csv("C:/Users/apratapsingh/Desktop/icy_data_tens.csv")
    var_to_decay =['Tot_FSI_Qty','Base_Dollars']

    for i in range(len(var_to_decay)):
        create_decay(var_to_decay[i], data)


    data.to_csv("model_data_1.csv")


data_prepare()
