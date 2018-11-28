#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cassert>
using namespace std;

struct acts{
  int st, ed, no;
};

int main() {
  int tt;
  cin >> tt;
  for (int tcas = 1; tcas <= tt; tcas++) {
    int N, K;
    vector<int> spare[2];
    vector<acts> arr;
    int result = 0;
    cin >> N >> K;
    for (int i = 0; i < N + K; i++) {
      acts A;
      cin >> A.st >> A.ed;
      A.no = i < N;
      arr.push_back(A);
    }
    sort(arr.begin(), arr.end(), [](acts A, acts B) {
      return A.st < B.st;
    });
    int used[2] = {0, 0};
    int flexSum = 0;
    for (int i = 0; i < arr.size(); i++) {
      int last = (i - 1 + arr.size()) % arr.size();
      int tim = (arr[i].st - arr[last].ed + 24 * 60) % (24 * 60);
      used[arr[i].no] += tim + arr[i].ed - arr[i].st;
      if (arr[i].no != arr[last].no) {
        flexSum += tim;
        result ++;
      } else {
        spare[arr[i].no].push_back(tim);
      }
    }

    assert(used[0] + used[1] == 1440);


    sort(spare[0].begin(), spare[0].end());
    sort(spare[1].begin(), spare[1].end());

    int bigOne;
    if (used[0] > used[1]) {
      bigOne = 0;
    } else bigOne = 1;
    int diff = abs(used[0] - used[1]) / 2;
    diff -= flexSum;
    if (spare[bigOne].size() > 0) {
      for (int i = spare[bigOne].size() - 1; diff > 0 && i >= 0; i--) {
        diff -= spare[bigOne][i];
        result += 2;
      }
    }
    cout << "Case #" << tcas << ": " << result << endl;


  }
}
