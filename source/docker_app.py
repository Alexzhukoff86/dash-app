import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np
from numpy import arange
from sklearn.linear_model import HuberRegressor 
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
import dash_table

app = dash.Dash()
server = app.server
data = pd.read_csv('insurance.csv')

df = data.copy()
df2 = data.head(n=5) 
#Label Encoding the data (sex, smoker, and region variables)
object_df = data.select_dtypes(include=['object']).copy() 
#print(object_df.head())
#changing variables to 'category' type 
object_df["sex"] = object_df["sex"].astype('category')
object_df["smoker"] = object_df["smoker"].astype('category') 
object_df["region"] = object_df["region"].astype('category')

#assinging encoded variables using 'cat.codes' 
object_df["sex_binary"] = object_df["sex"].cat.codes 
object_df["smoker_binary"] = object_df["smoker"].cat.codes 
object_df["region_encoded"] = object_df["region"].cat.codes 

df["sex"] = object_df["sex_binary"] 
df["smoker"] = object_df["smoker_binary"] 
df["region"] = object_df["region_encoded"]

df3 = df.head(n=5) 

fig = px.scatter_matrix(data, dimensions=[
    'age', 'sex', 'bmi', 'children', 'smoker', 'charges'], labels = {col:" " for col in data.columns},color='region', size_max =5)
fig.update_traces(diagonal_visible = False)

fig2 = px.histogram(data,x = data['charges'], color = 'region')
# checking the first 10 occurences of the data
# print(data.head(n=10))



app.layout = html.Div([
    #setting the title 
    html.H1("Internship 2020 - The GreatFull Plate", style = {"textAlign": "center","width":"800px", "font-family":"Verdana"}, className = "container"), 
    html.H2("Author: Arcelio E. Perez", style = {"textAlign":"center", "width": "800px", "font-family":"Verdana"}, className = "container"),
    html.H4("*WEBSITE UNDER CONSTRUCTION*", style = {"textAlign":"center", "width": "800px", "font-family":"Verdana"}, className = "container"),
    #tabs 
    dcc.Tabs(id = "tabs", children = [
        dcc.Tab(label = "How To", children = [
            html.Div([
                html.H1("How To Run The Files?", style = {"textAlign": "center", "font-family":"Verdana"}), 
                dcc.Markdown('''
                ## Files to Download:  
                 
                Required files: [insurance.csv](https://raw.githubusercontent.com/arcelioeperez/dash-app/gh-pages/source/insurance.csv) | [requirements.txt](https://raw.githubusercontent.com/arcelioeperez/dash-app/main/assets/requirements.txt) | [app.py](https://raw.githubusercontent.com/arcelioeperez/dash-app/gh-pages/source/app.py).   
                All in one folder - including Makefile: [Files](https://github.com/arcelioeperez/dash-app/tree/gh-pages/source)  
                Optional - only the makefile: [Makefile](https://raw.githubusercontent.com/arcelioeperez/dash-app/gh-pages/source/makefile)  
                
                GitHub:  
                [GitHub Repository](https://github.com/arcelioeperez/dash-app/tree/gh-pages) | [GitHub Pages](https://arcelioeperez.github.io/dash-app/)

                ## Running on Windows:  

                ### Running with Make:  
                If you don't have Make installed you could install it by downloading it on this [website](http://gnuwin32.sourceforge.net/packages/make.htm).  
                You could also download and install 'Chocolatey', which is a package manager for Windows.

                **Please use a Unix-like terminal like Git Bash or Powershell - it makes running programs easier**  

                ```
                #installing Make with Chocolatey 
                choco install make
                ```  
                Running the *app.py* file with *make*:  
                ```
                #installing all the packages with one command
                make packages
                #then running the app.py file
                make app
                ```  
                ### If you don't want to use Make:
                ```
                #installing all the packages with requirements.txt
                pip install -r requirements.txt
                #then running app.py
                python app.py
                ```  
                >*After running the above commands - either with or without make - you must go the localhost link i.e. http://127.0.0.1:8050/*   

                ## Running on MacOS  

                ### Running with Make:  
                Open the terminal and check if you have *make* installed
                ```
                make --version
                ```  
                *If you don't have it installed, you can install it with Homebrew - a package manager for MacOS*

                ### Installing *make* with Brew
                ```
                brew install make
                ```  
                **The rest is similar to the Windows instructions.** 

                **Note: all the files must be in the same directory (folder) and all the packages must be installed prior to running `app.py`.**
                
                ### Links to the plotly and dash documentations:  
                1.[Plotly](https://plotly.com/)  
                2.[Dash](https://dash.plotly.com/)  
                3.[Kaggle Dataset- Medical Cost Personal Datasets by Miri Choi](https://www.kaggle.com/mirichoi0218/insurance)  

                ### Works Cited:  
                1.[Machine Learning Mastery - Random Forest](https://machinelearningmastery.com/random-forest-ensemble-in-python/)  
                2.[Machine Learning Mastery - Huber Regressor](https://machinelearningmastery.com/robust-regression-for-machine-learning-in-python/#:~:text=Regression%20is%20a%20modeling%20task,most%20successful%20being%20linear%20regression.)  
                3.[Scatter Plots](https://www.evl.uic.edu/aej/524/kyoung/Training-scatterplot.html)

                ### Books Recommended: 
                1.[Fooled by Randomness, Nassim Nicholas Taleb](https://www.amazon.com/Fooled-Randomness-Hidden-Markets-Incerto/dp/0812975219)
                
                ''', style={"font-family":"Verdana"}, className = "container", highlight_config={"theme":"dark"})
            ])
        ],style = {"font-family": "Verdana"}),
        dcc.Tab(label = "Data Pre-Processing", children = [
            html.Div([
                html.H1("Data Cleaning", style = {"textAlign":"center", "font-family":"Verdana"}),
                dcc.Markdown('''
                ### Opening the CSV file with Pandas:  
                ```python
                import pandas as pd 
                data = pd.read_csv("insurance.csv", delimiter = ",")
                #the delimiter parameter is optional, pandas could figure out that it is a comma
                #could also use the sep = "," parameter
                ```  

                ### Converting the 'object' varibles (i.e. those that are categorical) to numeric:  
                ```
                #converting data into a dataframe
                data = pd.DataFrame(data = data)

                #Label Encoding the data (sex, smoker, and region variables)
                object_df = data.select_dtypes(include=['object']).copy() 
                #print(object_df.head())
                #changing variables to 'category' type 
                object_df["sex"] = object_df["sex"].astype('category')
                object_df["smoker"] = object_df["smoker"].astype('category') 
                object_df["region"] = object_df["region"].astype('category')

                #assinging encoded variables using 'cat.codes' 
                object_df["sex_binary"] = object_df["sex"].cat.codes 
                object_df["smoker_binary"] = object_df["smoker"].cat.codes 
                object_df["region_encoded"] = object_df["region"].cat.codes

                #assigning colums to the data object 
                data["sex"] = object_df["sex_binary"] 
                data["smoker"] = object_df["smoker_binary"] 
                data["region"] = object_df["region_encoded"] 

                ```  

                ''', style = {"font-family":"Verdana"}, className = "container", highlight_config = {"theme":"dark"})
                ]),
            html.H3("Data With Categorical Variables", style = {"textAlign":"center", "font-family":"Verdana"}),
            dash_table.DataTable(id = "table",
                                 columns = [{"name":i, "id": i} for i in df2.columns ],
                                 data = df2.to_dict("records")),
            html.H3("Data With Numerical Variables", style = {"textAlign":"center","font-family":"Verdana"}),
            dash_table.DataTable(id = "table2",
                                 columns = [{"name":i, "id":i} for i in df3.columns],
                                 data = df3.to_dict("records")),
            dcc.Markdown(''' 
            ### Variables in the data:  
            
            Age: age of the person   
            BMI: body mass index    
            Sex: female (0) or male (1)    
            Children: number of children   
            Smoker: smoker (1) or non-smoker (0)    
            Region: southwest (3), southeast (2), northwest (1), northeast (0)  
            Charges: amount charged by the insurance  

            Data Exploration File: [exploratory_analysis.py](https://github.com/arcelioeperez/dash-app/raw/gh-pages/source/exploratory_analysis.py)  
            Basic Statistics of the data: [statistical_significance](https://github.com/arcelioeperez/dash-app/raw/gh-pages/source/statistical_significance.py) | [stats.txt](https://github.com/arcelioeperez/dash-app/raw/gh-pages/source/stats.txt)  

            ''', style = {"font-family":"Verdana"}, className = "container", highlight_config = {"theme":"dark"})
            ]),
                
        dcc.Tab(label = "Data Exploration", children = [
            html.Div([ 
                html.H1("Scatter Matrix",style = {"textAlign": "center", "font-family":"Verdana"}), 
                dcc.Graph(figure = fig), 
               
                dcc.Markdown(''' 
                ## Python code to generate this chart:  
                ```
                data = pd.read_csv('insurance.csv')
                fig = px.scatter_matrix(data, dimensions=[
                'age', 'sex', 'bmi', 'children', 'smoker', 'charges'], color='region')
                ```
                ##### *Where, 'px' is the 'plotly.express' module to plot the scatter matrix - this is the 'plotly' package.*  

                #### Installing packages and dependencies:    
                ``` 
                pip install dash  
                pip install plotly  
                pip install numpy  
                pip install pandas  
                pip install sklearn  
                ```  
                #### Importing files needed for the app.py program:  
                ``` 
                import dash
                import dash_core_components as dcc
                import dash_html_components as html
                import pandas as pd
                import plotly.graph_objs as go
                from dash.dependencies import Input, Output
                import plotly.express as px
                import numpy as np
                from numpy import arange
                from sklearn.linear_model import HuberRegressor 
                from sklearn.model_selection import cross_val_score
                from sklearn.model_selection import RepeatedKFold
                ```  
                #### Explanation of the Scatter Matrix:  
                A scatter matrix shows that 'all the pair-wise scatter plots of the variables' in a single picture. The diagonal is the variable against 
                itself - therefore, it will show a perfect correlation. For this chart, the diagonal was removed.  

                **As we see from this chart, the predictors that stand out the most are:** 

                Age, BMI (body mass index), and whether someone is a smoker, seem to be the predictors that explain the insurance charges.  
                However, as I will explain next, more analysis is needed in order to make a definitive conclusion. From the linear regression and random forest
                models- and their plots - we could see that this project is complex because it deals with predicting the charges that a person will have given their 
                age, sex, bmi, region, number of children, and if that person is a smoker.  

                One could argue that a 'basic model' would be intuition. For example, we know that if someone is obese, old, and is a smoker that person will have more
                health problems and therefore will probably be charged more. This basic model tells us a lot because we could then use linear regression, random
                forest or any other model to see if we are right in our analysis.  

                An important conclusion is that we are the ones programming and building the models. It doesn't make sense to conclude that we need machine learning techniques,
                Artificial Intelligence (AI), or a mathematical model for every single problem that we have. We sometimes need that basic model to act as a benchmark - sometimes
                that basic model could prove that a machine learning model would even complicate our analysis even more.  

                **How to deal with outliers?**  

                Dealing with outliers is not easy. I have seen many models online where people eliminate outliers in their data prepocessing steps. This could be the case, for example,
                if a professor is calculating grades. However, if one is dealing with sensitive information one would be making a mistake by eliminating the outliers from the analysis.
                When dealing with potential losses, profits, and health data one has to be extra careful with outliers because the magnitude of the consequences will be
                more than any benefit or insight that we could get from the data.  

                ''', style={"font-family":"Verdana"}, className = "container", highlight_config={"theme":"dark"}),
                html.H1("Histogram of Charges by Region", style = {"textAlign": "center", "font-family":"Verdana"}),
                dcc.Graph(figure = fig2)
                
            ], className = "container"),
        ],style = {"font-family": "Verdana"}),
        dcc.Tab(label = "Perfomance Metrics" , children = [
            html.H1("Linear Regression Metrics", style = {"textAlign": "center", "font-family":"Verdana"}),
            dcc.Dropdown(id='my-dropdown', 
            options=[{'label':'Age','value':'age'}, 
            {'label':'Sex','value':'sex'}, 
            {'label':'BMI','value':'bmi'}, 
            {'label':'Children','value':'children'},
            {'label':'Smoker','value':'smoker'},
            {'label':'Region','value':'region'}

            ], multi=True,value=['age'], 
            style={"display":"block", "margin-left":"auto", "margin-right":"auto", "width":"60%"}), 
            dcc.Graph(id="linear"), 
            dcc.Markdown(''' 
            ### Variables in this chart:  
            Age: age of the person  
            BMI: body mass index  
            Sex: female (0) or male (1)  
            Children: number of children  
            Smoker: smoker (1) or non-smoker (0)  
            Region: southwest (3), southeast (2), northwest (1), northeast (0)  

            ### Code to generate this chart

            ```py
            def update_graph(selected_dropdown):
        
                #dropdown = {'Age':'age', 'Sex':'sex', 'BMI':'bmi', 'Children':'children','Smoker':'smoker', 'Region':'region'}
                for i in selected_dropdown: 
                    if i == "age": 
                         dfx = df["age"]
                    elif i == "sex":
                        dfx = df["sex"]
                    elif i == "bmi":
                        dfx = df["bmi"]
                    elif i == "children":
                        dfx = df["children"]
                    elif i == "smoker":
                         dfx = df["smoker"]
                    else:
                        dfx = df["region"]
                    dfx = np.array(dfx) 
                    dfx = dfx.reshape(-1,1)
        
                    #results = evaluate_model(dfx, dataY, model)
                    #print("MAE (mean) and MAE (stdev): ", np.mean(results), np.std(results)) 
                    model = HuberRegressor() 
                    model.fit(dfx, df["charges"])
                    x_range = np.linspace(dfx.min(), dfx.max(), 100) 
                    y_range = model.predict(x_range.reshape(-1,1))
                    figure3 = px.scatter(data,x=df[f"{i}"], y=df["charges"])
                    figure3.add_traces(go.Scatter(x=x_range, y=y_range, name = "Regression Fit"))
                return figure3
            ```
            *Note: this code was inside the `@app.callback` function*  
            ''',style={"font-family":"Verdana"}, className = "container", highlight_config={"theme":"dark"}), 
            
            html.H1("Random Forest Model", style = {"textAlign": "center", "font-family":"Verdana"}), 
            dcc.Markdown('''
            ## What is a Random Forest Model?  
            >  
            > "Random Forests grow many classification trees. \[...] Each tree gives a classification, and we say the tree 'votes' for that class. The forest chooses
            the classification having the most votes (over all the trees in the forest)." - [Breiman and Cutler](https://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm)
            >  

            ## Code to generate the Random Forest Model:  
            ```py
            def get_models(): 
                models = dict() 
                #exploring ratios from 10% to 100% 
                for i in arange(0.1, 1.1, 0.1): 
                    key = "%.1f" % i 
                    #setting the max samples to none 
                    if i == 1.0: 
                        i = None 
                    models[key] = RandomForestRegressor(max_samples = i)
                return models 
            def evaluate_model(model, x, y): 
                #defining the evaluation procedure 
                cv = RepeatedKFold(n_splits = 10, n_repeats = 3, random_state = 1) 
                #scores = cross_val_score(model, dataX, dataY, scoring = "neg_mean_absolute_error", cv = cv, n_jobs = 1, error_score = "raise")
                scores = cross_val_score(model, dataX, dataY, scoring = "neg_mean_squared_error", cv = cv, n_jobs = 1, error_score = "raise")
                return np.absolute(scores) 
            ```
            ## Testing the models:
            ```py
            models = get_models()
            results, names = list(), list()

            for name, model in models.items():
                #evaluate the model
                scores = evaluate_model(model, dataX, dataY)
                #storing the results
                results.append(scores)
                names.append(name)
                #summarizing the performance
                #print("Mean MAE scores and STD", name, mean(scores), std(scores))
                print("RMSE scores and STD", name, mean(np.sqrt(scores)))

            ans = np.sqrt(results)
            #converting the ans variable to a list in order to plot it with the names list - otherwise it won't run
            ans = list(ans)
            plt.boxplot(ans, labels = names, showmeans = True)
            ```  
            For this model I decided to include two error metrics - RMSE (Root Mean Squared Error) and MAE (Mean Squared Error). RMSE tends to penalize bigger errors, 
            therefore when MAEs for a given problem tend to be the same, the RMSE could be a factor deciding which is the 'best' model - or at least the one that fits
            the problem.  

            In the above code, if you want to get the same results for the MAE:  
            >Don't use **'ans = np.sqrt(results)'**. Instead, uncomment the **'print("Mean MAE ...'** and use the **'results'** variable in the **'plt.boxplot(results, labels = names, showmeans = True)'** function.   

            Since we are dealing with insurance charges, I opted to include both error metrics and use the RMSE as the benchmark.  
            
            \*[File](https://raw.githubusercontent.com/arcelioeperez/dash-app/gh-pages/source/random_forest.py) that produced the model and the plots.\* 
            
            To run the above file and create a text file with the output, type:  
            ```
            python random_forest.py > random_forest.txt
            ```  
            
            These files contain the MAE (mean and standard deviation) and the RMSE from the random forest model:  
            [MAE-Random Forest](https://raw.githubusercontent.com/arcelioeperez/dash-app/gh-pages/source/random_forest_mae.txt)|[RMSE-Random Forest](https://raw.githubusercontent.com/arcelioeperez/dash-app/gh-pages/source/random_forest_rmse.txt)  
            ## MAE Plot  
            ![MAE Plot](https://github.com/arcelioeperez/dash-app/raw/gh-pages/demo/randomforest.PNG)
            ## RMSE Plot  
            ![RMSE Plot](https://github.com/arcelioeperez/dash-app/raw/gh-pages/demo/randomforestrmse0.PNG)
            ''', style={"font-family":"Verdana"}, className = "container", highlight_config={"theme":"dark"})   

     ])
 
    ],style = {"font-family": "Verdana"})
   

])

@app.callback(Output('linear', 'figure'), 
[Input('my-dropdown', 'value')])
def update_graph(selected_dropdown):
    
    #dropdown = {'Age':'age', 'Sex':'sex', 'BMI':'bmi', 'Children':'children','Smoker':'smoker', 'Region':'region'}
    for i in selected_dropdown: 
        if i == "age": 
            dfx = df["age"]
        elif i == "sex":
            dfx = df["sex"]
        elif i == "bmi":
            dfx = df["bmi"]
        elif i == "children":
            dfx = df["children"]
        elif i == "smoker":
            dfx = df["smoker"]
        else:
            dfx = df["region"]
        dfx = np.array(dfx) 
        dfx = dfx.reshape(-1,1)
        
        #results = evaluate_model(dfx, dataY, model)
        #print("MAE (mean) and MAE (stdev): ", np.mean(results), np.std(results)) 
        model = HuberRegressor() 
        model.fit(dfx, df["charges"])
        x_range = np.linspace(dfx.min(), dfx.max(), 100) 
        y_range = model.predict(x_range.reshape(-1,1))
        figure3 = px.scatter(data,x=df[f"{i}"], y=df["charges"])
        figure3.add_traces(go.Scatter(x=x_range, y=y_range, name = "Regression Fit"))
    return figure3

    
if __name__ == "__main__": 
    app.run_server(debug=False, host = "0.0.0.0",port = 80)

