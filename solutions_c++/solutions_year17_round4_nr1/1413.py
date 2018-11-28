#include<bits/stdc++.h>
using namespace std;

int mod[5];

void solve2(int n);
void solve3(int n);
void solve4(int n);

void solve(){
  int n,p;
  vector< int > G;
  fill(mod,mod+10,0);
  cin >> n >> p;
  for(int i = 0;i < n;++i){
    int g;
    cin >> g;
    ++mod[g % p];
  }
  if(p == 2)solve2(n);
  else if(p == 3)solve3(n);
  else if(p == 4)solve4(n);
}

void solve2(int n){
  int res = mod[0];
  if(res == n)cout << res << endl;
  else cout << res + (mod[1]+1)/2 << endl;
}

void solve3(int n){
  int res = mod[0];
  int calc;
  calc = min(mod[1],mod[2]);
  res += calc;mod[1] -= calc;mod[2] -= calc;

  calc = mod[1]/3;
  res += calc;
  mod[1] -= calc*3;

  calc = mod[2]/3;
  res += calc;
  mod[2] -= calc*3;

  if(mod[1] > 0 || mod[2] > 0)++res;  
  cout << res << endl;
}

void solve4(int n){
  int res = mod[0];
  int calc;
  
  calc = mod[2]/2;
  res += calc;mod[2] -= calc*2;

  calc = min(mod[1],mod[3]);
  res += calc;mod[1] -= calc;mod[3] -= calc;

  if(mod[2] > 0){
    if(mod[1] >= 2){++res;--mod[2];mod[1] -= 2;}
    else if(mod[3] >= 2){++res;--mod[2];mod[3] -= 2;};
  }

  calc = mod[1]/4;
  res += calc;
  mod[1] -= calc*4;

  calc = mod[3]/4;
  res += calc;
  mod[3] -= calc*4;

  if(mod[1] > 0 || mod[2] > 0 || mod[3] > 0)++res;
  cout << res << endl;
}


int main(void){
  int t;
  cin >> t;
  for(int i = 0;i < t;++i){
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}
