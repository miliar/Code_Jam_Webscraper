// Author: Xujie Si
// Email: six@gatech.edu
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
using namespace std;

#define FOR(i,X) for(int i=0;i<(X);++i)
#define PB(X) push_back( (X) )

typedef long long LL;
typedef vector<int> VI;

priority_queue<int> maxQ; // largest on the top
priority_queue<int, VI, greater<int> > minQ; // smallest on the top

auto cmp1 = [](int& a, int& b) -> bool {return a>b;};
auto dbg = ostream_iterator<int>(cerr, ",");

string insert(string& s, int K, char c) {
	string res = "";
	int len = s.length();
	int n = std::max(len, K);
	for(int i = 0; i < n; ++i) {
		if(i < K)
			res += c;
		if(i < len) {
			res += s[i];
		}
	}

	return res;
}

string eq(int K, char c1, char c2) {
	string res;
	for(int i=0;i<K;++i) {
		res += c1;
		res += c2;
	}
	return res;
}


string expand(int K, char rep, char target, string& s) {
	string res;

	for(int i=0; i < s.length(); ++i) {
		if(target == s[i]){
			res = s.substr(0, i);
			res += eq(K, target, rep);
			res += s.substr(i);
			return res;
		}
	}

	std::cerr << "error in expand: cannot find target!!! " << endl;
	return "error";
}


void solve(){
	// exact implementation appears here
	int n;
	int R, O, Y, G, B, V;
	cin >> n >> R >> O >> Y >> G >> B >> V;

	int sum = R + O + Y + G + B + V;

	if(B < O || R < G || Y < V) {
		puts("IMPOSSIBLE");
		return;
	}

	if(O && B == O) {
		if(sum != B + O) {
			puts("IMPOSSIBLE");
			return;
		}
		string s = eq(B, 'B', 'O');
		std::cout << s << endl;
		return;
	}

	if(G && G == R) {
		if(sum != R + G) {
			puts("IMPOSSIBLE");
			return;
		}
		string s = eq(R, 'R', 'G');
		std::cout << s << endl;
		return;
	}

	if(V && V == Y) {
		if(sum != Y + V) {
			puts("IMPOSSIBLE");
			return;
		}
		string s = eq(V, 'Y', 'V');
		std::cout << s << endl;
		return;
	}

	B -= O;
	Y -= V;
	R -= G;

	// R, Y, B
	
	if(R > Y + B || Y > R + B || B > R + Y) {
		puts("IMPOSSIBLE");
	}
	else{

		vector< pair<int,char> > v;
		v.PB( make_pair(R,'R') );
		v.PB( make_pair(Y,'Y') );
		v.PB( make_pair(B,'B') );
		sort(v.begin(), v.end());

		string s;
		//string s1 = insert(s, R, 'R');
		string s1 = insert(s, v[0].first, v[0].second);
		//std::cerr << "s1: " << s1 << endl;

		//string s2 = insert(s1, Y, 'Y');
		string s2 = insert(s1, v[1].first, v[1].second);
		//std::cerr << "s2: " << s2 << endl;
		// reverse s2
		std::reverse(s2.begin(), s2.end());
		//std::cerr << "reverse s2: " << s2 << endl;

		//string s3 = insert(s2, B, 'B');
		string s3 = insert(s2, v[2].first, v[2].second);


		string ans = s3;
		if(O > 0) {
			ans = expand(O,'O', 'B', ans);
		}
		if(G > 0) {
			ans = expand(G,'G', 'R', ans);
		}
		if(V > 0) {
			ans = expand(V,'V', 'Y', ans);
		}

		cout << ans << endl;
	}
}

int main()
{
  int cs = 0, T;
  scanf("%d",&T);
  while(++cs <= T){
    printf("Case #%d: ", cs);
    solve();
  }
  return 0;
}
