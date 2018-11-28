#include <bits/stdc++.h>

using namespace std;

#define ll long long int

vector< vector<ll> > pos;

string tidy(string s) {
  /*ll size = 9;
  int dig = 1;
  while (size < n) {
    dig++;
    for (int i = 1; i <= 9; i++) {
      size += pos[dig][i];
    }
    cout << size << "\n";
  }*/
  int n = s.size();
  reverse(s.begin(), s.end());
  vector<int> td(n, 0);
  int spos = 0;
  while (spos < n - 1) {
    if (s[spos] >= s[spos + 1]) {
      spos++;
    } else {
      for (int dig = 0; dig <= spos; dig++) {
	s[dig] = '9';
      }
      s[spos + 1]--;
      spos++;
    }
  }

  reverse(s.begin(), s.end());
  
  string res;
  int i = 0;
  while (s[i] == '0') {
    i++;
  }
  while (i < s.size()) {
    res.push_back(s[i]);
    i++;
  }
  

  return res;
}

void input() {
  //freopen("in.txt", "r", stdin);
  //freopen("out.txt", "w", stdout);
}

void calculate() {
  /*pos.assign(20, vector<ll>(10, 0));
  for (int i = 1; i <= 9; i++) {
    pos[1][i] = 1;
  }
  for (int position = 2; position < 20; position++) {
    for (int i = 1; i <= 9; i++) {
      ll sum = 0;
      for (int j = i; j <= 9; j++) {
	sum += pos[position - 1][j];
      }
      pos[position][i] = sum;
    }
  }

  for (int i = 1; i < 10; i++) {
    cout << "Digits: " << i << "\n";
    for (int d = 1; d <= 9; d++) {
      cout << pos[i][d] << " ";
    }
    cout << "\n";
  }*/
  
  int t;
  cin >> t;
  for (int cs = 0; cs < t; cs++) {
    string n;
    cin >> n;
    cout << "Case #" << (cs + 1) << ": " << tidy(n) << "\n";
  }
}

void output() {

}

int main() {
  input();
  calculate();
  output();
  return 0;
}
