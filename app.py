from flask import Flask, render_template, request
import pandas as pd
import urllib

app = Flask(__name__)

# Veri setini yükle
df = pd.read_csv('movie_id_titles.csv')

def get_imdb_link(movie_name):
    base_url = "https://www.imdb.com/find"
    params = urllib.parse.urlencode({'q': movie_name})
    imdb_link = base_url + "?" + params
    return imdb_link

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        film_adi = request.form['film_adi']
        matched_films = df[df['Name'].str.contains(film_adi, case=False)]
        if not matched_films.empty:
            film_row = matched_films.iloc[0]
            film_genre = film_row['Genre']

            similar_films = df[df['Genre'] == film_genre]
            similar_films = similar_films[similar_films['Name'] != film_row['Name']]
            recommendations = similar_films.head(7).to_dict('records')

            for film in recommendations:
                film["IMDBLink"] = get_imdb_link(film["Name"])

            return render_template('index.html', recommendations=recommendations)
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
