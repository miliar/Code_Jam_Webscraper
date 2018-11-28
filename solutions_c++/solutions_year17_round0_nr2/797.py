#include <iostream>
using namespace std;
int T;
string s;

void doit() {
  if (s.size() == 1) {
    printf("%c\n", s[0]);
    return;
  }
  for (int i = 0; i < s.size() - 1; ++i) {
    if (s[i] > s[i + 1]) {
      s[i] -= 1;
      for (int j = i + 1; j < s.size(); ++j) s[j] = '9';
      while (i > 0) {
	if (s[i] < s[i - 1]) {
	  s[i - 1] -= 1;
	  s[i] = '9';
	  --i;
	} else break;
      }
      if (s[0] != '0') printf("%c", s[0]);
      for (int j = 1; j < s.size(); ++j) printf("%c", s[j]);
      printf("\n");
      return;
    }
  }
  for (int i = 0; i < s.size(); ++i) printf("%c", s[i]);
  printf("\n");
  return;  
}

int main() {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> s;
    printf("Case #%d: ", t);
    doit();
  }
  return 0;
}
