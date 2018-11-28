#include <iostream>
#include <cassert>

using namespace std;

long long solve(long long N, long long have1, long long have2, long long K){
  //cout << N << " " << have1 << " " << have2 << " " << K << endl;
  if(K <= have1) return N;
  K -= have1;
  if(K <= have2) return N - 1;
  K -= have2;

  long long next_have1 = 0;
  long long next_have2 = 0;

  if(N % 2 == 0){
    next_have1 = have1;
    next_have2 = have2 * 2 + have1;
  }else{
    next_have1 = have1 * 2 + have2;
    next_have2 = have2;
  }

  return solve(N / 2, next_have1, next_have2, K);
}

int main(){
  int T;
  cin >> T;
  long long N,K;

  for(int tc = 1;tc <= T;++tc){
    cin >> N >> K;
    long long L = solve(N,1,0,K);
    //cout << "L = " << L << endl;
    cout << "Case #" << tc << ": " << L / 2 << " " << (L - 1) / 2 << "\n";
  }

  return 0;
}
