#include <iostream>
#include <vector>

using namespace std;

int solve() {
  string s;
  cin >> s;
  vector<bool> vec;
  for (int i = 0;i < s.size();i++)
    vec.push_back(s[i] == '+');
  int k;
  cin >> k;
  int count = 0;
  int i;
  for(i = 0;i<=vec.size()-k;i++) {
    if(!vec[i]) {
      count++;
      for(int j = i; j < i + k;j++) {
        vec[j] = !vec[j];
      }
    }
//    for(int c = 0;c<vec.size();c++)
//      cout << vec[c] << " ";
//    cout << endl;
  }
  for(;i < vec.size();i++) {
    if(!vec[i]) return -1;
  }

  return count;
}

int main() {
  int T;
  cin >> T;
  for(int t = 1;t<=T;t++) {
    int a = solve();
    if (a == -1)
      cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    else
      cout << "Case #" << t << ": " << a << endl;
  }
}
