#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;
typedef unsigned long long ull;

bool check(ll N){
  int prev = 9;
  while(N>0){
    if(N%10 > prev) return false;
    prev = N%10;
    N /= 10;
  }
  return true;
}

ll solve_naive(ll N){
  stringstream ss;
  ss << N;
  int len = ss.str().size();
  if(len == 1) return N;

  for(ll x = N; x>=0; x--){
    if(check(x)){
      return x;
    }
  }
}

ll solve(ll N){
  stringstream ss;
  ss << N;
  string s = ss.str();
  if(s.size() == 1) return N;
  int b = 0;
  REP(i,1,s.size()){
    if(s[i]-'0' > s[i-1]-'0'){
      b = i;
    }
    if(s[i]-'0' < s[i-1]-'0'){
      if(b == 0){
        if(s[0] == '1'){
          s = string(s.size()-1, '9');
        }else{
          s[0] = (char)('0' + (int)(s[0]-'0')-1);
          REP(j,1,s.size()){
            s[j] = '9';
          }
        }
      }else{
        s[b] = (char)('0' + (int)(s[b]-'0')-1);
        REP(j,b+1,s.size()){
          s[j] = '9';
        }
      }
      break;
    }
  }
  ll ret = 0;
  stringstream tt(s);
  tt >> ret;
  return ret;
}

int test(){
  REP(N,1,100000){
    if(solve(N) != solve_naive(N)){
      cout << N << " " << solve(N) << " " << solve_naive(N) << endl;
    }
  }

  return 0;
}


int main(){
  int T;
  cin >> T;
  rep(t,T){
    ll N;
    cin >> N;

    ll ret = solve(N);
    
    cout << "Case #" << t+1 << ": " << ret << endl;
  }
  
  return 0;
}



//ios::sync_with_stdio(false);
