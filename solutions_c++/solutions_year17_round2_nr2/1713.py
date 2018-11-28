#include<bits/stdc++.h>
using namespace std;
string res;
string x;
void solve(int n,int r,int y,int b,int idx){
 if(res.size()) return;
  if(n==0){
   if(x[0] != x[idx-1]){
   res  = x;
   return;
   }
  }
  if(x[idx-1]=='R'){
  if(y >= b && y){
  x[idx] = 'Y';
  solve(n-1,r,y-1,b,idx+1);
  } else
  if(b){
  x[idx] = 'B';
  solve(n-1,r,y,b-1,idx+1);
  }
  }
  if(x[idx-1]=='Y'){
  if(r >= b && r){
  x[idx] = 'R';
  solve(n-1,r-1,y,b,idx+1);
  } else
  if(b){
  x[idx] = 'B';
  solve(n-1,r,y,b-1,idx+1);
  }
  }
  if(x[idx-1]=='B'){
  if(y >= r && y){
  x[idx] = 'Y';
  solve(n-1,r,y-1,b,idx+1);
  } else
  if(r){
  x[idx] = 'R';
  solve(n-1,r-1,y,b,idx+1);
  }
  }
}
int main(){
               cin.sync_with_stdio(false);
               freopen("a.txt","r",stdin);
               freopen("b.txt","w",stdout);
               int T , tt = 1;
               cin >> T;
               while(T--){
                   res.clear();
                   x.clear();
                   int n,r,o,y,g,b,v;
                  cin>>n>>r>>o>>y>>g>>b>>v;
                  for(int i = 0 ; i < n;  ++i )
                  x += '$';
                  if(r){
                  x[0] = 'R';
                   solve(n - 1 , r - 1 , y , b  , 1);
                   }
                                     if(y){
                  x[0] = 'Y';
                   solve(n - 1 , r  , y - 1 , b  , 1);
                   }
                                     if(b){
                  x[0] = 'B';
                   solve(n - 1 , r  , y , b - 1  , 1);
                   }



                   if(!res.size()) res = "IMPOSSIBLE";
             cout << "Case #" << tt++<<": "<< res << endl;
            }
}
