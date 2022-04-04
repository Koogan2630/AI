import streamlit as st 
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt 
from streamlit_folium import folium_static
import folium
from PIL import Image 

st.title('TIC 3151')
st.title('Artificial Intelligence')

st.markdown('Prepared by:')
st.markdown('1. Koogan Letchumanan (1181102004)')
st.markdown('2. Muhd Azraei Hadi (1201302190)')

part = st.selectbox('Select a part to view the analysis', [ 'Question 1','Question 3'])


if(part=='Question 1'):
    st.header('1. Question 1')
    st.markdown("a) Selection, Crossover and Mutation Graph")
    
    img3 = Image.open('selection.png')
    st.image(img3)
    st.success("Through the multiple differing types for the selection processes chosen there is only a small margin of difference between the three .As such, the process of selection does not pose a huge determinant for the Genetic Algorithm as long as the process eleviates agents with better fitness over others")
    img3 = Image.open('crossover.png')
    st.image(img3 )
    st.success("Multipoint and Onepoint crossover are not much of a difference . However, this could not be said the same for the Average Multipoint . A possible explanation for such an occurance is that balancing the values over and over slows the elimiaion process for values that are too extreme for the fitness test")
    img3 = Image.open('mutation.png')
    st.image(img3)
    st.success("There is not much difference for Increment/Decrement in the 10% range or Decrement in a 20% range . However solely having an increment to the values somehow stops the fitness to a constant . A possible reason to this is that the mutation chance is too high thus resulting in too many increase in value . In addition to the already large initial values set on the first generation, there is no chance for it to be useful as there is no average reduction in the value . For the other two mutations, as this is tested multiple times the second mutations provides a more reliable mutation for the genetic algorithm")

elif(part=='Question 3'):
    st.header('Clustering Analysis')
    st.markdown("a) Customer segmentation based on Employment Type, Property Type, and State.")
    
    img3aK = Image.open('cluster1.png')
    st.image(img3aK)
    st.success("By using clustering analysis, we were able to do customer segmentation based on employment Type, Property Type, and State. As the features used in this analysis are categorical variables, K-Modes clustering algorithm is used. From the elbow method, the optimal number of clusters to have is 3. Cluster 0 has the most number of customers in the cluster, followed by Cluster 1 and Cluster 2. The cluster with the least number of customers is Cluster 2.")
    
    img3a1 = Image.open('cluster2.png')
    st.image(img3a1 )
    img3a2 = Image.open('cluster3.png')
    st.image(img3a2)
    img3a3 = Image.open('cluster4.png')
    st.image(img3a3)

    st.success("In Cluster 0, there’s an overwhelming majority of customers who works in goverment sector. Most of the customers in Cluster 0 are living in condominium. Cluster 0 has the most number of customers who are from Johor state. Majority of the fresh graduates customers are found in Cluster 1. Most of them live in flat found in cluster 1. Highest number of the customers who are from Kuala Lumpur are also found in Cluster 1. As for Cluster 2, no fresh graduates or goverment or non-employer customers are found in the cluster while the majority of the customers in the cluster are employee . The cluster are mostly from terrace house . The customers who are from Kuala Lumpur are more likely to be found in Cluster 2 . ")

    st.header('Classification Models')
    st.markdown("a) Predict Employment Type of Customer.")

    img5ai = Image.open('features.png')
    st.image(img5ai)
    st.success("Feature selection is performed to find the best features to predict the employment type. Here, Chi2 feature selection is used to perform the feature selection. The reason why Chi2 feature selection is used is due to the data. Chi2 feature selection is best used on categorical and continous data input and categorical output . Since the input and output of the data is mostly categorical and continous , therefore Chi2 feature selection is used. The result shows the best results of the feature selection with the highest being Loan Amount meaning Loan Amount contributes the highest in predicting the employment typeof the customer. SelectKBest is used to select the best features for model evaluation.")

    img5b1 = Image.open('accurancy.png')
    st.image(img5b1)
    st.success("From the observation, we can see that the Decision Tree shows the highest accuracy after tuning , however Naive Bayes accuracy is low. Therefore, we conclude that the Decision Tree is the most suitable model for predicting the employment type.")
    
    