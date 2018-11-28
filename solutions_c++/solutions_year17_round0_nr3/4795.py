//Author: Andres-Felipe Ortega-Montoya
//C.cpp
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> ii;

const int INF = 1 << 30;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll TC;
  cin >> TC;
  priority_queue<int> q1;
  for(int t = 1; t <= TC; ++t){
    ll n,k;
    priority_queue<tuple<ll, ll, ll> > q;
    cin >> n >> k;
    q.push(make_tuple(n,0,n+1));
    ll l = 0;
    ll r = n;
    for(int i = 0; i < k;++i){
      ll a = get<1>(q.top());
      ll b = get<2>(q.top());
      q.pop();
      ll mid = (a+b)/2;
      l = mid-a;
      r = b-mid;
      //cout << mid << "a\n";
      q.push(make_tuple(l,a, mid));
      q.push(make_tuple(r,mid, b));
    }
    cout << "Case #" << t << ": " << max(l, r)-1 << " " << min(l, r)-1 << "\n";
  }
}
