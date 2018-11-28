#include <string>
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
using namespace std;

//map<int, int> cache;
void problem() {
  unsigned long long n;
  cin >> n;
  string s = to_string(n);
  int i = 1;
  while (s[i] >= s[i- 1]) {
    i++;
  }
  if (i != s.size()) {
    int t = i;
    do {
      // fill 9s to right
      while (i < s.size()) {
        s[i++] = '9';
      }

      t--;
      if (s[t] == '0') {
        s[t] = '9';
      } else {
        s[t]--;
      }
      i = t;
    } while (t > 0 && s[t] < s[t - 1]);
  }

  cout << stoull(s) << endl;
}
//
//bool is_fine(long long n) {
//  string s = to_string(n);
//  int i = 1;
//  while(s[i - 1] >= s[i])
//    i++;
//  return i == s.size();
//}
//
//void make_cache(int n) {
//  for (int i = 0; i < n; ++i) {
//
//  }
//}

int main() {
  ifstream in("../in");
  cin.rdbuf(in.rdbuf());


  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cout << "Case #" << i +1  << ": ";
    problem();
  }

  return 0;
}