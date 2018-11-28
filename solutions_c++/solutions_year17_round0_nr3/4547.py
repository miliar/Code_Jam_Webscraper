#include <iostream>
#include <vector>
#include <queue>
using namespace std;
typedef unsigned long int UL;
typedef pair<int, int> PII;
class Compare
{
public:
    bool operator() (PII a, PII b) //strict weak
    {
      int m_a = min(a.first, a.second), m_b = min(b.first, b.second);
      if (m_a != m_b)
        return m_a < m_b;
      else {
        m_a = max(a.first, a.second), m_b = max(b.first, b.second);
        if (m_a != m_b)
          return m_a < m_b;
      }
      return true;
    }
};
int main(){
  int T;
  UL N, K;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    cin >> N >> K;
    priority_queue<PII, std::vector<PII>, Compare> pq;
    if (N & 1) //odd
      pq.push(PII(N/2, N/2));
    else
      pq.push(PII((N-1)/2, N/2));
    while(!pq.empty() && K > 1) {
      PII k = pq.top(); pq.pop();
      //cout << k.first << " " << k.second << " " << pq.size() << endl;
      if (k.first & 1) //odd
        pq.push(PII(k.first/2, k.first/2));
      else if (k.first > 0)
        pq.push(PII((k.first-1)/2, k.first/2));
      if (k.second & 1) //odd
        pq.push(PII(k.second/2, k.second/2));
      else if (k.second > 0)
        pq.push(PII((k.second-1)/2, k.second/2));
      K--;
    }
    PII k = pq.top();
    cout << max(k.first, k.second) << " " << min(k.first, k.second) << endl;
  }
}
