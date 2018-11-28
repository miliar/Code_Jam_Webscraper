#include <bits/stdc++.h>
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define sqr(x) ((x)*(x))
#define fname ""

using namespace std;

typedef long long ll;
const double eps = 1e-9;
const double PI = acos(-1.0);
const int inf = (int) 1e9 + 7;
const ll INF = (ll) 1e18 + 7;
const int mod = (int) 1e9 + 7;
const int N = (int) 2e5 + 7;

int t;
string s;

void g(int pos) {
	s[pos] --;
	for(int i = pos + 1; i < s.size(); i ++)
		s[i] = '9';
}

void f() {
	for(int i = 1; i < s.size(); i ++) {
	 	if(s[i] < s[i - 1]) {
	 		if(i > 1 && s[i - 2] > s[i - 1])
	 			g(i - 1);
	 		else {
	 			while(i > 1 && s[i - 2] == s[i - 1])
	 				i --;
	 			g(i - 1);
	 		}
	 		return;
	 	}
	}
}

int main () {
   	//freopen(fname".in", "r", stdin);
   	freopen("output.txt", "w", stdout);
   	ios_base::sync_with_stdio(0);

   	cin >> t;
   	for(int i = 0; i < t; i ++) {
   	 	cin >> s;
   	 	f();
   	 	while(s[0] == '0')
   	 		s = s.substr(1);
   	 	cout << "Case #" << i + 1 << ": " << s << '\n';
   	}
   	return 0;
}   