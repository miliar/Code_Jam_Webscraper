#include <cstdio>
#include <iostream>
#include <stack>
#include <queue>

using namespace std;

int main(){
  int T;
  cin >> T;

  for(int i = 1; i <= T; i++){
    long long K, N;
    cin >> N >> K;
    priority_queue<long long> seq;
    seq.push(N);
    long long cnt = 0;
    while(!seq.empty()){
      cnt++;
      long long x = seq.top();
      seq.pop();
      if(x < 2) break;
      N = x;
      long long center = x/2 + x%2;
      long long l = center - 1;
      long long r = N - center;
      if(l > 1) seq.push(l);
      if(r > 1) seq.push(r);
      if(cnt >= K) break;
    }
    cout << "Case #" << i << ": ";
    if(cnt < K) cout << 0 << ' ' << 0 << endl;
    else{
      long long center = N/2 + N%2;
      long long l = center - 1;
      long long r = N - center;
      cout << max(r, l) << ' ' << min(r, l) << endl;
    }
  }


  return 0;
}
