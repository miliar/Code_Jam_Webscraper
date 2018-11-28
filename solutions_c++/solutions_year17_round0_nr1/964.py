#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

char flip[256];

void init() {
  flip['+'] = '-';
  flip['-'] = '+';
}

void solve() {
  string s;
  int K;
  cin >> s >> K;
  int n = 0;

  // find the first '-'
  int i = 0;
  while (i < s.size() && s[i] == '+')
    i++;

  if (i >= s.size()) {
    cout << 0 << endl;
    return;
  }

  do {
    if (i + K <= s.size()) {
      for (int j = i; j < i+K; j++)
	s[j] = flip[s[j]];
    } else {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
    n++;
    while (i < s.size() && s[i] == '+')
      i++;
  } while (i < s.size());

  cout << n << endl;
}
       
int main(){
  int T;
  cin >> T; 
  string s; getline(cin,s); 

  init();
  for (int i = 0; i < T; i++) {
    cout << "Case #" << i+1 << ": ";
    solve();
  }
  return 0;
}


