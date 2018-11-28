#include <iostream>
using namespace std;

typedef unsigned long long ull;

pair<ull, ull> calcMaxMin(ull n, ull k)
{

  ull nMax, nMin;
  nMax = nMin = (n-1)/2;
  if (n % 2 == 0)
    nMax++;
  
  if (k == 1) return pair<ull, ull>(nMax,nMin);

  ull k1, k2;
  k1 = k2 = (k-1)/2;
  if (k % 2 == 0)
    k2++;

  if(k2 > k1 || k1 == 0)
    return calcMaxMin(nMax, k2);
  else
    return calcMaxMin(nMin, k1);
      
}

int main() {

  int t;
  cin >> t;  
  for (int i = 1; i <= t; ++i) {
    ull n, k;
    cin >> n >> k;
    pair<ull, ull> res = calcMaxMin(n, k);
    cout << "Case #" << i << ": " << res.first << " " << res.second << endl;
  }

  return 0;
}
