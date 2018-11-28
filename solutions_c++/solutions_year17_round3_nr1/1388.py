#include <iostream>
#include <stdio.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

#define r first
#define h second


int n, k;
vector<pair<double,double>>v;

double inf=1e14;
double pi=acos(-1);

double side(int i){return 2*pi* v[i].r * v[i].h; }
double surface(int i){return pi * v[i].r * v[i].r;}


double dp[1007][1007];
bool visited[1007][1007];

double solve(int index, int rem){
  if(rem==0) return 0;
  if(index==n) return -inf;
  if(visited[index][rem]) return dp[index][rem];
  visited[index][rem]=1;

  return dp[index][rem] = max(solve(index+1, rem), (rem==k)*surface(index) + side(index) + solve(index+1, rem-1));
}

int main() {
  cout<<fixed<<setprecision(9);
  int T; cin>>T;
  for(int t=1; t<=T; t++) {
    for(int i=0; i<1007; i++) for(int j=0; j<1007; j++) visited[i][j]=0;
    cin>>n>>k;
    v.resize(n);
    for(int i=0; i<n; i++) cin>>v[i].r>>v[i].h;
    sort(v.rbegin(), v.rend());
    cout<<"Case #"<<t<<": "<<solve(0,k)<<endl;
  }
}
