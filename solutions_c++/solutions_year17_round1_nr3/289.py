#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pii pair<int,int>
#define piii pair< pii, int >
#define tiiii tuple< int, int, int, int >
#define tiiiii tuple< int, int, int, int, int >
#define pll pair<ll,ll>
#define PB push_back
#define MP make_pair
#define MT make_tuple

int Solve(){
  int H, hd, ad, hk, ak, b, d, ans = -1;
  set< tiiiii > s;
  queue< tiiii > Q;
  queue< int > D;

  cin >> hd >> ad >> hk >> ak >> b >> d;
  H = hd;
  Q.push(MT(hd, ad, hk, ak));
  s.insert(MT(hd, ad, hk, ak, 0));
  D.push(0);

  while(!Q.empty()){
    tie(hd, ad, hk, ak) = Q.front();
    int k = D.front();
    int x = (k + 1) % 2;

    Q.pop();
    D.pop();

    if(hd <= 0)
      continue;

    if(hk <= 0){
      ans = (k + 1) / 2;
      break;
    }

    if(k % 2){
      if(hd - ak > 0 && s.find(MT(hd - ak, ad, hk, ak, x)) == s.end()){
        Q.push(MT(hd - ak, ad, hk, ak));
        s.insert(MT(hd - ak, ad, hk, ak, x));
        D.push(k + 1);
      }
      continue;
    }

    if(s.find(MT(hd, ad, hk - ad, ak, x)) == s.end()){
      Q.push(MT(hd, ad, hk - ad, ak));
      s.insert(MT(hd, ad, hk - ad, ak, x));
      D.push(k + 1);
    }

    if(s.find(MT(hd, ad + b, hk, ak, x)) == s.end()){
      Q.push(MT(hd, ad + b, hk, ak));
      s.insert(MT(hd, ad + b, hk, ak, x));
      D.push(k + 1);
    }

    if(s.find(MT(H, ad, hk, ak, x)) == s.end()){
      Q.push(MT(H, ad, hk, ak));
      s.insert(MT(H, ad, hk, ak, x));
      D.push(k + 1);
    }

    ak = max(0, ak - d);
    if(s.find(MT(hd, ad, hk, ak, x)) == s.end()){
      Q.push(MT(hd, ad, hk, ak));
      s.insert(MT(hd, ad, hk, ak, x));
      D.push(k + 1);
    }
  }

  return ans;
}

int main(){
  int t;
  scanf("%d", &t);
  for(int k = 1; k <= t; k++){
    int ans = Solve();
    if(ans < 0)
      printf("Case #%d: IMPOSSIBLE\n", k);
    else
      printf("Case #%d: %d\n", k, ans);
  }
  return 0;
}
