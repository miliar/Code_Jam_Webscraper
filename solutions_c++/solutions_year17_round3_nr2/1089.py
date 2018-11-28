#include <bits/stdc++.h>


using namespace std;
typedef pair<int, int> pii;

int main(){
  int t;
  cin >> t;
  for (int a = 0; a < t; a++) {
    int ans = 2;
    int Ac, Aj;
    cin >> Ac >> Aj;
    priority_queue<pii, vector<pii>, greater<pii> > scheduleC;
    priority_queue<pii, vector<pii>, greater<pii> > scheduleJ;
    for (int i = 0; i < Ac; i++) {
      int x, y;
      cin >> x >> y;
      scheduleC.push(make_pair(x, y));
    }
    for (int i = 0; i < Aj; i++) {
      int x, y;
      cin >> x >> y;
      scheduleJ.push(make_pair(x, y));
    }

    if (Ac == 1 || Aj == 1) {
      ans = 2;
    }
    else if (Ac == 2) {
      int start1, end1, start2, end2;
      start1 = scheduleC.top().first;
      start2 = scheduleC.top().second;
      scheduleC.pop();
      end1 = scheduleC.top().second;
      end2 = scheduleC.top().first;
      // cout << start << " " << end << endl;
      if (end1 - start1 <= 720 || end2 - start2 >= 720) {
	ans = 2;
      }
      else ans = 4;
    }
    else {
      int start1, end1, start2, end2;
      start1 = scheduleJ.top().first;
      start2 = scheduleJ.top().second;
      scheduleJ.pop();
      end1 = scheduleJ.top().second;
      end2 = scheduleJ.top().first;
      // cout << start << " " << end << endl;
      if (end1 - start1 <= 720 || end2 - start2 >= 720) {
	ans = 2;
      }
      else ans = 4;
    }

    cout << "Case #" << a+1 << ": " << ans << endl;
  }
  return 0;
}
