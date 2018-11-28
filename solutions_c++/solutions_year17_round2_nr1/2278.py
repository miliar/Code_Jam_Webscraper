#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

ifstream cin ("test.in");
ofstream cout("test.out");

const int MaxN = 1005;

vector <pair <double, double>> horseList;
int dist, n, TaskNr;

int main() {
  cin >> TaskNr;
  for (int task = 1; task <= TaskNr; ++task) {
    cin >> dist >> n;
    horseList.clear();
    for (int i = 1; i <= n; ++i) {
      double k, s;
      cin >> k >> s;
      horseList.push_back(make_pair(k, s));
    }

    sort(horseList.begin(), horseList.end());
    horseList.push_back(make_pair(dist, 0));

    double timeAtEnd = 0;
    double currPos = horseList.front().first;
    double horseSpeed = horseList.front().second;
    for (int i = 1; i < horseList.size(); ++i) {
      if (horseList[i].second >= horseList[i - 1].second) {
        continue;
      }

      horseList[i].first += horseList[i].second * timeAtEnd;
      double currTime = (horseList[i].first - currPos) / (horseSpeed - horseList[i].second);
      currTime = min(currTime, (dist - currPos) / horseSpeed);
      currPos = currPos + currTime * horseList[i - 1].second;
      timeAtEnd += currTime;
      horseSpeed = min(horseSpeed, horseList[i].second);
    }

    double ans = dist / timeAtEnd;
    cout << fixed << setprecision(10) << "Case #" << task << ": " << ans << '\n';
  }
  return 0;
}
