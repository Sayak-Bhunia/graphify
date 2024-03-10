import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def main():
    st.title("Plot your graph with Graphify")
    st.subheader('Solve your graph-based assignments with ease')

    # Input fields for x and y values
    x_values = st.text_input("Enter x values (separated by comma):")
    y_values = st.text_input("Enter y values (separated by comma):")

    # Convert input strings to lists of floats
    x_values_list = [float(x.strip()) for x in x_values.split(',')] if x_values else []
    y_values_list = [float(y.strip()) for y in y_values.split(',')] if y_values else []

    if x_values_list and y_values_list:
        data = {'X axis': x_values_list, 'Y axis': y_values_list}
        df = pd.DataFrame(data) #dataframe a streamlit component
        st.write(df)

    if st.button("Plot Graph"):
        try:
            # Plot the graph using Plotly / can also use mayplotlib but for some reason it is giving error while hosting it on streamlit
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_values_list, y=y_values_list, line=dict(color='#7c3aed', width=2), mode='lines+markers', name='Data Points'))
            fig.update_layout(title='Your Graph', xaxis_title='X axis', yaxis_title='Y axis')
            st.plotly_chart(fig)

        except ValueError:
            st.error("Please enter valid numerical values.")

if __name__ == "__main__":
    main()
