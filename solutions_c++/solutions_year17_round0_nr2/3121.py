#include <iostream>
#include <string>

using namespace std;

// 1275999
int main() {
  int T;
  cin >> T;
  for (int c = 0; c < T; c++) {
    string s;
    cin >> s;
    int i, n = s.size();
    for (i = 0; i < n; i++) {
      if (i + 1 < n && s[i + 1] < s[i]) {
        while(i!=0 && s[i-1]==s[i]) i--;
        s[i]=s[i]-1;
        i++;
        for (;i<n;i++)s[i]='9';
        break;
      }
    }
    if (s[0] == '0') {
      s.erase(0, 1);
    }
    cout << "Case #" << c + 1 << ": " << s << endl;
  }
}
