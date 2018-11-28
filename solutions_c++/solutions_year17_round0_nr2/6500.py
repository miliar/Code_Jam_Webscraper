#include <bits/stdc++.h>
using namespace std;

void solve(int Case) {
  string s;
  cin >> s;
  int nine = s.length();
  for (int i=s.length()-1;i>=1;i--) {
    int current = int(s[i]-'0');
    int next = int(s[i-1]-'0');
    if (next > current) {
      nine = i;
      s[i-1]--;
    }
  }
  // cout << nine << "\n";
  // cout << s << "\n";
  cout << "Case #" << Case <<": ";
  for (int i=0;i<s.length();i++) {
    if (i >= nine)
      printf("9");
    else if (s[i] == '0')
      continue;
    else {
      if (s[i] < '0') {
        printf("REALLY\n");
      }
      printf("%c", s[i]);
    }
  }
  printf("\n");
}

int main () {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);

  int T;
  cin >> T;
  for (int i=0;i<T;i++) solve(i+1);
}