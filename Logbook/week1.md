## Week 1

I have met Shah, whose interest lies in machine learning domain.
We have discussed the project intentions listed below.

## Next Week

- Explore existing recommender systems (closed/open source) from the below URL
  - https://github.com/grahamjenson/list_of_recommender_systems
- Explore existing datasets and choose one you want to work with
  - Example: https://labrosa.ee.columbia.edu/millionsong/
- Report on the choice of technology

## Introduction

RECOMMENDARE system produces visualisation of choices that were considered to produce current recommendation and allows users to manipulate them to retrain system for new recommendations.

For example, if system recommending movies gave you recommendation of any five movies it needs to explain why those five movies were selected. Then, users will be able to interact with those choices to produce new set of recommendation.

Current proposal for visualisation will be in forms of bubbles, each bubble representing significant factor for the final recommendation. For example, if systems has recommended movie "Cinderella", the evidence will be portrayed as different sized bubbles representing most influential categories with the biggest ones being _Disney_ and _Princess_ and _Vintage_. These categories are extracted from the evidence used by recommender system. User can then change the size of the bubbles increasing or decreasing the emphasis of the target category, producing new recommendation. When operating category bubbles, categories can appear or disappear.

NOTE: The "bubble" approach is just a proposal and is a subject to change.

## Challenges

1. Understand current state-of-the-art recommendation approaches and analyse how the data is processed to produce final recommendation
2. Classify (supervised, probably not) or clusterise (unsupervised, probably yes) the data to create categories for recommendations
3. Implement visual system that can interact with the model

[Next](week5.md)
