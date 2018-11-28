#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define rep(i,from,to) for(int i = from; i < (to); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define FOR(i,to) for(int i=0;i<(to);++i)
#define Nmax 101010

priority_queue<ll> pq;
map<ll,ll> h;

void clear() {
  h.clear();
  while(!pq.empty()) pq.pop();
}

void add(ll x,ll num) {
 // cout << x << endl;
  if(h.count(x)) {
    h[x]+=num;
  } else {
    h[x]+=num;
    pq.push(x);
  }
}
ll N,K,tt,T;
int main() {
  cin >> T;
  while(T--) {
    ++tt;
    cin >> N >> K;
    clear();
    add(N,1);
    cout << "Case #" << tt <<": ";
    while(!pq.empty()) {
      ll x = pq.top();
      pq.pop();
      if(h[x] >= K) {
        cout <<(x) / 2 << " " << (x-1) /2 << "\n";
        break;
      }
      K-=h[x];
      if(x == 2) {
        add(1,h[x]);
      } else if(x>2) {
        ll y = (x-1)/2;
        ll z = (x-1) - y;
        add(y,h[x]);
        add(z,h[x]);
      }
    }
  }
}
