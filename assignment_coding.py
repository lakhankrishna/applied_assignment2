import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def Create_dataframes(path_dataset):
    """
    The method is used for getting 2 dataframe from the given dataframe.
    parameters: 
    1. Path_data 
    which is used for taking the path of dataset.
    """
    climate_data = pd.read_csv(path_dataset)
    climate_data_transpose = pd.DataFrame.transpose(climate_data)
    h = climate_data_transpose.iloc[0].values.tolist()
    climate_data_transpose.columns = h
    climate_data=climate_data.drop(columns=['Indicator Code','Country Code'])
    climate_data_transpose=climate_data_transpose.iloc[4:]
    return climate_data_transpose,climate_data

col_as_countries, col_as_years = Create_dataframes('climate_world_dataset.csv')

indi_name=col_as_years.iloc[:,1].unique()

countries= col_as_countries.columns.unique()

africa=['Africa Eastern and Southern','Africa Western and Central','Middle East & North Africa']


africa_dataframe = col_as_years[col_as_years['Country Name'] == africa[0]]

for region in africa[1:]:
    africa_dataframe = pd.concat([africa_dataframe,col_as_years[col_as_years['Country Name'] == region]])


#bar plots 1
indi='Urban population'
indi_df = africa_dataframe[africa_dataframe['Indicator Name']== indi]
indi_df =indi_df .drop(columns=['Indicator Name'])
indi_df =indi_df .transpose()
header = indi_df .iloc[0].values.tolist()
indi_df .columns = header
indi_df =indi_df.iloc[1:,:]
indi_df [45:60].plot(kind='bar',figsize=(20,10))
plt.ylabel("urban population in africa region from 2005")
plt.title('Urban population')
plt.xlabel('years')
plt.show()

#bar plot 2
indi='CO2 emissions (kt)'
indi_df = africa_dataframe[africa_dataframe['Indicator Name']== indi]
indi_df =indi_df .drop(columns=['Indicator Name'])
indi_df =indi_df .transpose()
header = indi_df .iloc[0].values.tolist()
indi_df .columns = header
indi_df =indi_df.iloc[1:,:]
   
indi_df [45:60].plot(kind='bar',figsize=(20,10))
plt.ylabel('CO2 emissions (kt)')
plt.title('CO2 emissions in africa from 2005')
plt.xlabel('years')
plt.show()


def correlations_plotting(dataframe,indicatr_name,region):
    '''
    The method is used for plotting correlation map from the dataframe using indicatorsname and region.
    parameter:
        1.dataframe: input dataframe to be used.
        2.indicatr: the list of indicator used in correlation
        3.region: africa region.
    '''
    correlation_df=dataframe[dataframe['Country Name']==region]
    x=[]
    for indi in indicatr_name:
        tem_df=correlation_df[correlation_df['Indicator Name']==indi]
        tem_df=tem_df.squeeze()
        x.append(tem_df)
    correlation_df=pd.DataFrame(x)
    correlation_df=correlation_df.iloc[:,1:]
    correlation_df=correlation_df.transpose()
 
    correlation_df.columns = correlation_df.iloc[0].values.tolist()
    correlation_df=correlation_df.iloc[1:,:]
    correlation_df=correlation_df.iloc[45:60,:]
    correlation_df=correlation_df.fillna(correlation_df.mean())
    sns.heatmap(
        correlation_df.corr(), 
        cmap="Dark2", annot=True
    )
    plt.title(region+" indicators correlation")
    plt.show()

indi_for_correlation = ['Urban population','Mortality rate, under-5 (per 1,000 live births)','Total greenhouse gas emissions (kt of CO2 equivalent)','Electricity production from coal sources (% of total)','Electricity production from oil sources (% of total)']
correlations_plotting(africa_dataframe, indi_for_correlation, 'Africa Eastern and Southern')
correlations_plotting(africa_dataframe, indi_for_correlation,'Africa Western and Central')

#Line plots 1
indi='Electric power consumption (kWh per capita)'
indi_df = africa_dataframe[africa_dataframe['Indicator Name']== indi]
indi_df =indi_df .drop(columns=['Indicator Name'])
indi_df =indi_df .transpose()
header = indi_df .iloc[0].values.tolist()
indi_df .columns = header
indi_df =indi_df.iloc[1:,:]
indi_df [45:60].plot(kind='line',figsize=(20,10))
plt.ylabel("Electric power consumption  ")
plt.title('Electric power consumption  in africa region from 2005')
plt.xlabel('years')
plt.show()

#Line plot 2
indi='Electricity production from renewable sources, excluding hydroelectric (% of total)'
indi_df = africa_dataframe[africa_dataframe['Indicator Name']== indi]
indi_df =indi_df .drop(columns=['Indicator Name'])
indi_df =indi_df .transpose()
header = indi_df .iloc[0].values.tolist()
indi_df .columns = header
indi_df =indi_df.iloc[1:,:]
   
indi_df [45:60].plot(kind='line',figsize=(20,10))
plt.ylabel('Electricity production from renewable sources')
plt.title('Electricity production from renewable sources from 2005')
plt.xlabel('years')
plt.show()

#Line plot 3
indi='Electricity production from oil sources (% of total)'
indi_df = africa_dataframe[africa_dataframe['Indicator Name']== indi]
indi_df =indi_df .drop(columns=['Indicator Name'])
indi_df =indi_df .transpose()
header = indi_df .iloc[0].values.tolist()
indi_df .columns = header
indi_df =indi_df.iloc[1:,:]
   
indi_df [45:60].plot(kind='line',figsize=(20,10))
plt.ylabel('Electricity production from oil sources')
plt.title('Electricity production from oil sources from 2005')
plt.xlabel('years')
plt.show()