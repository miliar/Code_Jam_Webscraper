#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
using namespace std;

bool check(vector<bool>& arr) {
  return accumulate(arr.begin(), arr.end(), 0) == 0;
}

int gao(vector<bool>& arr, int K) {
  if (check(arr)) {
    return 0;
  }
  int N = arr.size();
  if (K > N) {
    return -1;
  }
  int result = N + 1;
  for (int i = 0; i <= N - K; ++i) {
    if (arr[i] == 1) {
      vector<bool> temp = arr;
      int tempCnt = 0;
      for (int j = i; j <= N - K; ++j) {
        if (temp[j] == 1) {
          tempCnt++;
          for (int k = j; k - j < K; k++) {
            temp[k] = !temp[k];
          }
        }
      }
      if (check(temp)) {
        result = min(result, tempCnt);
      }
    }
  }
  return result > N ? -1 : result;
}
int main() {
    int caseN = 0;
    cin >> caseN;
    for (int tcas = 1; tcas <= caseN; ++tcas) {
      string inputS;
      int K;
      cin >> inputS >> K;
      vector<bool> initArray;
      for (auto c : inputS) {
        initArray.push_back(c == '-');
      }
      int result = gao(initArray, K);
      cout << "Case #" << tcas << ": ";
      if (result == -1) {
        cout << "IMPOSSIBLE" << endl;
      } else {
        cout << result << endl;
      }
    }

}
