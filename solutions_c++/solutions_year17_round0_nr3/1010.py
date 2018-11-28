#include <iostream>
#include <map>
#include <queue>
using namespace std;

int main(void) {
  int T; cin >> T;
  for(int ts=1; ts<=T; ts++) {
    long N, K; cin >> N >> K;
    //cout << N << " " << K << endl;
    priority_queue<long> q;
    q.push(N);
    map<long,long> cnts;
    cnts[N]=1;
    long j;
    for(;;) {
      j=q.top();
      //cout << j << " " << cnts[j] << " " << K << endl;
      if(cnts[j]==0) {
        q.pop();
        continue;
      }
      if(cnts[j]>=K) break;
      K -= cnts[j];
      long j1=j/2;
      long j2=(j-1)/2;
      cnts[j1] += cnts[j];
      cnts[j2] += cnts[j];
      cnts[j]=0;
      q.pop();
      q.push(j1);
      if(j1!=j2) q.push(j2);
    }
    cout << "Case #" << ts << ": " << (j/2) << " " << ((j-1)/2) << endl;
  }
}
