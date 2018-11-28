#include <iostream>
#include <string>
#include <set>

using namespace std;

int main(void) 
{
  int i;
  int k, n;
  int t, tt;
  int maxans, minans;
  multiset<int> metric;
  multiset<int>::iterator widest;

  cin >> tt;
  for(t = 1; t <= tt; ++t) {
    cin >> n;
    cin >> k;

    metric.clear();
    metric.insert(n);
    for(i = 0; i < k; ++i) {
      widest = metric.end(); widest--;
      int w = *widest;
      metric.erase(widest);

      w--;
      minans = w / 2;
      maxans = w / 2 + w % 2;
      metric.insert(minans);
      metric.insert(maxans);
    }

    cout << "Case #" << t << ": " << maxans << " " << minans << endl;
  }

  return 0;
}

