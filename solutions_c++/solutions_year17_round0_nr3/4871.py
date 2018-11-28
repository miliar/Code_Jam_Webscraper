#include <bits/stdc++.h>
#define ll long long

using namespace std ;

int main(int argc, char const *argv[])
{
  ll count;
  cin >> count ;
  for (ll j = 0; j < count; ++j) {
    cout << "Case #" << j + 1 << ": " ;
    ll N, K;
    cin >> N >> K;
    if(K==1) {
      if(N%2) {
        cout << N/2 << " " << N/2 << endl;
        continue;
      }
      cout << N/2 << " " << ((N/2)-1) << endl;
      continue;
    }
    ll odd{1}, even{1};
    if (N % 2) {
      if((N/2 )%2) {
        odd = 2;
        even = 0;
      }
      else {
        odd = 0;
        even = 2;
      }
    }
    ll t = floor(log2(K)) + 1;
    ll t1{0}, p{K - powl(2, t - 1) + 1};
    while (t) {
      ll temp{odd};
      if (t1)
        odd = even;
      if (t1 && !(((N - 1) / 2 ) % 2)) {
        even += temp * 2;
      }
      else if (t1) {
        odd += temp * 2;
      }
      N /= 2;
      t1++;
      t--;
    }
    bool same{true};
    ll pos;
    if ((even >= odd) == !(N % 2)) {
      if (!(N % 2)) {
        pos = (even - odd) / 2;
      }
      else {
        pos = (odd - even) / 2;
      }
    }
    else {
      pos = min(even,odd);
      same = false;
    }
    ll N1;
    if(!N) {
      N1 = 0;
    }
    else {
      N1 = N-1;
    }
    if (same) {
      if (p <= pos) {
        cout << N << " " << N << endl;
      }
      else {
        cout << N << " " << N1 << endl;
      }
      continue;
    }
    else {
      if (p <= pos) {
        cout << N << " " << N1 << endl;
      }
      else {
        cout << N1 << " " << N1 << endl;
      }
    }
  }
  return 0;
}
