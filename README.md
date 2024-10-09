# Synthetic Data Generation Using LLM

This project generates synthetic customer reviews for smartphones using a language model. The generated reviews are designed to simulate realistic user feedback, highlighting features such as camera quality, battery life, and overall value for money. 

I generated Reviews as real like human review for smartphones 


## Task Questions/Answers

### Why was the model/architecture used?

I used Gemini 1.5 Flash, a language model that excels at natural language processing tasks, including text generation. You can use any LLM open model the reason why i am using this gemini have produces high-quality contextually relevant text also have benefits of Versatility, Quality and Coherence.

### What were the different factors considered for generating this dataset? (Length, topic diversity, etc.)?


- Length: Because you are generating reviews real like humans it typically ranges from 50 to 150 words.

- Realism: Fix vocabulary & linguistics as human text and make sure what kind of data you are generating from an LLM compares to the actual dataset for realism like authenticity, and users do some grammatical mistakes.

- Topic Diversity: this dataset covered multiple aspects of smartphone use, including camera quality, battery life, design, and value for money. this helps to diversify the different users.

- Uniqueness: Each review was generated to be unique to avoid redundancy, which enhances the dataset's quality and realism.

- Prompts Engineering: Provide clear and concise prompts to guide the LLM in generating the desired type of text.


### How do we measure the efficacy of a synthetic dataset?

- Realism: Ensure that the synthetic data mimics real human data, including occasional grammatical mistakes to add authenticity. Compare the generated data from an LLM to the actual dataset to check for realism and authenticity.

- Human Evaluation: Have domain experts assess the quality and realism of the synthetic data compared to real examples. Experts can provide insights into how believable and accurate the synthetic data appears.

- Distribution Comparison: Compare distributions of key features such as review lengths, word counts, and sentiment scores between the synthetic and real datasets. This helps ensure that the synthetic data mirrors the statistical properties of real data.

- A/B Testing: Conduct A/B tests by using synthetic data in place of or alongside real data. Compare the outcomes to evaluate how well the synthetic data performs in real-world scenarios or applications.

- Uniqueness Check: Use tools to detect duplicates and ensure that the generated data is sufficiently different from the source data. This prevents replication and promotes the originality of the synthetic dataset.

- Data Anonymization: Ensure that any personal information in the synthetic data is anonymized or synthesized in a way that it cannot be traced back to real individuals. This is crucial for privacy and compliance with data protection regulations.

### How do we ensure the synthetic dataset one generates is inspired from a source dataset but not an exact replica?

To Avoid creating exact replicas.  

You can use Data Augmentation Techniques:
- Word Replacement: Replace words with synonyms or semantically similar words.
- Back translation
- By adding random noise

Combine Multiple Datasets: Combine your source dataset with other relevant datasets to introduce new perspectives and variations.


### What were the top challenges in solving for this problem statement?

Top challenges are:

- Close to Realism: When generating data we have to give procise prompt to achieve the realism or human like data.

- Not having Expert: If you do not have any expert to check or compare the generated data, it will be difficult to Evalute.

- Controllable Generation:
    - Conditional Generation: Condition the generative model on specific attributes or styles to guide the generation process while maintaining diversity.
    
    - Style Transfer: Transfer the style of one dataset to another to create new, inspired variations.