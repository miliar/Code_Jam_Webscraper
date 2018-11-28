#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<deque>
#include<set>

using namespace std;

#define sz(x) (int)(x.size())
#define fi(a, b) for(int i=a;i<b;++i)
#define fj(a, b) for(int j=a;j<b;++j)
#define fk(a, b) for(int k=a;k<b;++k)
#define mp make_pair
#define pb push_back
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

///////////////

int const N = 1e3 + 41;
ll const INF = (1e9 * 1LL * 1e9);

char ans[N];
int n;

void clear(){
	fi(0, N) ans[i] = '.';
}

void print(int t, string s){
	printf("Case #%d: ",t+1);
	cout << s << endl;
}

void add(int &a, int b){
	a += b;
	a %= n;
}

int getPos(pair<int, char> ps, int sp){
	int ret = sp;
	while(ps.first > 0){
		--ps.first;
		if(ans[ret] == '.'){
		}else{
			while(true){
				add(ret, 1);
				if(ans[ret] == '.') break;
			}
		}
		ans[ret] = ps.second;
		add(ret, 2);
	}
	return ret;
}

void solve(int test){
	clear();
	//N, R, O, Y, G, B, and V.
	int N, R, O, Y, G, B, V;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	n = R + O + Y + G + B + V;
	vector<pair<int, char> > a;
	a.pb(mp(R, 'R'));
	a.pb(mp(B, 'B'));
	a.pb(mp(Y, 'Y'));
	sort(a.begin(), a.end());
	if(n % 2 == 1){
		if((n + 1) / 2 <= a.back().first){
			print(test, "IMPOSSIBLE");
			return;
		}
	}else{
		if(n / 2 + 1 <= a.back().first){
			print(test, "IMPOSSIBLE");
			return;
		}
	}


	int p = 0;
	for(int i=2;i>=0;--i){
		p = getPos(a[i], p);
	}
	string s;
	fi(0, n) s.pb(ans[i]);
	print(test, s);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int test;
	cin >> test;
	for(int t=0;t<test;++t){
		solve(t);
	}

	return 0;
}