#include <iostream>
#include <cstdlib>

using namespace std;

typedef long long lli;

int digits(lli n){
  int d = 0;
  while (n > 0){
    d += 1;
    n /= 10;
  }
  return d;
}

void solve(int i, int arr[], lli candidate, lli pow10,  lli top, lli &max){
  lli c;
  if(i == 0){
    return;
  }
  for(int j=1; j < 10; j++){
    if(pow10 > 1 && j > arr[i]){
      continue;
    }
    arr[i-1] = j;
    c = candidate + j * pow10;
    if(c <= top && c > max){
      max = c;
    }
    solve(i-1, arr, c, pow10 * 10, top, max);
  }
}

int main(){
  int t, d, arr[20];
  lli n, max;
  cin >> t;
  for(int _t=0; _t < t; _t++){
    cin >> n;
    max = 0;
    d = digits(n);
    solve(d, arr, 0, 1, n, max);
    cout << "Case #" << _t+1 << ": " << max << "\n";
  }
}
