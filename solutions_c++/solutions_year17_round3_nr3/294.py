#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int T, N, K;
int U;
priority_queue<int> pq;

int main(){
  cin >> T;
  for (int cas=1; cas <= T; cas++){
    while (!pq.empty()) pq.pop();
    cin >> N >> K;
    string US;
    cin >> US;
    if (US.length() == 7){
      U = 100000 * (US[0] - '0') + 10000 * (US[1] - '0') + 1000 * (US[3] - '0') + 100 * (US[4] - '0') + 10 * (US[5] - '0') + 1 * (US[6] - '0');
    }else{
      U = 10000 * (US[0] - '0') + 1000 * (US[2] - '0') + 100 * (US[3] - '0') + 10 * (US[4] - '0') + 1 * (US[5] - '0');
    }
    for (int i = 0; i < N; i++){
      string s;
      cin >> s;
      int val = 10000 * (s[0] - '0') + 1000 * (s[2] - '0') + 100 * (s[3] - '0') + 10 * (s[4] - '0') + 1 * (s[5] - '0');
      pq.push(-val);
    }

    for (int i = 0; i < U; i++){
      int v = pq.top();
      pq.pop();
      if (v == - 10000){
        pq.push(v);
        break;
      }else{
        v -= 1;
        pq.push(v);
      }
    }

    double prob = 1.0;
    for (int i = 0; i < N; i++){
      double tp = - (double) pq.top() / 10000.0;
      prob *= tp;
      pq.pop();
    }
    cout << "Case #" << cas << ": " << prob << endl;
  }
  return 0;
}
