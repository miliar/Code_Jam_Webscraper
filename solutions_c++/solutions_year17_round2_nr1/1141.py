#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long ll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(i,c)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

//#include "cout11.h"
typedef long double Double;


Double solve(ll D, vector<pair<ll,int> >& KS) {
    int N = KS.size();
    sort(all(KS)); // reverse(all(KS));
    // cout << KS << endl;

    Double maxt = 0.0;
    for (int i=N-1; i>=0; --i) {
        ll k = KS[i].first;
        int s = KS[i].second;
        Double r = (Double)(D - k);
        Double t = r / s;
        maxt = max(maxt, t);
    }
    return (Double)D / maxt;
    // return 0;
}

int main(){
  int _T; cin>>_T; // 1-100
  rep(_t,_T){
    ll D; int N; cin >> D >> N;
    vector<pair<ll,int> > KS;
    rep(i, N) { // 1000
        ll k; int s; cin >> k >> s;
        KS.push_back(make_pair(k, s));
    }
    Double ans = solve(D, KS);

 answer:
    printf("Case #%d: %.6Lf\n", 1+_t, ans);
  }
}
