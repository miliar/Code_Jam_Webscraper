#include "bits/stdc++.h"

using namespace std;

using dd = double;
using VD = vector<dd>;
using VVD = vector<VD>;
using PL = pair<long long, long long>;
using VP = vector<PL>;

#define PI (acos(-1.0))

VP res;

#define maxx 1100

bool cmp(PL a, PL b) {
  if(a.first == b.first) {
    return a.second > b.second;
  }
  return a.first > b.first;
}

double rec(int cur,int rem, VVD &dp) {
  // cout<<cur<<" "<<rem<<" \n";
  if(rem==0) return 0;
  if(cur == ((int)res.size())) return 0.0;

  dd &ret = dp[cur][rem];
  if(ret > (-0.5)) return ret;
  
  ret = rec(cur+1, rem, dp);

  ret = max(ret, rec(cur+1, rem-1, dp) + 2.0*PI*res[cur].first*res[cur].second);

  return ret;
}

int main(int argc, char const *argv[])
{
  freopen("AS.in", "r",stdin);
  freopen("AS.out", "w", stdout);
  int tcase,cas=1;
  cin>>tcase;

  // res.push_back({2,3});
  // res.push_back({2,10});

  // sort(res.begin(), res.end(), cmp);

  // cout<<res[0].second;

  while(tcase--) {
    int n,k;
    cin>>n>>k;
    res = VP(n);
    for(auto &p: res) {
      cin>>p.first>>p.second;
    }

    sort(res.begin(), res.end(), cmp);
    
    VVD dp(n+1, VD(n+1, -1));
    dd sol = 0;
    for(int i = 0 ; i<n ; i++) {
      // cout<<res[i].first<<" -- "<<res[i].second<<endl;
      if(k<=(n-i)) {
        sol = max(sol, rec(i+1, k-1, dp)+ PI*res[i].first*res[i].first + 2.0*PI*res[i].first*res[i].second);
        // cout<<sol<<endl;
      }
    }

    // cout<<cout.fix<<sol<<endl;
    printf("Case #%d: %.10lf\n",cas++, sol);
  }
  return 0;
}