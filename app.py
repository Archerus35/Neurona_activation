import streamlit as st
import numpy as np
from PIL import Image

image = Image.open('neurona.png')

input_values = []
weight_values = []
     
st.title("Simulador de neurona")

def sigmoid(x):
    return 1/(1+np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

class Neuron():

  def __init__(self,weights,bias,func):
    self.weights = weights
    self.bias = bias
    self.func = func

  
  def cambiobias(self,bias):
    self.bias = bias

  def hacerfunc(self,func):
    self.func = func
  
  def run(self,input_data):
    x = np.array(input_data)
    peso = np.array(self.weights)
    multi = np.dot(x, peso) + (self.bias)
    #return RELU(multi)
    if self.func == "relu":
      return relu(multi)
    elif self.func == "sigmoid":
      return sigmoid(multi)
    elif self.func == "tanh":
      return tanh(multi)

def inputs_cols_generator(number_inputs, name):
    values = st.columns(number_inputs)
    lista = []
    for i in range(number_inputs):
        with values[i]:
         valores =  st.number_input(f'${name}_{i}$', key=f'{name}_{i}')
         lista.append(valores)

         #values[i]
    return lista
    
    
number_inputs_weights = st.slider(
    'number_inputs',
    1,10, 
    label_visibility="collapsed",
    key='number_inputs_weights'
)
st.write(number_inputs_weights)
st.subheader("Pesos")
w_values= inputs_cols_generator(number_inputs_weights, 'w')
st.write(w_values)
st.subheader("Entradas")
x_values = inputs_cols_generator(number_inputs_weights, 'x')
st.write(x_values)



col_st_1, col_st_2 = st.columns(2)

with col_st_1:
    st.subheader("Sesgo")
    bias = st.number_input("Introduce el valor del sesgo" ,key="bias")
    st.write(bias)

with col_st_2:
    st.subheader("Función de activación")
    activation_function = st.selectbox(
        "Función de activación", 
        ("relu", "tanh", "sigmoid")
    )
    st.write(activation_function)

boton = st.button("Calcular la salida", key="boton1")
if boton:
    conjunto = Neuron(weights=w_values, bias=bias, func=activation_function)
    x = x_values
    salida = conjunto.run(input_data=x)

    st.write(f"La salida es:{salida}")


