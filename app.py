from flask import Flask, request, render_template
from numpy import random

import pandas as pd

from keras.models import Sequential
from keras.layers import Dense

import keras


# Create Flask object to run
app = Flask(__name__,template_folder= 'templates' )







Yencoded_anti_acne_serum = pd.get_dummies(pd.read_csv('ancti_acne_serum_ing.csv')['Anti-Acne'])
Yencoded_anti_aging_serum = pd.get_dummies(pd.read_csv('ancti_aging_serum_ing.csv')['Anti-Aging'])
Yencoded_brightning_serum = pd.get_dummies(pd.read_csv('brightning_serum_ing.csv')['Brightning'])

Yencoded_anti_acne_serum_shefee = pd.get_dummies(pd.read_csv('ancti_acne_serum_ing_shefee.csv')['Anti-Acne'])
Yencoded_anti_aging_serum_shefee = pd.get_dummies(pd.read_csv('ancti_aging_serum_ing_shefee.csv')['Anti-Aging'])
Yencoded_brightning_serum_shefee = pd.get_dummies(pd.read_csv('brightning_serum_ing_shefee.csv')['Brightning'])


Yencoded_anti_acne_serum_akmal = pd.get_dummies(pd.read_csv('anti_acne_serum_ing_akmal.csv')['Anti-Acne'])
Yencoded_anti_aging_serum_akmal = pd.get_dummies(pd.read_csv('anti_aging_serum_ing_akmal.csv')['Anti-Aging'])
Yencoded_brightning_serum_akmal = pd.get_dummies(pd.read_csv('anti_bightning_serum_ing_akmal.csv')['Brightning'])



Y_list_serum = [Yencoded_anti_acne_serum,Yencoded_anti_aging_serum,Yencoded_brightning_serum]
Y_list_serum_shefee = [Yencoded_anti_acne_serum_shefee,Yencoded_anti_aging_serum_shefee,Yencoded_brightning_serum_shefee]
Y_list_serum_akmal = [Yencoded_anti_acne_serum_akmal ,Yencoded_anti_aging_serum_akmal ,Yencoded_brightning_serum_akmal ]






Yencoded_anti_acne_serum_model = keras.models.load_model('Yencoded_anti_acne_model')
Yencoded_anti_aging_serum_model = keras.models.load_model('Yencoded_anti_aging_model')
Yencoded_brightning_serum_model= keras.models.load_model('Yencoded_anti_brightning_model')

Yencoded_anti_acne_shefee_model = keras.models.load_model('Yencoded_anti_acne_shefee_model')
Yencoded_anti_aging_shefee_model = keras.models.load_model('Yencoded_anti_aging_shefee_model')
Yencoded_brightning_shefee_model= keras.models.load_model('Yencoded_anti_brightning_shefee_model')




Yencoded_anti_acne_akmal_model = keras.models.load_model('Yencoded_Anti Acne_model_akmal')
Yencoded_anti_aging_akmal_model = keras.models.load_model('Yencoded_Anti aging_model_akmal')
Yencoded_brightning_akmal_model= keras.models.load_model('Yencoded_Brightning_model_akmal')

important_ingredients_acne = ['Benzoyl Peroxide', 'Betaine Salicylate', 'Salicylic Acid', 'Zinc Sulfate', 'Phytosphingosine', 'Potassium Azeloyl Diglycinate/Azelaic Acid', 'Zinc Gluconate', 'Zinc Pca']
important_ingredients_aging = ['Acetyl Hexapeptide-1', 'Ascorbic Acid (Vitamin C/Ascorbyl Glucoside/Magnesium Ascorbyl Phosphate/Tetrahexyldecyl Ascorbate/Ascorbyl Tetraisopalmitate)', 'Carnosine', 'Genistein', 'Ginkgo Biloba', 'Green Tea', 'Hexapeptide-10', 'Hydrolyzed Hyaluronic Acid','Mandelic Acid','Palmitoyl Pentapeptide-4','Palmitoyl Tripeptide-1','Resveratrol','Tocopheryl Acetate','Ubiquinone']
important_ingredients_brightning = ['Acetyl Glucosamine','Arbutin','Ascorbic Acid (Vitamin C/Ascorbyl Glucoside/Magnesium Ascorbyl Phosphate/Tetrahexyldecyl Ascorbate/Ascorbyl Tetraisopalmitate)','Glutathione','Kojic Acid','Lactic Acid','Phenylethyl Resorcinol','Resveratrol','Niacinamide','Tetrapeptide-30','Tranexamic Acid','Undecylenoyl Phenylalanine']
ingllll = [important_ingredients_acne,important_ingredients_aging,important_ingredients_brightning]  





serum_model = [Yencoded_anti_acne_serum_model,Yencoded_anti_aging_serum_model,Yencoded_brightning_serum_model]
serum_model_shefee = [Yencoded_anti_acne_shefee_model,Yencoded_anti_aging_shefee_model,Yencoded_brightning_shefee_model]
serum_model_akmal = [Yencoded_anti_acne_akmal_model ,Yencoded_anti_aging_akmal_model ,Yencoded_brightning_akmal_model]
serum_model_name = ['Yencoded_anti_acne_serum_model','Yencoded_anti_aging_serum_model','Yencoded_brightning_serum_model']



def arrr(predictionss):
   
    prod = list([0] * len(list(predictionss)))
    maxm = max(predictionss)

    indd = list(predictionss).index(maxm)
    return indd




def modreccomenderz(custdetails,modelz,Ymod):
    Y_col = list(Ymod.columns)
    #print(Y_col)
    predictionn = (modelz.predict([givlis(custdetails)]))[0]

    maxm = max(predictionn)

    indd = list(predictionn).index(maxm)

def givlis_serum(dictionin,concern):
    if concern == 'Anti_Acne_serum_ingrdients':
        # Acne_serum = pd.read_csv('serum_anti_acne_cosmly.csv')
       
        # X = Acne_serum[['Age', 'SkinType', 'SkinConcerns', 'SkinTyone']]
        spare_age = '25-34'
        spare_SkinType = 'Combination'
        spare_SkinConcerns = 'Acne'
        spare_SkinTyone = 'Dark'
       
        # print(spare_age,spare_SkinType,spare_SkinConcerns,spare_SkinTyone)
       
        # Xencoded = pd.get_dummies(X)
        # X = Xencoded
        # X_fu = list(X.columns)

        X_fu =  ['Age_13-17', 'Age_18-24', 'Age_25-34', 'Age_35-44', 'Age_45-54',
           'Age_55-120', 'SkinType_Combination', 'SkinType_Dry', 'SkinType_Normal',
           'SkinType_Oily', 'SkinTyone_Dark', 'SkinTyone_Deep', 'SkinTyone_Ebony',
           'SkinTyone_Fair', 'SkinTyone_Light', 'SkinTyone_Medium',
           'SkinTyone_Olive', 'SkinTyone_Porcelain', 'SkinTyone_Tan',
           'SkinConcerns_Acne', 'SkinConcerns_Aging', 'SkinConcerns_Blackheads',
           'SkinConcerns_Calluses', 'SkinConcerns_Cellulite',
           'SkinConcerns_Cuticles', 'SkinConcerns_Dark circles',
           'SkinConcerns_Dullness', 'SkinConcerns_Pores', 'SkinConcerns_Puffiness',
           'SkinConcerns_Redness', 'SkinConcerns_Sensitivity',
           'SkinConcerns_Stretch marks', 'SkinConcerns_Sun damage',
           'SkinConcerns_Uneven skin tones']
        if 'Age'+'_'+dictionin['Age'] not in X_fu:
            dictionin['Age'] = spare_age
       
        if 'SkinType'+'_'+dictionin['SkinType'] not in X_fu:
            dictionin['SkinType'] = spare_SkinType

        if 'SkinConcerns'+'_'+dictionin['SkinConcerns'] not in X_fu:
            dictionin['SkinConcerns'] = spare_SkinConcerns
           
        if 'SkinTyone'+'_'+dictionin['SkinTone'] not in X_fu:
            dictionin['SkinTone'] = spare_SkinTyone                
           

        listofzeros = [0] * len(X_fu)
        listofzeros[X_fu.index('Age'+'_'+dictionin['Age'])] = 1
        listofzeros[X_fu.index('SkinType'+'_'+dictionin['SkinType'])] = 1
        listofzeros[X_fu.index('SkinTyone'+'_'+dictionin['SkinTone'])] = 1
        listofzeros[X_fu.index('SkinConcerns'+'_'+dictionin['SkinConcerns'])] = 1
        return listofzeros
    if concern == 'Anti_Aging_serum_ingrdients':
        #Aging_serum = pd.read_csv('serum_anti_aging_cosmly.csv')
        #X = Aging_serum[['Age', 'SkinType', 'SkinConcerns', 'SkinTyone']]
        spare_age = '25-34'
        spare_SkinType = 'Combination'
        spare_SkinConcerns = 'Aging'
        spare_SkinTyone = 'Dark'
       
       
       
        # Xencoded = pd.get_dummies(X)
        # X = Xencoded
        # X_fu = list(X.columns)
        X_fu = ['Age_13-17', 'Age_18-24', 'Age_25-34', 'Age_35-44', 'Age_45-54',
           'Age_55-120', 'SkinType_Combination', 'SkinType_Dry', 'SkinType_Normal',
           'SkinType_Oily', 'SkinTyone_Dark', 'SkinTyone_Deep', 'SkinTyone_Ebony',
           'SkinTyone_Fair', 'SkinTyone_Light', 'SkinTyone_Medium',
           'SkinTyone_Olive', 'SkinTyone_Porcelain', 'SkinTyone_Tan',
           'SkinConcerns_Acne', 'SkinConcerns_Aging', 'SkinConcerns_Blackheads',
           'SkinConcerns_Calluses', 'SkinConcerns_Cellulite',
           'SkinConcerns_Cuticles', 'SkinConcerns_Dark circles',
           'SkinConcerns_Dullness', 'SkinConcerns_Pores', 'SkinConcerns_Puffiness',
           'SkinConcerns_Redness', 'SkinConcerns_Sensitivity',
           'SkinConcerns_Stretch marks', 'SkinConcerns_Sun damage',
           'SkinConcerns_Uneven skin tones']
       
        if 'Age'+'_'+dictionin['Age'] not in X_fu:
            dictionin['Age'] = spare_age
       
        if 'SkinType'+'_'+dictionin['SkinType'] not in X_fu:
            dictionin['SkinType'] = spare_SkinType

        if 'SkinConcerns'+'_'+dictionin['SkinConcerns'] not in X_fu:
            dictionin['SkinConcerns'] = spare_SkinConcerns
           
        if 'SkinTyone'+'_'+dictionin['SkinTone'] not in X_fu:
            dictionin['SkinTone'] = spare_SkinTyone    

        listofzeros = [0] * len(X_fu)
        listofzeros[X_fu.index('Age'+'_'+dictionin['Age'])] = 1
        listofzeros[X_fu.index('SkinType'+'_'+dictionin['SkinType'])] = 1
        listofzeros[X_fu.index('SkinTyone'+'_'+dictionin['SkinTone'])] = 1
        listofzeros[X_fu.index('SkinConcerns'+'_'+dictionin['SkinConcerns'])] = 1
        return listofzeros
    if concern == 'Brightning_serum_ingrdients':
        #Brightning_serum_ = pd.read_csv('serum_anti_brightning_cosmly.csv')
       
        #X = Brightning_serum_[['Age', 'SkinType', 'SkinConcerns', 'SkinTyone']]
        spare_age = '25-34'
        spare_SkinType = 'Combination'
        spare_SkinConcerns = 'Dullness'
        spare_SkinTyone = 'Dark'
       
       
       
        # Xencoded = pd.get_dummies(X)
        # X = Xencoded
        # X_fu = list(X.columns)
        X_fu = ['Age_13-17', 'Age_18-24', 'Age_25-34', 'Age_35-44', 'Age_45-54',
           'Age_55-120', 'SkinType_Combination', 'SkinType_Dry', 'SkinType_Normal',
           'SkinType_Oily', 'SkinTyone_Dark', 'SkinTyone_Deep', 'SkinTyone_Ebony',
           'SkinTyone_Fair', 'SkinTyone_Light', 'SkinTyone_Medium',
           'SkinTyone_Olive', 'SkinTyone_Porcelain', 'SkinTyone_Tan',
           'SkinConcerns_Acne', 'SkinConcerns_Aging', 'SkinConcerns_Blackheads',
           'SkinConcerns_Calluses', 'SkinConcerns_Cellulite',
           'SkinConcerns_Cuticles', 'SkinConcerns_Dark circles',
           'SkinConcerns_Dullness', 'SkinConcerns_Pores', 'SkinConcerns_Puffiness',
           'SkinConcerns_Redness', 'SkinConcerns_Sensitivity',
           'SkinConcerns_Stretch marks', 'SkinConcerns_Sun damage',
           'SkinConcerns_Uneven skin tones']  
       
        if 'Age'+'_'+dictionin['Age'] not in X_fu:
            dictionin['Age'] = spare_age
       
        if 'SkinType'+'_'+dictionin['SkinType'] not in X_fu:
            dictionin['SkinType'] = spare_SkinType

        if 'SkinConcerns'+'_'+dictionin['SkinConcerns'] not in X_fu:
            dictionin['SkinConcerns'] = spare_SkinConcerns
           
        if 'SkinTyone'+'_'+dictionin['SkinTone'] not in X_fu:
            dictionin['SkinTone'] = spare_SkinTyone  

        listofzeros = [0] * len(X_fu)
        listofzeros[X_fu.index('Age'+'_'+dictionin['Age'])] = 1
        listofzeros[X_fu.index('SkinType'+'_'+dictionin['SkinType'])] = 1
        listofzeros[X_fu.index('SkinTyone'+'_'+dictionin['SkinTone'])] = 1
        listofzeros[X_fu.index('SkinConcerns'+'_'+dictionin['SkinConcerns'])] = 1
        return listofzeros  
       
       
       
       
def givlis_serum_shefee(dictionin,concern):
    if concern == 'Anti_Acne_serum_ingrdients':
        # Acne_serum = pd.read_csv('serum_anti_acne_cosmly.csv')
       
        # X = Acne_serum[['Age', 'SkinType', 'SkinConcerns', 'SkinTyone']]
        spare_age = '25-34'
        spare_SkinType = 'Combination'
        spare_SkinConcerns = 'Acne'
        spare_SkinTyone = 'Dark'
       
        # print(spare_age,spare_SkinType,spare_SkinConcerns,spare_SkinTyone)
       
        # Xencoded = pd.get_dummies(X)
        # X = Xencoded
        # X_fu = list(X.columns)

        X_fu =  ['Age_13-17', 'Age_18-24', 'Age_25-34', 'Age_35-44', 'Age_45-54',
           'Age_55-120', 'SkinType_Combination', 'SkinType_Dry', 'SkinType_Normal',
           'SkinType_Oily', 'SkinTyone_Dark', 'SkinTyone_Deep', 'SkinTyone_Ebony',
           'SkinTyone_Fair', 'SkinTyone_Light', 'SkinTyone_Medium',
           'SkinTyone_Olive', 'SkinTyone_Porcelain', 'SkinTyone_Tan',
           'SkinConcerns_Acne', 'SkinConcerns_Aging', 'SkinConcerns_Blackheads',
           'SkinConcerns_Calluses', 'SkinConcerns_Cellulite',
           'SkinConcerns_Cuticles', 'SkinConcerns_Dark circles',
           'SkinConcerns_Dullness', 'SkinConcerns_Pores', 'SkinConcerns_Puffiness',
           'SkinConcerns_Redness', 'SkinConcerns_Sensitivity',
           'SkinConcerns_Stretch marks', 'SkinConcerns_Sun damage',
           'SkinConcerns_Uneven skin tones']
        if 'Age'+'_'+dictionin['Age'] not in X_fu:
            dictionin['Age'] = spare_age
       
        if 'SkinType'+'_'+dictionin['SkinType'] not in X_fu:
            dictionin['SkinType'] = spare_SkinType

        if 'SkinConcerns'+'_'+dictionin['SkinConcerns'] not in X_fu:
            dictionin['SkinConcerns'] = spare_SkinConcerns
           
        if 'SkinTyone'+'_'+dictionin['SkinTone'] not in X_fu:
            dictionin['SkinTone'] = spare_SkinTyone                
           

        listofzeros = [0] * len(X_fu)
        listofzeros[X_fu.index('Age'+'_'+dictionin['Age'])] = 1
        listofzeros[X_fu.index('SkinType'+'_'+dictionin['SkinType'])] = 1
        listofzeros[X_fu.index('SkinTyone'+'_'+dictionin['SkinTone'])] = 1
        listofzeros[X_fu.index('SkinConcerns'+'_'+dictionin['SkinConcerns'])] = 1
        return listofzeros

    if concern == 'Anti_Aging_serum_ingrdients':
        #Aging_serum = pd.read_csv('serum_anti_aging_cosmly.csv')
        #X = Aging_serum[['Age', 'SkinType', 'SkinConcerns', 'SkinTyone']]
        spare_age = '25-34'
        spare_SkinType = 'Combination'
        spare_SkinConcerns = 'Aging'
        spare_SkinTyone = 'Dark'
       
       
       
        # Xencoded = pd.get_dummies(X)
        # X = Xencoded
        # X_fu = list(X.columns)
        X_fu = ['Age_13-17', 'Age_18-24', 'Age_25-34', 'Age_35-44', 'Age_45-54',
           'Age_55-120', 'SkinType_Combination', 'SkinType_Dry', 'SkinType_Normal',
           'SkinType_Oily', 'SkinTyone_Dark', 'SkinTyone_Deep', 'SkinTyone_Ebony',
           'SkinTyone_Fair', 'SkinTyone_Light', 'SkinTyone_Medium',
           'SkinTyone_Olive', 'SkinTyone_Porcelain', 'SkinTyone_Tan',
           'SkinConcerns_Acne', 'SkinConcerns_Aging', 'SkinConcerns_Blackheads',
           'SkinConcerns_Calluses', 'SkinConcerns_Cellulite',
           'SkinConcerns_Cuticles', 'SkinConcerns_Dark circles',
           'SkinConcerns_Dullness', 'SkinConcerns_Pores', 'SkinConcerns_Puffiness',
           'SkinConcerns_Redness', 'SkinConcerns_Sensitivity',
           'SkinConcerns_Stretch marks', 'SkinConcerns_Sun damage',
           'SkinConcerns_Uneven skin tones']
       
        if 'Age'+'_'+dictionin['Age'] not in X_fu:
            dictionin['Age'] = spare_age
       
        if 'SkinType'+'_'+dictionin['SkinType'] not in X_fu:
            dictionin['SkinType'] = spare_SkinType

        if 'SkinConcerns'+'_'+dictionin['SkinConcerns'] not in X_fu:
            dictionin['SkinConcerns'] = spare_SkinConcerns
           
        if 'SkinTyone'+'_'+dictionin['SkinTone'] not in X_fu:
            dictionin['SkinTone'] = spare_SkinTyone    

        listofzeros = [0] * len(X_fu)
        listofzeros[X_fu.index('Age'+'_'+dictionin['Age'])] = 1
        listofzeros[X_fu.index('SkinType'+'_'+dictionin['SkinType'])] = 1
        listofzeros[X_fu.index('SkinTyone'+'_'+dictionin['SkinTone'])] = 1
        listofzeros[X_fu.index('SkinConcerns'+'_'+dictionin['SkinConcerns'])] = 1
        return listofzeros
    if concern == 'Brightning_serum_ingrdients':
        #Brightning_serum_ = pd.read_csv('serum_anti_brightning_cosmly.csv')
       
        #X = Brightning_serum_[['Age', 'SkinType', 'SkinConcerns', 'SkinTyone']]
        spare_age = '25-34'
        spare_SkinType = 'Combination'
        spare_SkinConcerns = 'Dullness'
        spare_SkinTyone = 'Dark'
       
       
       
        # Xencoded = pd.get_dummies(X)
        # X = Xencoded
        # X_fu = list(X.columns)
        X_fu = ['Age_13-17', 'Age_18-24', 'Age_25-34', 'Age_35-44', 'Age_45-54',
           'Age_55-120', 'SkinType_Combination', 'SkinType_Dry', 'SkinType_Normal',
           'SkinType_Oily', 'SkinTyone_Dark', 'SkinTyone_Deep', 'SkinTyone_Ebony',
           'SkinTyone_Fair', 'SkinTyone_Light', 'SkinTyone_Medium',
           'SkinTyone_Olive', 'SkinTyone_Porcelain', 'SkinTyone_Tan',
           'SkinConcerns_Acne', 'SkinConcerns_Aging', 'SkinConcerns_Blackheads',
           'SkinConcerns_Calluses', 'SkinConcerns_Cellulite',
           'SkinConcerns_Cuticles', 'SkinConcerns_Dark circles',
           'SkinConcerns_Dullness', 'SkinConcerns_Pores', 'SkinConcerns_Puffiness',
           'SkinConcerns_Redness', 'SkinConcerns_Sensitivity',
           'SkinConcerns_Stretch marks', 'SkinConcerns_Sun damage',
           'SkinConcerns_Uneven skin tones']
       
        if 'Age'+'_'+dictionin['Age'] not in X_fu:
            dictionin['Age'] = spare_age
       
        if 'SkinType'+'_'+dictionin['SkinType'] not in X_fu:
            dictionin['SkinType'] = spare_SkinType

        if 'SkinConcerns'+'_'+dictionin['SkinConcerns'] not in X_fu:
            dictionin['SkinConcerns'] = spare_SkinConcerns
           
        if 'SkinTyone'+'_'+dictionin['SkinTone'] not in X_fu:
            dictionin['SkinTone'] = spare_SkinTyone  

        listofzeros = [0] * len(X_fu)
        listofzeros[X_fu.index('Age'+'_'+dictionin['Age'])] = 1
        listofzeros[X_fu.index('SkinType'+'_'+dictionin['SkinType'])] = 1
        listofzeros[X_fu.index('SkinTyone'+'_'+dictionin['SkinTone'])] = 1
        listofzeros[X_fu.index('SkinConcerns'+'_'+dictionin['SkinConcerns'])] = 1
        return listofzeros  





def givlis_serum_akmal(dictionin,concern):
    X_fu = ['White Race', 'Black Race', 'Elder Age', 'Intermediate Age',
       'Young Age', 'Tropical', 'Dry', 'Temperate', 'Continental', 'Polar']

    listofzeros = [0] * len(X_fu)
    if   (dictionin['Age'] == '13-17') or (dictionin['Age'] == '18-24')  or (dictionin['Age'] == '25-34'):
        
        listofzeros[X_fu.index('Young Age')] = 1
    if   (dictionin['Age'] == '35-44') or (dictionin['Age'] == '45-54')  :       
        listofzeros[X_fu.index('Intermediate Age')] = 1
    if   (dictionin['Age'] == '55-120') :
        listofzeros[X_fu.index('Elder Age')] = 1
    if   (dictionin['Race'] == 'White') :
        listofzeros[X_fu.index('White Race')] = 1
    if   (dictionin['Race'] == 'Black') :
        listofzeros[X_fu.index('Black Race')] = 1        
    if   (dictionin['Climate'] == 'Tropical') :
        listofzeros[X_fu.index('Tropical')] = 1
    if   (dictionin['Climate'] == 'Dry') :
        listofzeros[X_fu.index('Dry')] = 1
    if   (dictionin['Climate'] == 'Temperate') :
        listofzeros[X_fu.index('Temperate')] = 1        
    if   (dictionin['Climate'] ==  'Continental') :
        listofzeros[X_fu.index( 'Continental')] = 1           
    if   (dictionin['Climate'] == 'Polar') :
        listofzeros[X_fu.index( 'Polar')] = 1         
    return listofzeros


































def modreccomender_serum(custdetails):
    dc = {}
    dcx = {}
    dcxx = {}
    final = {}
    model_concern = ['Anti_Acne_serum_ingrdients','Anti_Aging_serum_ingrdients','Brightning_serum_ingrdients']
    for modind in range(len(serum_model)):

        predictionn = (serum_model[modind].predict([givlis_serum(custdetails,model_concern[modind])]))[0]
        #maxm = max(predictionn)
        sorted_prediction = sorted( list(predictionn),reverse = True)
        maxm = sorted_prediction[random.randint(5)]
       
        
       

        indd = list(predictionn).index(maxm)

        dc[model_concern[modind]] = (Y_list_serum[modind].columns)[indd]
        if 'Niacinamide' in   dc[model_concern[modind]]:
            dc[model_concern[modind]] = dc[model_concern[modind]].replace('Niacinamide',['Niacinamide','Benzoyl Peroxide','Salicyclic Acid','Phytosphingosine','Zinc                 PCA','Potassium Azeloyl Diglycinate','Geinstein','Zinc Sulphate'][random.randint(7)])  
           
       
       
       
       
       
       
        predictionnx = (serum_model_shefee[modind].predict([givlis_serum_shefee(custdetails,model_concern[modind])]))[0]
        #maxmx = max(predictionnx)
        sorted_prediction = sorted( list(predictionnx),reverse = True)
        maxmx = sorted_prediction[random.randint(5)]       

        inddx = list(predictionnx).index(maxmx)

        dcx[model_concern[modind]] = (Y_list_serum_shefee[modind].columns)[inddx]    




    


        predictionnxx = (serum_model_akmal[modind].predict([givlis_serum_akmal(custdetails,model_concern[modind])]))[0]
        #maxmxx = max(predictionnxx)
        sorted_prediction = sorted( list(predictionnxx),reverse = True)

        maxmxx = sorted_prediction[random.randint(5)]   
        pk = []
        for i in sorted_prediction:
            inddxx = list(predictionnxx).index(i)
            ingri = (Y_list_serum_akmal[modind].columns)[inddxx]
            pk.append(ingri)
        for j in pk:
            if j in ingllll[modind]:
                break
        support = [j]   
        print(support)     
        for s in pk:
            if s not in ingllll[modind] and len(support)<3:
                support.append(s)

        dcxx[model_concern[modind]] = ', '.join(support)                 

       
       
        res =   dcxx[model_concern[modind]] + ','+ dc[model_concern[modind]] + ','+  dcx[model_concern[modind]]
       
        ree      = list(set(res.split(',')))
        sq = []
        for i in ree:
            if i in Y_list_serum_akmal[modind].columns:
                sq.append(i)
            
   
        final[model_concern[modind]]  =        ', '.join(sq)       

    return  final


 
 
 
 
 
 
 
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    product =    str(request.form.get('Product'))
   
    SkinConcerns = str(request.form.get('SkinConcerns'))

    Age = str(request.form.get('Age'))

    SkinType = str(request.form.get('SkinType'))

    Gender = str(request.form.get('Gender'))

    SkinTone = str(request.form.get('SkinTyone'))

    Race = str(request.form.get('Race'))
   
    Climate = str(request.form.get('Climate'))  


               

 
    out = {}
   
   

    if product == 'Anti Acne Serum':
        custdetails = {'SkinConcerns':SkinConcerns,'Age':Age,'SkinType':SkinType,'SkinTone':SkinTone,'Gender':Gender,
                  'Race':Race,'Climate':Climate}
 
        out = modreccomender_serum(custdetails)['Anti_Acne_serum_ingrdients'] 
    if product == 'Anti Aging Serum':
        custdetails = {'SkinConcerns':SkinConcerns,'Age':Age,'SkinType':SkinType,'SkinTone':SkinTone,'Gender':Gender,
                  'Race':Race,'Climate':Climate}
 
        out = modreccomender_serum(custdetails)['Anti_Aging_serum_ingrdients']            
    if product == 'Brightning Serum':
        custdetails = {'SkinConcerns':SkinConcerns,'Age':Age,'SkinType':SkinType,'SkinTone':SkinTone,'Gender':Gender,
                  'Race':Race,'Climate':Climate}
 
        out = modreccomender_serum(custdetails)['Brightning_serum_ingrdients']        
       
    print(out)

    return render_template('index.html', prediction_text= out)



   
   
if __name__ == "__main__":
    app.run()