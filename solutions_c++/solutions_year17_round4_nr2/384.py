#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int main() {
  int numTestCases;
  cin >> numTestCases;
  for (int curTestCase=1; curTestCase <= numTestCases; ++curTestCase) {
    cout << "Case #" << curTestCase << ": ";
    
    int n, c, m;
    cin >> n >> c >> m;
    vector<int> p(n,0), b(c,0);
    for (int i=0; i<m; ++i) {
      int pi, bi;
      cin >> pi >> bi;
      p[pi-1]++;
      b[bi-1]++;
    }
    int rides=0;
    for (int i=0;i<c;++i)
      rides = max(rides, b[i]);
    int sum=0;
    for (int i=0;i<n;++i) {
      sum += p[i];
      rides = max(rides, (sum+i)/(i+1));
    }
    int proms = 0;
    for (int i=0;i<n;++i)
      if (p[i] > rides)
        proms += p[i]-rides;
    cout << rides << ' ' << proms << endl;
  }
}
