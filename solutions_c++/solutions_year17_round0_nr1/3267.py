#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>
#include <string>
#include <climits>
using namespace std;

int globalMin = INT_MAX;

void flip(char &k) {
  if (k == '+') k = '-';
  else k = '+';
}
void DFShelper(string result, string &comp1, string &comp2, vector<bool> &visited, int &len, int &K, int slow, int level) {
  //cout << "result=" << result << " level=" << level << " slow=" << slow<< endl;
  if (result == comp1 || result == comp2) {
    if (level < globalMin) {
    //   cout << "here we go" << endl;
       globalMin = level;
    }
  }
  for (int i = slow; !visited[i] && i < len; i++) {
    //if (i == slow) {
      for (int j = i; j < i + K; j++) flip(result[j]);
      visited[i] = true;
      DFShelper(result, comp1, comp2, visited, len, K, i+1, level+1);
      visited[i] = false;
      for (int j = i; j < i + K; j++) flip(result[j]);
    //} else {
    //  visited[i] = true;
    //  flip(result[i]); flip(result[i+K]);
    //  DFShelper(result, comp1, comp2, visited, len, K, i+1, level+1);
    //  flip(result[i]); flip(result[i+K]);
    //  visited[i] = false;
    //}
  }
}

string solution(string S, int K) {
  string result(S.length(), '+');
  string comp1 = S, comp2;
  vector<bool> visited(S.length(), false);
  int left = 0, right = S.length() - 1;
  int len = S.length() - K + 1;//(S.length() - K + 1) / 2;
  //if (S == result) return 0;
  while(left < right) swap(S[left++], S[right--]);
  comp2 = S;
  //cout << comp1 <<" " << comp2 << endl;
  DFShelper(result, comp1, comp2, visited, len, K, 0, 0);
  return globalMin == INT_MAX ? "IMPOSSIBLE" : to_string(globalMin);
}

int main() {
    int T, K;
    string S;
    cin >> T;
    for ( int i = 0; i < T; i++) {
        cin >> S;
        cin >> K;
        cout << "Case #" << i+1 <<": " << solution(S, K) << endl;
        globalMin = INT_MAX;
    }
    return 0;
}
