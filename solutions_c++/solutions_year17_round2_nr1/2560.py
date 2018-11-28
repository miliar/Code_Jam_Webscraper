//
//  main.cpp
//  1
//
//  Created by Ken-Hao Liu on 22/04/2017.
//  Copyright © 2017 Ken-Hao Liu. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#define forn(i,n) for(int i=0;i<n;i++)
#define fillv(v,a) fill(v.begin(),v.end(),a)
typedef long long ll;
typedef std::vector<int> vi;

using namespace std;

class Solution{
public:
  void solve(int t){
    
  }
};

int main(int argc, const char * argv[]) {
  int t,N,D;
  double k,s,time;
  cin>>t;
//  Solution sol;
  forn(i,t){
    time=0;
    cin>>D>>N;
    forn(j,N){
      cin>>k>>s;
      time=max((double)(D-k)/s,time);
    }
    printf("Case #%d: %.6f\n",i+1,(double)D/time);
//    sol.solve(i+1);
  }
}
