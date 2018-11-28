#include <iostream>
using namespace std;
long long pow2(long long e) {
  long long ans = 1;
  while(e--) ans = ans << 1;
  return ans;
}
int main() {
  int t;
  long long n, k;
  cin >> t;
  for(int i = 1; i <= t; i++) {
    cin >> n >> k;
    long long y, z, ny, nz, my, mz;
    long long hy, hz, nhy, nhz;
    long long top;
    long long power = 1;
    long long j = 1;
    y = n;
    z = n;
    hy = 1;
    hz = 0;
    while(j < k) {
      ny = (y-1)/2 + (y-1)%2;
      my = (y-1)/2;
      nhy = hy;
      nhz = 0;
      if(my == ny) {
        nhy += hy;
      }
      else {
        nhz += hy;
      }
      nz = (z-1)/2 + (z-1)%2;
      mz = (z-1)/2;
      if(nz == ny) {
        nhy += hz;
      }
      else {
        nhz += hz;
      }
      if(mz == ny) {
        nhy += hz;
      }
      else {
        nhz += hz;
      }
      hy = nhy;
      hz = nhz;
      y = max(ny, max(my, max(nz, mz)));
      z = max(0ll, min(ny, min(my, min(nz, mz))));
      j += pow2(power);
      power++;
    }
    if(k-(j-pow2(power-1)) <= hy) {
      cout << "Case #" << i << ": " << (y-1)/2+(y-1)%2 << ' ' << (y-1)/2 << '\n';
    }
    else {
      cout << "Case #" << i << ": " << (z-1)/2+(z-1)%2 << ' ' << (z-1)/2 << '\n';
    }


    /*
    for(int j = 0; j < k; j+=pow(2, i)) {
      y = n/2 + n%2;
      z = n/2;
      if(k == j) {
        cout << y, z else z z
      }
    }
    */
  }
}
