#include<iostream>
#include<algorithm>

using namespace std;

#define INF (1<<25)

int cnt(int hd, int ad, int hk, int ak ,int b, int d, int B, int D){
  int Hd = hd;
  int Hk = hk;
  int dcnt = 0;
  int bcnt = 0;
  int turn = 0;
  while(true){
    turn ++;
    if(turn > 1080)return INF;
    if(dcnt < D){
      if(hd <= max(0, ak - d)){
	hd = Hd;
      }
      else{
	ak = max(0, ak - d);
	dcnt++;
      }
    }
    else if(bcnt < B){
      if(hd <= ak)hd = Hd;
      else{
	ad += b;
	bcnt++;
      }
    }
    else{
      if(hd <= ak && hk - ad > 0){
	hd = Hd;
      }
      else{
	hk -= ad;
      }
    }

    if(hk <= 0)break;
    else hd -= ak;
  }
  return turn;
}

void solve(){
  int hd, ad, hk, ak, b, d;
  cin >> hd >> ad >> hk >> ak >> b >> d;
  int res = INF;
  for(int i = 0;i <= 100;i++){
    for(int j = 0;j <= 100;j++){
      res = min(res, cnt(hd, ad, hk, ak, b, d, i, j));
    }
  }
  if(res != INF)
    cout << res << endl;
  else
    cout << "IMPOSSIBLE" << endl;
}

int main(){
  int t;
  cin >> t;
  for(int i = 1;i <= t;i++){
    cout << "Case #" << i << ": ";    solve();
  }
  return 0;
}
