#include <bits/stdc++.h>

using namespace std;

const int MAXN = (1 << 10);

int d[MAXN];

void clear() {
  for(int i = 0 ; i < MAXN ; i++) {
    d[i] = -1;
  }
}

int getInitialState(string s, int n) {
  int initial_state = 0;
  for(int i = 0 ; i < n ; i++) {
    if(s[i] == '+') {
      initial_state |= (1 << i);
    }
  }
  return initial_state;
}

void f(int state, int n) {
  for(int i = 0 ; i < n ; i++) {
    if(state & (1 << i)) {
      cout << "1";
    } else {
      cout << "0";
    }
  }
  cout << endl;
}

int main(){
  int casos, n, k;
  string s;
  cin >> casos;
  for(int caso = 1 ; caso <= casos; caso++) {
    cin >> s >> k;
    int n = s.size();
    int target = (1 << n) - 1;
    clear();
    int initial_state = getInitialState(s, n);
    queue<int> states;
    states.push(initial_state);
    d[initial_state] = 0;
    while(!states.empty()) {
      int state = states.front();
      states.pop();
      int mask = (1 << k) - 1;
      for(int i = 0 ; i <= n-k ; i++) {
        int new_state = state ^ mask;
        if(d[new_state] == -1) {
          d[new_state] = d[state] + 1;
          states.push(new_state);
        }
        mask = mask << 1;
      }
    }
    if(d[target] == -1) {
      cout << "Case #" << caso << ": IMPOSSIBLE" << endl;
    } else { 
      cout << "Case #" << caso << ": " << d[target] << endl;
    }
  }
  return 0;
}