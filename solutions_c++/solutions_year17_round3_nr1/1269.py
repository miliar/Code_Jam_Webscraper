#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

int main(){
  cout << fixed << setprecision(9);
  int t;
  cin >> t;
  for (int a = 0; a < t; a++) {
    int n, k;
    cin >> n >> k;
    priority_queue<pair<ll, int> > largest;
    vector<pair<int, int> > pancakes;
    for (int i = 0; i < n; i++) {
      ll x, y;
      cin >> x >> y;
      pancakes.push_back(make_pair(x, y));
      largest.push(make_pair(x*y,i));
    }

    double answer = 0;
    for (int i = 0; i < n; i++) {
      priority_queue<pair<ll, int> > tmpLargest = largest;
      double tmp = 0;
      tmp = M_PI * pancakes[i].first * pancakes[i].first + 2 * M_PI * pancakes[i].first * pancakes[i].second;
      int j = 0;
      while (j < k-1) {
	pair<ll, int> tmpPancake = tmpLargest.top();
	tmpLargest.pop();
	if (tmpPancake.second != i) {
	  int index = tmpPancake.second;
	  tmp += 2 * M_PI * pancakes[index].first * pancakes[index].second;
	  j += 1;
	}
      }

      if (tmp > answer) answer = tmp;
    }

    cout << "Case #" << a+1 << ": " << answer << endl;
  }
  return 0;
}
