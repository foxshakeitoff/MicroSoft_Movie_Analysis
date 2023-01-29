# Overview
![pic](images/The_Gallow.jpg) from upsplash.com
Film industry is big. And some films have big box offices, such as Avatar. Some films may not seems big but with small investment, yielded significant profits comparing to investment, like The Gallows. There are many factors can affect investment outcomes, such as politics, time of year, economy. More in films themselfs, there are *factors* like **Budget, Director/Actor, Genre**. 

# Business Understanding
Microsoft wants to invest in film industry. Here I use **Return on Investment**(or ROI) as measurment to determine if the film is worth to invest. **Budget, Director/Actor, Genre** were investigated here to see how different value of them can affect ROI. At end of the project, recommendations are provided on how to choose between these 3 selections in order to yield high **ROI**. However, these recommendations are just recommendations, final decisions have to be made based on real situation. 

# Data Understanding
There are 5 *csv files*(including tsv files) and 1 *sqlite database*. 

*movie_budgets.csv* contains information about **budgets** and **worldwide_gross**, which were used to calculate **ROI**. 

In sqlite3 database, there are four tables *movie_basics*,*movie_akas*,*persons*,*principals*. These tables contains information about directors, actors, actresses, including their name. Also movie titles have primary titles, original title and aka titles, which are used to connected to *movie_budgets.csv*, so we can get the ROI for each **category(directors, actors, actresses)**. At mean time, we also can get the ROI for each **genres**.

# Data Preparation
## Table previews
table **previews** are showned below to give a brief peep into datas that will be worked on.

# Exploratory Data Analysis
### Budgets
1. Most films have ROI below 50. 

2. When **budget** is *between* 10K to 1M, films have *higher* chance to achieve higher ROI, especially when budget are *between* 100K to 1M.

3. There are many films that has **budget** *between* 1M to 10M, but they can't achieve ROI more than 100. Then budgets *higher* than 10M lead to *much lower* ROI overall.

4. There are few films that has **budget** *between* 1K to 10K, but ROI in this **budget** range can be very high or low, means having big variance. 

My **recommendation** is to have **budget** set *between* 100K to 200K to have better chance to have high return on investment. 
### Director/Actor
These show *top 20* **actors, directors, actresses** from above graphs. However this result is strongly *correlated* the specific **films** they are in. As top 1 and top 2 in each category, Reese Mishler, Cassiidy Gifford, Travis Cluff, Chris Lofing, Pfeifer Brown, and Ryan Shoos all are part of in *same* film. 

I recommend pick top 10 personas from each category, since these persons have significant higher ROI than rest of person.
### Genre
1. *'Adventure, Animation, Comedy', 'Action, Adventrue, Sci-Fi','Action, Adventure, Fantasy'* are there **genres** that generates *most* **ROI** comparing to other **genres** or genres conbinations. 

2. However overall each **genres** tends to have smilar **ROI** based on median comparison.

3. *Drama* has many *high* **ROI** films, however it could be the results of *high records volumns*. And majority of dramas films have *negative* **ROI**. 

4. *Comedy* and *Documentary* have many films that has *high* **ROI**. 

I would *recommend* setting genre as adventure and action or comedy, since films yeild high **ROI** are in these genre or commbination of these genres. 
# Results
## Recommendation 
This Analysis generates 3 recommendations:
1. Have **budget** set *between* 100K to 200K to have better chance to have high return on investment. 
2. Pick top 10 personas from each category such as Reese Mishler, Cassiidy Gifford, Travis Cluff, Chris Lofing, Pfeifer Brown, and Ryan Shoos, since these persons have significant higher **ROI** than rest of person.
3. Set genre as adventure and action or comedy, since films yeild high **ROI** are in these genre or commbination of these genres.
## More
There are some more related finds:
1. Another *measurement* here can be films **rating**, while it would provide perspective about how people like the film, ratings might not give as many insights about profit as **ROI** does.  

2. There are many **Generes** that doesn't have many records. However for those not-well-produced **generes** have some films that yield high ROI. This films can be investigated further and out of this project's scope.

3. The impact of persons on films'ROI are so correlated to films themselves. If there a group of person are in same film and that film has high **ROI** then those person all have high **ROI**. So alternatively, we can investigate **ROI** for each **title**, and then choose person from top 10 films that have highest ROI. 

4. Avatar has big box office, however it's budget is so high that makes it not high in ROI.


# More Informations
Link of my jupyternotebook, presentation.pdf
## Repository Structure
```
├── data
├── images
├── README.md
├── Presentation.pdf
└── Notebook.ipynb
```

