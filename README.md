# jumble-word-noob
## Noob Implementation of Jumble Word against a small English Dictionary
### How to Use ?
First argument is a **jumbled word** and the rest arguments are already seen words of the given jumbled word.
<br>**Example is shown below:**

```bash
$ python3 jumble_word.py lbemju
jumble
Time Elapsed: 5.1797566413879395 seconds

$ python3 jumble_word.py rboe
boer
Time Elapsed: 0.041929006576538086 seconds

$ python3 jumble_word.py rboe boer
bore
Time Elapsed: 0.04587697982788086 seconds

$ python3 jumble_word.py rboe boer bore
ebro
Time Elapsed: 0.16556215286254883 seconds

$ python3 jumble_word.py rboe boer bore ebro
robe
Time Elapsed: 0.343045711517334 seconds

$ python3 jumble_word.py rboe boer bore ebro robe
sorry..not found
Time Elapsed: 0.5118098258972168 seconds
```
