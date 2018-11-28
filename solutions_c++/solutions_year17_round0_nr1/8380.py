#include <iostream>
#include <string>
using namespace std;

char inv(char ch) {
  if (ch == '+')
    return '-';
  return '+';
}
struct sol {
  bool solved;
  int level;
};

bool checkvalid(string &s) {
  bool good = true;
  for(int i = 0; i < s.length(); i++) {
    if (s[i] == '-') {
      good = false;
      break;
    }
  }
  return good;
}

sol flip(string s, int k, int flip_index,  sol sl) {
  int strlen = s.length();   
  if (checkvalid(s)) {
    sl.solved = true;
    return sl;
  }

  // flip pancakes
  if (flip_index != -1) {
    sl.level++;
    for(int i = flip_index; i < (flip_index + k); i++)
      s[i] = inv(s[i]);
    if (checkvalid(s)) {
      sl.solved = true;
      return sl;
    }
  }
  sol groupsl = {false, sl.level};
  for(int i = (flip_index + 1);(i <= (strlen - k)); i++) {
    sol subsl = flip(s, k, i, sl);
    if (i == (flip_index + 1)) {
      groupsl.level = subsl.level;
      groupsl.solved = subsl.solved;
    }
    else if (subsl.solved && !groupsl.solved){
      groupsl.level = subsl.level;
      groupsl.solved = subsl.solved;
    }
    else if (subsl.solved &&
	     groupsl.solved &&
	     subsl.level < groupsl.level)
      groupsl.level = subsl.level;
  }

  return groupsl;
}


int main() {
  int TC;
  string inputstr, kstr;
  int k;
  scanf("%d\n",&TC); // number of test cases
  for (int tc = 1; tc <= TC; tc++) {
    getline(cin, inputstr,' ');
    getline(cin, kstr); 
    k = stoi(kstr);
    sol sl = {false, 0};
    sol finalsl = flip(inputstr, k, -1, sl);
    string output = "Case #"+ to_string(tc) + ": ";
    output += (finalsl.solved) ? (to_string(finalsl.level)) : "IMPOSSIBLE";
    cout << output;
    if(tc != TC)
      cout << endl;
  }
  return 0;
}
