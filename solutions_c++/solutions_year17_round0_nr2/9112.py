#include <bits/stdc++.h>

using namespace std;

string s;
int n;
string ans;
int check;
int id;
int num;

void sol() {
  cin >> s;
  n = s.size();
  ans = "";
  id = -1;

  if(n == 1) {
    cout << s << '\n';
    return;
  }

  check = 1;
  for(int i = 0; i < n - 1; i++) {
    if(s[i] > s[i + 1]) {
      check = 0;
      break;
    }
  }
  if(check) {
    cout << s << '\n';
    return;
  }

  for(int i = 0; i < n - 1; i++) {
    if(s[i] > s[i + 1]) {
      id = i;
      break;
    }
  }
  for(int i = id - 1; i >= 0; i--) {
    if(s[i] == s[i + 1]) {
      id = i;
    }
    else {
      break;
    }
  }

  num = stoi(s.substr(0, id + 1));
  num--;
  if(num > 0) {
    cout << num;
  }
  for(int i = 1; i <= n - (id + 1); i++)
    cout << 9;
  cout << '\n';

}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    sol();
  }

  return 0;
}
