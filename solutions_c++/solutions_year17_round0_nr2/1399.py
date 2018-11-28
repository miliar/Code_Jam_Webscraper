#include <iostream>
#include <algorithm>

using namespace std;

int T;
vector<int> d;
long long N;
long long p10[20];

int main() {
  cin >> T;
  
  p10[0] = 1ll;

  for (int i = 1;i < 20;++i) {
    p10[i] = p10[i - 1] * 10ll;
  }

  for (int t = 1;t <= T;++t) {
    cout << "Case #" << t << ": ";
    d.clear();
    cin >> N;
    long long tmp = N; 
    while (tmp > 0) {
      d.push_back(tmp%10ll);
      tmp /= 10ll;
    }

    reverse(d.begin(), d.end());
  
    int i = 0;

    while (i + 1 < d.size() && d[i] <= d[i + 1]) i++;
    
    if (i != d.size() - 1) {
      while (i >= 1 && d[i] == d[i - 1]) i--;
      d[i]--;
      for (int j = i + 1;j < d.size();++j)
        d[j] = 9;
    }
    i = 0;

    while (d[i] == 0) ++i;
    for (;i < d.size();++i)
      cout << d[i];
    cout << "\n";
  }
  return 0;
}
