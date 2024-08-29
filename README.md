### Privacy Stories v0.2.7



#### To create graphs based on annotated privacy policies that display connections of actions, data types and purposes -> 
graphs_stories/graphs.ipynb 


#### To create privacy stories 
upload a privacy policy file to the input folder and use story_prompting1.ipynb
output -> output/{app_id}_privacy_stories.xlsx 
or leave output file blank to have all sent to privacy_stories_1_1.xlsx


#### To annotate/answer questions about output privacy stories
Use annotator/processor.ipynb to load an excel file for annotation and modify the questions accordingly. 
navigate to the annotator directory and run

```python main.py```

Open the link provided in terminal.

Note: this relies on the llm outputting stories in the proper format of 1. {story}, 2. {story} , etc...

#### To view annotated policies 
policies_annotated/annotated_policies/{app_id} 


