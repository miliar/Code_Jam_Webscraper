#include <iostream>
#include <vector>
#include <string>
using namespace std;

int isValid(string s) {
  for (int i = 1; i < s.size(); i++) {
    if (s[i] < s[i - 1]) return 0;
  }
  return 1;
}

int main() {

  int n;
  scanf("%d", &n);

  for (int i = 1; i <= n; i++) {
    char s[32];
    scanf("%s", s);

    char s2[32];
    strcpy(s2, s);

    int f = -1;
    for (int j = 1; j < strlen(s); j++) {
      if (s[j] < s[j - 1]) {
        f = j;
        break;
      } 
    }

    if (f == -1) {
      printf("Case #%d: %s\n", i, s);
      continue;
    }

    for (int j = f; j < strlen(s); j++) {
      s[j] = '9';
    }

    f--;
    while (f >= 0) {
      int mora = 0;
      if (s[f] <= '1') {
        s[f] = '9';
        if (f == 0) {
          s[f] = '0';
        }
        mora = 1;
      } else {
        s[f]--;
      }
      if (f > 0) {
        if (s[f - 1] > s[f] || mora) {
          s[f] = '9';
          f--;
        } else {
          break;
        }
      } else {
        break;
      }
    }

    if (s[0] == '0') {
      strcpy(s, s + 1);
    }
 
    printf("Case #%d: %s\n", i, s);

    
    /*int t = stoi(s2);
    while (1) {
      char cc[32];
      sprintf(cc, "%d", t);
      if (isValid(cc)) {
        cout << t << endl;
        break;
      } else {
        t--;
      }
    }*/
  }

  return 0;
}
