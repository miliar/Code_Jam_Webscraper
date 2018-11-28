#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;
typedef unsigned long long ull;

pair<ll,ll> solve_naive(ll N, ll K){
  map<ll,ll> memo;
  priority_queue<ll> que;
  que.push(N);

  rep(i,K-1){
    ll now = que.top(); que.pop();
    memo[now]++;
    if(now%2==0){
      if(now>=2){
        que.push(now/2);
        que.push(now/2-1);
      }
    }else{
      if(now>2){
        que.push((now-1)/2);
        que.push((now-1)/2);
      }
    }
  }
  ll ret = que.top();
  if(ret%2==0){
    return make_pair(ret/2, ret/2-1);
  }else{
    return make_pair((ret-1)/2, (ret-1)/2);
  }
}

pair<ll,ll> solve(ll N, ll K){
  map<ll,ll> memo;
  ll x = N, y = 0, xcnt = 1, ycnt = 0;
  while(true){
    //cout << " " << x << " " << y << " " << xcnt << " " << ycnt << endl;
    memo[x] += xcnt;
    if(y>0) memo[y] += ycnt;
    if(x==1) break;
    
    ll nx, ny, nxcnt = 0, nycnt = 0;
    if(x%2==0){
      nx = x/2;
      ny = x/2-1;
      nxcnt += xcnt;
      nycnt += xcnt;
      nycnt += 2*ycnt;
    }else{
      nx = (x-1)/2;
      ny = (x-1)/2 - 1;
      nxcnt += 2*xcnt;
      nxcnt += ycnt;
      nycnt += ycnt;
    }
    x = nx;
    y = ny;
    xcnt = nxcnt;
    ycnt = nycnt;
  }
  
  for(map<ll,ll>::reverse_iterator itr=memo.rbegin(); itr!=memo.rend(); ++itr){
    if(K <= itr->second){
      ll ret = itr->first;
      if(ret%2==0){
        return make_pair(ret/2, ret/2-1);
      }else{
        return make_pair((ret-1)/2, (ret-1)/2);
      }
      break;
    }
    K -= itr->second;
  }
  return make_pair(0,0);
}

int test(){
  for(ll N=1; N<=1000; N++){
    for(ll K=1; K<=N; K++){
      pair<ll,ll> ret1 = solve(N, K);
      pair<ll,ll> ret2 = solve_naive(N, K);

      if(ret1.first != ret2.first || ret1.second != ret2.second){
        cout << N << " " << K << " " << ret1.first << " " << ret1.second << "   " << ret2.first << " " << ret2.second << endl;
      }
    }
  }
  
  return 0;
}

int main(){
  int T;
  cin >> T;
  rep(t,T){
    ll N, K;
    cin >> N >> K;

    pair<ll,ll> ret = solve(N, K);

    cout << "Case #" << t+1 << ": " << ret.first << " " << ret.second << endl;
  }
  
  return 0;
}



//ios::sync_with_stdio(false);
