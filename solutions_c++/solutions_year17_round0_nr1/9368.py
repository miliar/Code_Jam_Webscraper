#include <iostream>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <cstdlib>
#include <cassert>

using namespace std;
int maxi = 0;
map <string, int> V;
map<string, vector<string> > G;
string flip(string& s, int i, int k) {
  //cout << s << " -> ";
  for(int j=0;j<k;j++) {
    s[i+j] = (s[i+j] == '-') ? '+' : '-';
  }
  //cout << s << endl;
  return s;
}

string perfect (int n) {
  string s;
  for(int i=0;i<n;i++) {
    s += '+';
  }
  return s;
}

int test_right(string arr, int k) {
  int n = arr.length();
  string perf = perfect(n);
  int changes = 0;
  while(changes<n) {
    if(arr == perf) {
      break;
    }
    int i;
    for(i=0;i<n;i++) {
      if(arr[i] == '-') {
        break;
      }
    }
    assert(i<n);
    if(i>=n-k+1) {
      //cout << "right:" << arr << endl;
      break;
    }
    flip(arr, i, k);
    changes++;
  }
  if(arr == perf) {
    return changes;
  }
  else {
    return -1;
  }
}

int test_left(string arr, int k) {
  int n = arr.length();
  string perf = perfect(n);
  int changes = 0;
  while(changes<n) {
    if(arr == perf) {
      break;
    }
    int i;
    for(i=n-1;i>=0;i--) {
      if(arr[i] == '-') {
        break;
      }
    }
    assert(i>=0);
    if(i<k-1) {
      break;
    }
    flip(arr, i-k+1, k);
    changes++;
  }
  if(arr == perf) {
    return changes;
  }
  else {
    return -1;
  }
}

void solveCase(ostream& out, int t) {
  string arr;
  int k;
  cin >> arr >> k;
  string arr_copy = arr;
  int left = test_left(arr, k);
  //cout << "now right: " << endl;
  int right = test_right(arr_copy, k);
  int result;
  if(left == -1) {
    result = right;
  }
  else if(right == -1) {
    result = left;
  }
  else {
    result = min(left, right);
  }
  if(result == -1) {
    out << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
  }
  else {
    out << "Case #" << t << ": " << result << endl;
  }
}

int main() {
  int T;
  cin >> T;
  for(int t=1;t<=T;t++) {
    solveCase(cout, t);
  }
  return 0;
}

string perfectZ (int n) {
  string s;
  for(int i=0;i<n;i++) {
    s += '+';
  }
  return s;
}

string flipZ(string s, int i, int k) {
  for(int j=0;j<k;j++) {
    s[i+j] = (s[i+j] == '-') ? '+' : '-';
  }
  return s;
}

void recurse(string& s, int i, int n, int k) {
  if(i==n) {
    for(int j=0;j<=n-k;j++) {
      string flipped = flip(s, j, k);
      G[s].push_back(flipped);
    }
    return;
  }
  s[i] = '-';
  recurse(s, i+1, n, k);
  s[i] = '+';
  recurse(s, i+1, n, k);
}

void construct(int n, int k) {
  string s;
  for(int i=0;i<n;i++) {
    s += '-';
  }
  recurse(s, 0, n, k);
}

int testZ(string arr, int k) {
  G.clear();
  V.clear();
  int n = arr.length();
  construct(n, k);
  queue<pair<string,int> > Q;
  Q.push(make_pair(arr, 0));
  string perf = perfect(n);
  int m = -1;
  while(!Q.empty()) {
    pair<string,int> x = Q.front();
    Q.pop();
    string xs = x.first;
    int xi = x.second;
    if(xs == perf) {
      m = xi;
      break;
    }
    V[xs] = 1;
    for(int i=0;i<G[xs].size();i++) {
      if(!V[G[xs][i]]) {
        Q.push(make_pair(G[xs][i], xi+1));
      }
    }
  }
  return m;
}


void solveCaseZ(ostream& out, int t) {
  string arr;
  int k;
  cin >> arr >> k;
  int result = testZ(arr, k);
  if(result == -1) {
    out << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
  }
  else {
    out << "Case #" << t << ": " << result << endl;
  }
}

int mainZ() {
  int T;
  cin >> T;
  for(int t=1;t<=T;t++) {
    solveCase(cout, t);
  }
  return 0;
}