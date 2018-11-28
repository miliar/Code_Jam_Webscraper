#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>


using namespace std;
typedef unsigned long int ui64;

ui64 location(ui64 N,ui64 &L,ui64 &R){
    ui64 loc = (N+1)/2;
    L = loc-1;     R = N-loc;    return loc;
}
ui64 pow2i(int p){
  ui64 res;
  res = ((unsigned long int)1 << p);
  return res;
}
void rec(ui64 N, ui64 K,ui64 &min,ui64 &max){
  if (K==1){
    ui64 loc,L,R;
    loc = location(N,L,R);
    if (L<R){
      min = L;      max = R;
    }
    else{
      max = L;      min = R;
    }
  }
  else{
    int i;
    for (i=0; i<64;i++){
      if (pow2i(i) < K){
        K -= pow2i(i);        N -= pow2i(i);
      }
      else
        break;
    }
    ui64 bin = pow2i(i);
    ui64 div = N/bin;
    ui64 rem = N % bin;
    if (K <= rem){
      rec(div+1,1,min,max);
    }
    else{
      rec(div,1,min,max);
    }
  }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;
    int T;
    ui64 N,K;
    cin >> T;
    for(int tc=1;tc <= T;tc++){
      cin >> N;
      cin >> K;
      cout << "Case #" << tc << ": ";
      ui64 min,max;
      rec(N,K,min,max);
      cout << max << ' ' << min << endl;
    }

    return 0;
}

