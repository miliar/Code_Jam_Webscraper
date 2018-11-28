#include <iostream>
#include <cmath>
#include <set>

using namespace std;

void caseN() {
  int N;
  int K;
  cin >> N >> K;
  multiset<int, greater<int> > ss;
  int LS = N;
  int RS = N;

  ss.insert(N);
  
  for (int k = 0; k < K; ++k) {
    int L = *ss.begin();
    ss.erase(ss.begin());
  
    LS = L /2;
    RS = L /2;
    if (L%2==0)
      LS--;

    ss.insert(LS);
    ss.insert(RS);
  }

  cout << max(LS, RS) << " " << min(LS, RS) << endl;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #"<< t << ": ";
    caseN();
  }
}
