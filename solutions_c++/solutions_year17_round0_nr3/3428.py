#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <queue>


using namespace std;

void stall(long long N, long long K)
{
  priority_queue<long long> q;
  q.push(N);

  for (int i = 1; i < K; i++) {
    long long a = q.top();
    q.pop();
    q.push(a / 2);
    q.push((a - 1) / 2);
  }

  cout << q.top() / 2 << " " << (q.top() - 1) / 2;
  
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    long long N, K;
    cin >> N >> K;

    cout << "Case #" << t << ": ";
    stall(N, K);
    cout << "\n";
  }

  return 0;
}

