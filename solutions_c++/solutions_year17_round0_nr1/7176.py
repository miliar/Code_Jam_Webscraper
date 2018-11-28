#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<bitset>

using namespace std;
typedef bitset<1000> BITSET;

BITSET checker, swaper, new_q;
int s_length, answer, min_step;

int main () {
  BITSET question, current_q;
  string s;
  int k, t, happy, count, current_count;
  int start, end, one_index;
  bool zeroes = false;
  checker.flip();

  cin >> t;
  for (int i = 0 ; i < t ; i++) {
    cin >> s >> k;

    question.reset();
    question.flip();
    answer = -1;
    s_length = s.length();
    for (int j = s_length - 1 ; j >= 0 ; j--) {
      if (s[j] == '-') {
        question[s_length - 1 - j] = 0;
      }
    }
    answer = 100000;

    start = 0;
    count = 1;
    end = k - 1;
    happy = 0;

    while(end < s_length) {
      if (question[start] == 1) {
        start++;
        end++;
        continue;
      }
      current_q = question;
      current_count = 0;

      // test flip
      for (int j = start ; j < start + count ; j++) {
        if (current_q[j] == 1) continue;
        for (int ii = j ; ii < j + k ; ii++) {
          current_q.flip(ii);
        }
        current_count++;
      }

      zeroes = false;

      // cout << start << endl;
      // cout << end << endl;
      // cout << count << endl;
      // for (int ii = s_length - 1 ; ii >= 0 ; ii--) {
      //   cout << current_q[ii];
      // }


      // check zero
      for (int ii = start; ii <= end ; ii++) {
        if (current_q[ii] == 0) zeroes = true;
      }

      if (!zeroes) {
        happy += current_count;
        start = end + 1;
        end = end + k;
        count = 1;
        question = current_q;
      } else {
        count++;
        end++;
      }

    }
    
    if (question.size() - question.count() > 0) {
      cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << (i+1) << ": " << happy << endl;
    }
  }
  return 0;
}
