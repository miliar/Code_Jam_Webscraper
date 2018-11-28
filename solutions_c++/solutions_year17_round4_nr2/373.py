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
int C;
int M;
int pb[1000*1000];

void solve(int t) {
  cerr << "test " << t << endl;
  cin >> N;
  cin >> C;
  cin >> M;
  int p;
  int b;
  for(int i=0; i<1000*1000; i++) {
    pb[i] = 0;
  }
  for(int i=0; i<M; i++) {
    cin >> p;
    cin >> b;
    p--;
    b--;
    pb[p*1000 + b]++;
  }
  int rides = 0;
  for(int cust=0; cust<1000; cust++) {
    int cust_ride = 0;
    for(int pos=0; pos<1000; pos++) {
      cust_ride += pb[pos*1000 + cust];
    }
    rides = max(rides, cust_ride);
  }
  int promos = 0;
  while(rides<1000*1000) {
    int carry = 0;
    for(int ride=1000-1; ride>=0; ride--) {
      int riders = 0;
      for(int cust=0; cust<1000; cust++) {
        riders += pb[ride*1000 + cust];
      }
      carry = max(0, riders - rides + carry);
    }
    if(carry > 0) {
      rides++;
      continue;
    }
    else {
      for(int pos=0; pos<1000; pos++) {
        int s = 0;
        for(int cust=0; cust<1000; cust++) {
          s += pb[pos * 1000 + cust];
        }
        /*if(s != 0) {
          cerr << "sum " << pos << ": " << s << endl;
          }*/
        if(s > rides) {
          promos += (s - rides);
        }
      }
      break;
    }
  }
  cout << "Case #" << t << ": " << rides << " " << promos << endl;
}

int main() {
  cin >> T;
  cout << setprecision(9);
  cerr << setprecision(9);
  for(int t=0; t<T; t++) {
    solve(t+1);
  }
}
