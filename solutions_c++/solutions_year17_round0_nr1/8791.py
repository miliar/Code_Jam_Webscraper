#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <fstream>
#include <queue>
#include <sstream>
#include <unordered_map>
using namespace std;

queue<string> qp;
unordered_map<string, pair<int, int> > states;

int generatePossibilities(string p, int k, int stateMove) {
  for(int i = 0; i < p.length() - (k - 1); i++) {
    for(int j = 0; j < k; j++) {
      if(p[i + j] == '-') {
        p[i + j] = '+';
      } else {
        p[i + j] = '-';
      }
    }

    if(states.find(p) == states.end()) {
      states[p] = make_pair(0, stateMove);
      qp.push(p);
    }

    for(int j = 0; j < k; j++) {
      if(p[i + j] == '-') {
        p[i + j] = '+';
      } else {
        p[i + j] = '-';
      }
    }
  }
  return 0;
}

int clearQ(queue<string> &q) {
  queue<string> empty;
  swap(q, empty);
  return 0;
}

bool checkState(string p) {
  for(int i = 0; i < p.length(); i++) {
    if(p[i] != '+') {
      return false;
    }
  }

  return true;
}

int main() {
  ifstream in("A-small.in");
  streambuf *cinbuf = cin.rdbuf();
  cin.rdbuf(in.rdbuf());

  ofstream out("A-small.out");
  streambuf *coutbuf = cout.rdbuf(); //save old buf
  cout.rdbuf(out.rdbuf());

  int t, k, move;
  string p, cp;
  bool possible;

  cin >> t;
  for(int i = 1; i <= t; i++) {
    cin >> p >> k;
    states[p] = make_pair(0, 0);
    qp.push(p);
    possible = false;
    while(!qp.empty()) {
      cp = qp.front();
      qp.pop();
      if(states.find(cp) != states.end() && states[cp].first == 0) {
        states[cp].first = 1;
        if(checkState(cp)) {
          possible = true;
          break;
        }

        generatePossibilities(cp, k, states[cp].second + 1);
      }
    }

    cout << "Case #" << i << ": ";
    if(possible) {
      cout << states[cp].second << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }

    states.clear();
    clearQ(qp);
  }

  return 0;
}
