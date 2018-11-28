#include <iostream>
#include <queue>
#include <utility>
using namespace std;

long long cal(long long n, long long k) {
  priority_queue<long long> q;
  q.push(n);
  long long cur;
  for(int i=0; i<k; i++){
    cur = q.top();
    q.pop();
    q.push(cur/2);
    if(cur%2 == 0){
      q.push((cur/2) -1);
    }else {
      q.push(cur/2);
    }
  }
  return cur;
}

int main() {
  int T;
  cin >> T;
  for(int num = 1; num <= T; num++) {
    int N, K;
    cin >> N >> K;
    long long cnt = cal(N, K);
    long long a = cnt/2;
    long long b = (cnt%2 == 0 ? (cnt/2) -1: cnt/2);
    cout << "Case #" << num << ": " << a << " " << b << endl;
  }
}
