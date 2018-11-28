#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

#include <functional>
#include <cassert>

typedef long long ll;
using namespace std;

#define debug(x) cerr << #x << " = " << x << endl;


#define mod 1000000007 //1e9+7(prime number)
#define INF 1000000000 //1e9
#define LLINF 2000000000000000000LL //2e18
#define SIZE 10000

void solve(){
  int n;
  int r,y,b;

  scanf("%d%d%*d%d%*d%d%*d",&n,&r,&y,&b);

  if(r*2 > n || y*2 > n || b*2 > n){
    puts("IMPOSSIBLE");
    return;
  }

  debug(r);
  debug(y);
  debug(b);
  

  char ans[SIZE] = {};

  vector<string> vec;
  
  for(int i=0;i<n/2;i++){

    if(r == max({r,y,b})){
      if(y > b){
        vec.push_back("RY");
        r--;y--;
      }else{
        vec.push_back("RB");
        r--;b--;
      }
    }else if(y == max({r,y,b})){
      if(r > b){
        vec.push_back("RY");
        r--;y--;
      }else{
        vec.push_back("BY");
        b--;y--;
      }
    }else{
      if(r > y){
        vec.push_back("RB");
        r--;b--;
      }else{
        vec.push_back("BY");
        b--;y--;
      }
    }
  }

  string ans1 = "" + vec[0].substr(0,1), ans2 = "" + vec[0].substr(1,1);

  if(r > 0 && ans1[ans1.size()-1] != 'R' && ans2[ans2.size()-1] != 'R'){
    ans1 += 'R';
    r--;
  }
  if(b > 0 && ans1[ans1.size()-1] != 'B' && ans2[ans2.size()-1] != 'B'){
    ans1 += 'B';
    b--;
  }
  if(y > 0 && ans1[ans1.size()-1] != 'Y' && ans2[ans2.size()-1] != 'Y'){
    ans1 += 'Y';
    y--;
  }
  
  for(int i=1;i<n/2;i++){
    if(vec[i][0] != ans1[ans1.size()-1] && vec[i][1] != ans2[ans2.size()-1]){
      ans1 += vec[i][0];
      ans2 += vec[i][1];
    }else{
      ans2 += vec[i][0];
      ans1 += vec[i][1];
    }

    if(r > 0 && ans1[ans1.size()-1] != 'R' && ans2[ans2.size()-1] != 'R'){
      ans1 += 'R';
      r--;
    }
    if(b > 0 && ans1[ans1.size()-1] != 'B' && ans2[ans2.size()-1] != 'B'){
      ans1 += 'B';
      b--;
    }
    if(y > 0 && ans1[ans1.size()-1] != 'Y' && ans2[ans2.size()-1] != 'Y'){
      ans1 += 'Y';
      y--;
    }
  }

  assert(r+y+b==0);
  
  reverse(ans2.begin(),ans2.end());

  ans1 += ans2;
  
  cout << ans1 << endl;
                  
}

int main(){
  int T;

  scanf("%d",&T);

  for(int i=1;i<=T;i++){

    printf("Case #%d: ",i);

    solve();
  }
  
  return 0;
}
