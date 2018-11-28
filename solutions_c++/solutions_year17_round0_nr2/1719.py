#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int, int> pi;
const int mod = 1e9 + 7;
const double EPS = 1e-9;
const int INF = 1 << 29;
#define mp make_pair
#define el putchar('\n')
#define sp putchar(' ')
#define Fill(a,val) memset(a,val,sizeof a)
#define all(a) a.begin(),a.end()
#ifndef ONLINE_JUDGE
#define tr(a, it) for (decltype(a.begin()) it = a.begin(); it != a.end(); ++it)
#else
#define tr(a, it) for (typeof(a.begin()) it = a.begin(); it != a.end(); ++it)
#endif
#define in(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define out(n) printf("%d",n);
#define outl(n) printf("%lld",n);

string f(string s){
	int n = s.length();
	for (int i = 0; i + 1 < n; ++i){
		if (s[i] > s[i + 1]){			
			string ret;
			if (s[i] == '1'){
				for (int j = 1; j < n; ++j)ret += '9';
			}
			else{
				bool done = false;
				for (int j = 0; j <= i; ++j){
					if (s[j] == s[i])ret += (done ? '9' : (s[j] - 1)), done = true;
					else ret += s[j];
				}
				for (int j = i + 1; j < n; ++j)ret += '9';
			}
			return ret;
		}
	}
	return s;
}

int tn(string s){
	int ret = 0;
	for (int i = 0; i < s.length(); ++i){
		ret = ret * 10 + s[i] - '0';
	}
	return ret;
}

string ts(int n){
	string ret;
	while (n){
		ret += n % 10 + '0'; n /= 10;
	}
	reverse(all(ret)); return ret;
}

bool ok(string s){
	for (int i = 0; i + 1 < s.length(); ++i){
		if (s[i] > s[i + 1])return false;
	}
	return true;
}

string g(string s){
	int n = tn(s);
	while (n >= 1){
		string ss = ts(n);
		if (ok(ss))return ss;
		--n;
	}
	return "1";
}

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int t; in(t);
	for (int cs = 1; cs <= t; ++cs){
		string s; cin >> s;
		printf("Case #%d: ", cs); cout << f(s); el;
		//if (f(s) != g(s))cout << "shit in case " << cs; el;
	}
	return 0;
}