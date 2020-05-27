from flask import Flask, jsonify, render_template, request
from collections import defaultdict
import sys

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    result = ''
    if request.method == 'POST' and 'statement' in request.form:
        statement=request.form.get('statement')
        result = smallestSubString(statement)
    return render_template("index.html", result=result)


def smallestSubString(S):
    distinct_count = len(set(list(S)))
    n = len(S)
    freq = defaultdict(int)
    start_idx = 0
    min_len = sys.maxsize
    distinct_till_here = 0
    for j in range(n):
        freq[S[j]] += 1
        if freq[S[j]] == 1:
            distinct_till_here += 1

        if distinct_count == distinct_till_here:
            while freq[S[start_idx]] > 1:
                if freq[S[start_idx]] > 1:
                    freq[S[start_idx]] -= 1
                start_idx += 1

            curr_len = j - start_idx + 1
            min_len = min(min_len, curr_len)
    return min_len

if __name__ == '__main__':
    app.run(debug=True)
