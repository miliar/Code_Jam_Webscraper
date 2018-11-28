#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main(){
  int T, K;
  string S;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    cin >> S >> K;
    vector<bool> l_k;
    for (char c : S) {
      l_k.push_back((c == '+' ? true : false));
    }
    int count = 0;
    int i= 0;
    for (; i < l_k.size(); i++) {
      if (!l_k[i]) {
        count++;
        int j = 0;
        for (; j < K && i + j < l_k.size(); j++)
          l_k[i + j] = !l_k[i + j];
        if (j != K)
          break;
      }
    }
    if (i != l_k.size())
      cout << "IMPOSSIBLE";
    else
      cout << count;
    cout << endl;
  }
}
