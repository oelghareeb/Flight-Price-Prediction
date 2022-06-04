from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Departure
        # Afternoon = 0 (not in column)
        Departure=request.form['Departure']
        if(Departure=='Night'):
            d_Night = 1
            d_Evening = 0
            d_Morning = 0
            d_Early_Morning = 0
            d_Late_Night = 0

        elif(Departure=='Evening'):
            d_Night = 0
            d_Evening = 1
            d_Morning = 0
            d_Early_Morning = 0
            d_Late_Night = 0


        elif(Departure=='Morning'):
            d_Night = 0
            d_Evening = 0
            d_Morning = 1
            d_Early_Morning = 0
            d_Late_Night = 0

        elif(Departure=='Early_Morning'):
            d_Night = 0
            d_Evening = 0
            d_Morning = 0
            d_Early_Morning = 1
            d_Late_Night = 0


        elif(Departure=='Late_Night'):
            d_Night = 0
            d_Evening = 0
            d_Morning = 0
            d_Early_Morning = 0
            d_Late_Night = 1

        else:
            d_Night = 0
            d_Evening = 0
            d_Morning = 0
            d_Early_Morning = 0
            d_Late_Night = 0


        # Arrival
        # Afternoon = 0 (not in column)
        Arrival = request.form['Arrival']
        if (Arrival == 'Night'):
            a_Night = 1
            a_Evening = 0
            a_Morning = 0
            a_Early_Morning = 0
            a_Late_Night = 0

        elif (Arrival == 'Evening'):
            a_Night = 0
            a_Evening = 1
            a_Morning = 0
            a_Early_Morning = 0
            a_Late_Night = 0

        elif (Arrival == 'Morning'):
            a_Night = 0
            a_Evening = 0
            a_Morning = 1
            a_Early_Morning = 0
            a_Late_Night = 0

        elif (Arrival == 'Early_Morning'):
            a_Night = 0
            a_Evening = 0
            a_Morning = 0
            a_Early_Morning = 1
            a_Late_Night = 0

        elif (Arrival == 'Late_Night'):
            a_Night = 0
            a_Evening = 0
            a_Morning = 0
            a_Early_Morning = 0
            a_Late_Night = 1

        else:
            a_Night = 0
            a_Evening = 0
            a_Morning = 0
            a_Early_Morning = 0
            a_Late_Night = 0


        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Class
        Class = int(request.form['class'])

        # Days Left
        Days_left = int(request.form['days_left'])

        # Duration
        Duration = int(request.form["duration"])

        # Airline
        # AIRASIA = 0 (not in column)
        airline=request.form['airline']
        if (airline=='IndiGo'):
            IndiGo = 1
            Air_India = 0
            SpiceJet = 0
            Vistara = 0
            GO_FIRST = 0

        elif (airline=='Air_India'):
            IndiGo = 0
            Air_India = 1
            SpiceJet = 0
            Vistara = 0
            GO_FIRST = 0

        elif (airline=='SpiceJet'):
            IndiGo = 0
            Air_India = 0
            SpiceJet = 1
            Vistara = 0
            GO_FIRST = 0

        elif (airline=='GO_FIRST'):
            IndiGo = 0
            Air_India = 0
            SpiceJet = 0
            Vistara = 0
            GO_FIRST = 1

        elif (airline=='Vistara'):
            IndiGo = 0
            Air_India = 0
            SpiceJet = 0
            Vistara = 1
            GO_FIRST = 0

        else:
            IndiGo = 0
            Air_India = 0
            SpiceJet = 0
            Vistara = 0
            GO_FIRST = 0

        # print(Jet_Airways,
        #     IndiGo,
        #     Air_India,
        #     Multiple_carriers,
        #     SpiceJet,
        #     Vistara,
        #     GoAir,
        #     Multiple_carriers_Premium_economy,
        #     Jet_Airways_Business,
        #     Vistara_Premium_economy,
        #     Trujet)

        # Source
        # Banglore = 0 (not in column)
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Mumbai = 0
            s_Kolkata = 0
            s_Hyderabad = 0
            s_Chennai = 0

        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Mumbai = 0
            s_Kolkata = 1
            s_Hyderabad = 0
            s_Chennai = 0

        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Mumbai = 1
            s_Kolkata = 0
            s_Hyderabad = 0
            s_Chennai = 0

        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Mumbai = 0
            s_Kolkata = 0
            s_Hyderabad = 0
            s_Chennai = 1

        elif (Source == 'Hyderabad'):
            s_Delhi = 0
            s_Mumbai = 0
            s_Kolkata = 0
            s_Hyderabad = 1
            s_Chennai = 0

        else:
            s_Delhi = 0
            s_Mumbai = 0
            s_Kolkata = 0
            s_Hyderabad = 0
            s_Chennai = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai,
        #     s_Hyderabad,
        #     s_Bangalore)

        # Destination
        # Banglore = 0 (not in column)
        Source = request.form["Destination"]
        if (Source == 'Delhi'):
            d_Delhi = 1
            d_Mumbai = 0
            d_Kolkata = 0
            d_Hyderabad = 0
            d_Chennai = 0

        elif (Source == 'Kolkata'):
            d_Delhi = 0
            d_Mumbai = 0
            d_Kolkata = 1
            d_Hyderabad = 0
            d_Chennai = 0

        elif (Source == 'Mumbai'):
            d_Delhi = 0
            d_Mumbai = 1
            d_Kolkata = 0
            d_Hyderabad = 0
            d_Chennai = 0

        elif (Source == 'Chennai'):
            d_Delhi = 0
            d_Mumbai = 0
            d_Kolkata = 0
            d_Hyderabad = 0
            d_Chennai = 1

        elif (Source == 'Hyderabad'):
            d_Delhi = 0
            d_Mumbai = 0
            d_Kolkata = 0
            d_Hyderabad = 1
            d_Chennai = 0

        else:
            d_Delhi = 0
            d_Mumbai = 0
            d_Kolkata = 0
            d_Hyderabad = 0
            d_Chennai = 0

        # print(
        #     d_Mumbai,
        #     d_Delhi,
        #     d_Bangalore,
        #     d_Hyderabad,
        #     d_Kolkata,
        #     d_Chennai
        # )
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']
        
        prediction=model.predict([[
            Total_stops,
            Class,
            Duration,
            Days_left,
            a_Night,
            a_Evening,
            a_Morning,
            a_Early_Morning,
            a_Late_Night,
            d_Night,
            d_Evening,
            d_Morning,
            d_Early_Morning,
            d_Late_Night,
            GO_FIRST,
            Air_India,
            IndiGo,
            SpiceJet,
            Vistara,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            s_Chennai,
            s_Hyderabad,
            d_Delhi,
            d_Mumbai,
            d_Kolkata,
            d_Hyderabad,
            d_Chennai
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
