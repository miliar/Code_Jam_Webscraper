#include <bits/stdc++.h>
using namespace std;
const int oo = 0x3f3f3f3f;
const long long ooo = 0x3f3f3f3f3f3f3f3fll;
template<class T> T abs(T x) { return x > 0 ? x : -x;}
template<class T>  inline T sqr(T x) {return x*x; }
template<class T>  T lcm(T a, T b){return b*a/__gcd(a, b);}
#define fi first
#define se second
#define mk make_pair
#define pb push_back
#define rep(i, a, n) for(int i=a; i <n; ++i)
#define per(i, a, n) for(int i=n-1; i>=a; --i)
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define uniq(c) (c).resize(unique(all(c)) - (c).begin())
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<vector<ll> >matrix;
vector<string>v;
void gen(string s){
	if(sz(s) == 0){
		for(int i = '1'; i <= '9'; ++i){
		  string ss;
		  ss.pb((char)i);
		  gen(s + ss);
		}
	}else{
		v.push_back(s);
		if(sz(s) == 18)return;
		for(int i = s[sz(s)-1]; i <= '9'; ++i){
		  string ss;
		  ss.push_back((char)i);
		  gen(s + ss);
		}
	}
}
bool mycomp(string &s1, string &s2){
	if(sz(s1) != sz(s2))return sz(s1) < sz(s2);
	return s1 < s2;
}
int main() {
  string s = "";  
  gen(s);
  sort(all(v), mycomp);
  int tc;
  scanf("%d", &tc);
  getchar();
  for(int i = 1; i <= tc; ++i){
	cin >> s;
	printf("Case #%d: ", i);
	int lf = 0;
	int rg = sz(v)-1;
	int ans  = 0;
	while(lf <= rg){
		int mid = (lf + rg)/2;
		if(sz(v[mid]) > sz(s)){
			rg = mid-1;
		}else if((sz(v[mid]) == sz(s)) && v[mid] > s){
			rg = mid-1;
		}else{
			ans = mid;
			lf = mid+1;
		}
	}
	cout << v[ans] << endl;
  }
  return 0;
}
