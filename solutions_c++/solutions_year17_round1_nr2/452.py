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
priority_queue<ll,vector<ll>, greater<ll> > pq[2222];
ll R[2222];
ll N,M,T,tt;
int can(ll p) {
  FOR(i,N) {
    while(pq[i].size() && pq[i].top() < 0.9 * p * R[i]) pq[i].pop();
  }
  int ok = 1;
  FOR(i,N) {
  //  cout << pq[i].size() << endl;
    if(pq[i].size() == 0 || pq[i].top() > p * R[i] * 1.1) {
      ok = 0;
    }
  }
  return ok;
}

void rem() {
  FOR(i,N) pq[i].pop();
}

int main() {
  cin >> T;
  while(T--) {
    ++tt;
    cin >> N >> M;
    FOR(i,N) {
      while(pq[i].size()) pq[i].pop();
      cin >> R[i];
    }
    FOR(i,N) {
      FOR(j,M) {
        int x;
        cin >> x;
        pq[i].push(x);
      }
    }
    ll p = 1;
    ll ret = 0;
    ll ok = 1;
    while(ok) {
      //cout << p << endl;
      while(can(p)) {
        rem();
        ++ret;
      }
      FOR(i,N) {
        if(pq[i].size() == 0) ok = 0;
      }
      ++p;
    }
    cout << "Case #" << tt << ": " << ret << endl;
  } 
}
