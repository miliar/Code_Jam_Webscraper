//Esteban Foronda Sierra
using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r;}

#define D(x) cout << #x " is " << x << endl
#define ll long long

void convert(string &x, int start) {
  for(int i = start + 1; i < x.size(); ++i) x[i] = '9';
  x[start]--;
  for(int i = start; i >= 1 && x[i] < x[i - 1]; --i) {
    x[i] = '9';
    x[i - 1]--;
  }
}

int main() {
  int t;
  cin >> t;
  for(int x = 0; x < t; ++x) {
    string n;
    cin >> n;
    for(int i = 0; i < n.size() - 1; ++i) {
      if(n[i] > n[i + 1]) convert(n, i);
    }
    printf("Case #%d: ", x + 1);
    bool leading = true, first = true;
    for(int i = 0; i < n.size(); ++i) {
      if(n[i] != '0') leading = false;
      if(!leading) cout << n[i];
    }
    cout << endl;
  }
}
