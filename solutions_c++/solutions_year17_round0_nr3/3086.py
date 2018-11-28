#include <iostream>

using namespace std;



long long findBr(long long N,long long K) {
  long long l=K;
  long long m=1;
  while (l>1) {
    l/=2;
    m*=2;
  }
  N-=(m-1);
  long long d=N/m;
  long long r=N-d*m;
  if (r>K-m) {
    return d+1;
  } else
    return d;
  
  
  
  
}
    



int main() {
  int T;
  cin >> T;

  for(int t=1; t<=T; t++) {
    cout << "Case #" << t << ": ";
    long long n,k;
    cin >> n >> k;
    cout << findBr(n,k)/2 << " " << (findBr(n,k)-1)/2 << endl;
  }
  return 0;
}
