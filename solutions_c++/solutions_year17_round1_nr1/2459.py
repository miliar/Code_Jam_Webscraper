#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;
typedef unsigned long long ull;

string output[26];

void calc(int y, int x, vector<string>& v){
  vector<int> wl,wr;
  int st = 0, ed = v.size();
  rep(i,v.size()){
    if(i<y && output[i][x] != '?' && output[i][x] != v[y][x]){
      wl.clear();
      wr.clear();
      st = i+1;
    }
    else if(i>y && output[i][x] != '?' && output[i][x] != v[y][x]){
      ed = i;
      break;
    }else{
      int lhs = x, rhs = x;
      while(lhs-1>=0 && output[i][lhs-1]=='?') lhs--;
      while(rhs+1<v[0].size() && output[i][rhs+1]=='?') rhs++;
      wl.push_back(lhs);
      wr.push_back(rhs);
    }
  }
  int mnl = -1, mnr = 10000000;
  rep(i,wl.size()){
    if(st+i<=y){
      mnl = max(mnl, wl[i]);
      mnr = min(mnr, wr[i]);
    }else{
      if(wl[i]>mnl || wr[i]<mnr){
        ed = st+i;
        break;
      }
    }
  }

  REP(i,st,ed){
    REP(j,mnl,mnr+1){
      output[i][j] = v[y][x];
    }
  }
  //cout << v[y][x] << " " << st << " " << ed << " " << mnl << " " << mnr << endl;
}


void solve(int R, int C, vector<string> v){
  rep(i,R){
    rep(j,C){
      if(v[i][j] != '?'){
        calc(i,j,v);
      }
    }
  }
    

  rep(i,R){
    cout << output[i] << endl;
  }
}


int main(){
  int T;
  cin >> T;

  rep(t,T){
    int R, C;
    vector<string> v;
    cin >> R >> C;
    rep(i,R){
      string tmp;
      cin >> tmp;
      output[i] = tmp;
      v.push_back(tmp);
    }
    
    cout << "Case #" << t+1 << ":" << endl;
    solve(R, C, v);
  }
  
  return 0;
}



//ios::sync_with_stdio(false);
