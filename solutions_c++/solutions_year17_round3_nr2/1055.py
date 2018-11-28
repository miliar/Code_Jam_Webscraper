// 2017  Round 1C Problem B
#include<algorithm>
#include<cmath>
#include<iostream>
#include<limits>
#include<utility>
#include<vector>

using namespace std;

// I/O

typedef pair<int, int> activity;

struct input {
  int Ac, Aj;
  vector<activity> vc;
  vector<activity> vj;
};

template<typename T0, typename T1>
istream& operator>>(istream& is, pair<T0, T1>& x) {
  is >> x.first >> x.second;
  return is;
}

template<typename T>
istream& operator>>(istream& is, vector<T>& x) {
  for(size_t i = 0; i < x.size(); ++i) is >> x[i];
  return is;
}

istream& operator>>(istream& is, input& in) {
  cin >> in.Ac >> in.Aj;
  in.vc.resize(in.Ac);
  in.vj.resize(in.Aj);
  cin >> in.vc >> in.vj;
  return is;
}

template<typename T0, typename T1>
ostream& operator<<(ostream& os, pair<T0, T1> const& x) {
  os << x.first << x.second;
  return os;
}

template<typename T>
ostream& operator<<(ostream& os, vector<T> const& x) {
  for(size_t i = 0; i < x.size(); ++i) os << x[i] << " ";
  return os;
}

// Algorithm

void solve(input const& in) {
  if (in.Ac + in.Aj == 1 || in.Ac == 1) {
    // change where the activity starts
    cout << "2"; return;
  }
  // one has 2 activities
  vector<activity> v = in.Ac == 2 ? in.vc : in.vj;
  sort(v.begin(), v.end());
  if (v[1].first - v[0].second >= 720 || 60*24+v[0].first-v[1].second >= 720) {
    cout << "2"; return;
  }
  cout << "4"; return;
}

int main() {
  int T = 0; cin >> T;
  for (int t = 0; t < T; ++t) {
    input in; cin >> in;
    cout << "Case #" << t+1 << ": ";
    solve(in);
    cout << endl;
  }
  return 0;
}
