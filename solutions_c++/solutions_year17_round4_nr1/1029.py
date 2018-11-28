#include <bits/stdc++.h>
using namespace std;

int main() {
  int T;
  cin >> T;
  while (T--) {

    int N, P;
    cin >> N >> P;
    vector<int> G(N);
    for (int &a:G) cin >> a;

    int res = 0;
    if (P == 2) {
      int cnt = 0;
      for( int a : G ){
        if( a%P == 0 ) res++;
        else cnt++;
      }
      if( cnt )
        res += (cnt-1)/2+1;
    } else if( P == 3 ){
      int cnt1 = 0, cnt2 = 0;
      for( int a : G ){
        if( a%P == 0 ) res++;
        else if( a%P == 1 ) cnt1++;
        else cnt2++;
      }
      int mc = min(cnt1,cnt2);
      res += mc;
      cnt1 -= mc; cnt2 -= mc;
      if( cnt2 ) swap( cnt1, cnt2 );
      if( cnt1 )
        res += (cnt1-1)/3+1;
    } else {

      int cnt1 = 0, cnt2 = 0, cnt3 = 0;
      for( int a : G ){
        if( a%P == 0 ) res++;
        else if( a%P == 1 ) cnt1++;
        else if( a%P == 2 ) cnt2++;
        else cnt3++;
      }

      res += cnt2/2;
      cnt2%=2;

      int mc = min( cnt1, cnt3 );
      res += mc;
      cnt1 -= mc; cnt3 -= mc;
      if( cnt3 ) swap( cnt1, cnt3 );

      if(cnt2){
        cnt1+=2;
      }
      if( cnt1 )
        res += (cnt1-1)/4+1;
    }

    static int ttt = 1;
    cout << "Case #" << ttt++ << ": ";
    cout << res << endl;
  }

}