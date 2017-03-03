#!/bin/bash
echo 'copy sample file'
cp text/sample.full text/sample.dat

echo 'participle.py'
python participle.py 
echo 'normalization.py' 
python normalization.py 
echo 'generate_feature_vector.py'
python generate_feature_vector.py 
echo 'cosine_categorize.py'
python cosine_categorize.py

echo 'success!'
