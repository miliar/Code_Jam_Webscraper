#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int T;

int main () {

  cin >> T;

  for(int tc=1;tc<=T;tc++) {
    int N, K;
    cin >> N >> K;
    double u;
    cin >> u;
    vector<double> p(N);
    double sum = u;
    priority_queue<double> pq;
    for(int i=0;i<N;i++) {
      cin >> p[i];
      pq.push(p[i]);
      sum += p[i];
    }
    double avg = sum / N;
    while(avg < pq.top() && !pq.empty()) {
      sum -= pq.top();
      pq.pop();
      avg = sum / pq.size();
    }
    
    for(int i=0;i<p.size();i++) {
      if(p[i] < avg) {
        p[i] = avg;
      }
      p[i] = min(p[i], 1.0);
    }
    double ret = 1.0;

    for(int i=0;i<p.size();i++) {
      ret = ret * p[i];
    }
    printf("Case #%d: ",tc);
    printf("%.7f", ret);
    printf("\n");
  }

  return 0;
}