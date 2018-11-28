#include <iostream>
#include <string>


using namespace std;
int main() {
  int t;
  cin >> t;

  for (int test=1;test<=t;test++) {
    cout << "Case #" << test << ": ";
    string s;
    int k, turns = 0;
    cin >> s >> k;

    for (int i=0;i<=s.length()-k;i++) {
      if (s[i] == '-') {
        for (int j=0;j<k;j++)
          s[i+j] = s[i+j] == '-' ? '+' : '-';
        turns++;
      }
    }

    if (s.find("-") != string::npos)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << turns << endl;
  }

  return 0;
}