#include <algorithm>
#include <bitset>
#include <cassert>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <math.h>
#include <memory>
#include <queue>
#include <sstream>
#include <stdio.h>
#include <string>
#include <vector>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define POW(n) ((n) * (n))
#define ALL(a) (a).begin(), (a).end()
#define dump(v) (cerr << #v << ": " << v << endl)
// #define cerr                                                                   \
//   if (true)                                                                    \
//   cerr

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<unsigned long long> vull;

int T;
ll S;

// ll n = to_T<ll>("114514")
template <class T> T to_T(const string &s) {
	istringstream is(s);
	T res;
	is >> res;
	return res;
}
template <class T> string to_s(const T &a) {
	ostringstream os;
	os << a;
	return os.str();
}

// string solve(string S) {
// 	string ans = "";
//
//   if(S.size() == 0)return  ans;
//   string str;
//   std::vector<char>  v;
//   REP(i,S.size()) v.push_back(S[i]);
//   sort(ALL(v));
//
//   REP(i,S.size()){
//     ans += v[0];
//     if(S[i] == v[0]){
//       str = S.substr(i+1,S.size());
//       dump(S);
//       dump(str);
//       dump(v[0]);
//       break;
//     }
//   }
//
//   return ans+solve(str);
// }

ll pow(ll base,ll p){
  ll ret = 1;

  REP(i,p){
    ret *= base;
  }

  return ret;
}

bool chk(string S){
  REP(i,S.size()-1){
    if(S[i] > S[i+1])return false;
  }
  return true;
}

string solve(string S) {
  if(chk(S))return S;

  for(int i=1;i<S.size();i++){
    if(S[i] < S[i-1] || S[i] == '0'){
      ll n = S[i] - '0' + 1;
      n *= pow(10,S.size() - i - 1);
      ll N = to_T<ll>(S);
      N -= n;
      S = to_s(N);
      for(int j=i;j<S.size();j++){
        S[j] = '9';
      }
      // dump(n);
      // dump(N);
      break;
    }
  }

  return solve(S);
}

int main() {
	ios::sync_with_stdio(false);
	cin >> T;

	REP(t, T){
		cin >> S;
    string s = to_s(S);
		string ans = solve(s);
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}

	return 0;
}
