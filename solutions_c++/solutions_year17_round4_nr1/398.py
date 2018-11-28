#include <iostream>
#include <sstream>
#include <climits>
#include <stdio.h>
#include <iomanip>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <string>
#include <gmpxx.h>

using namespace std;

int T;
int N;
int P;

void solve(int t) {
  int count = 0;
  cerr << "test " << t << endl;
  cin >> N;
  cin >> P;
  int a[4];
  for(int i=0; i<4; i++) {
    a[i] = 0;
  }
  for(int i=0; i<N; i++) {
    int G;
    cin >> G;
    a[G % P]++;
  }
  if(P == 2) {
    count+=a[0];
    count+=ceil((1.0*a[1])/2.0);
  }
  if(P == 3) {
    count+=a[0];
    count+=min(a[1], a[2]);
    count+=ceil(1.0*(max(a[1], a[2]) - min(a[1], a[2]))/3.0);
  }
  if(P == 4) {
    count+=a[0];
    count+=min(a[1], a[3]);
    count+=a[2]/2;
    int add = 0;
    if(a[2] % 2 == 1) {
      add = 2;
    }
    count+=ceil(1.0*(max(a[1], a[3]) + add - min(a[1], a[3]))/4.0);
  }
  cout << "Case #" << t << ": " << count << endl;
}

int main() {
  cin >> T;
  cout << setprecision(9);
  cerr << setprecision(9);
  for(int t=0; t<T; t++) {
    solve(t+1);
  }
}
