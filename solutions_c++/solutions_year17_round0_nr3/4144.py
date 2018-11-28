#include <iostream>
#include <sstream>
#include <climits>
#include <stdio.h>
#include <iomanip>
#include <list>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <string>
#include <gmpxx.h>

using namespace std;

int T;

int extract_max(const map<int, int> &m) {
  int a = 0;
  for(pair<int, int> b : m) {
    a = max(a, b.first);
  }
  return a;
}

void upsert(map<int, int>& m, int len, int count) {
  int current = 0;
  if(m.find(len) != m.end()) {
    current = m[len];
  }
  m[len] = current + count;
}

int iterate(map<int, int> &m, int N) {
  //cerr << "iterate " << N << endl;
  int a = extract_max(m);
  //cerr << "max: " << a << endl;
  int count = m[a];
  if(a == 0) {
    return 0;
  }
  if(count > N) {
    return a;
  }
  int b;
  int c;
  if(a%2 == 0) {
    b = a/2 - 1;
    c = a/2;
  }
  else {
    b = (a-1)/2;
    c = (a-1)/2;
  }
  //cerr << "upsert " << b << " " << count << endl;
  upsert(m, b, count);
  //cerr << "upsert " << c << " " << count << endl;
  upsert(m, c, count);
  m.erase(a);
  return iterate(m, N-count);
}

void solve(int t) {
  int N;
  int K;
  cin >> N;
  cin >> K;
  map<int ,int> m;
  m[N] = 1;
  int r = iterate(m, K-1);
  //cerr << "r: " << r << endl;
  int a;
  int b;
  if(r%2 == 0) {
    a = r/2;
    b = r/2 - 1;
  }
  else {
    a = (r-1)/2;
    b = (r-1)/2;
  }
  cout << "Case #" << t << ": " << a << " " << b << endl;
}

int main() {
  cin >> T;
  for(int t=0; t<T; t++) {
    solve(t+1);
  }
}
