#include<iostream>
#include<algorithm>
#include<string>

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

void solve(int test){
	string s;
	cin >> s;
	int k;
	cin >> k;
	int ans = 0;
	fi(0, sz(s)){
		if(s[i] == '-'){
			++ans;
			fj(0, k) s[i+j] = (s[i+j] == '-' ? '+' : '-'); 
		}
		if(i + k == s.size()) break;
	}
	fi(0, sz(s)) if(s[i] != '+'){
		cout << "Case #" << test + 1 << ": IMPOSSIBLE" << endl;
		return;
	}
	cout << "Case #" << test + 1 << ": " << ans << endl;
}

int main(){
#ifdef _DEBUG
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif

	int test;
	cin >> test;
	fi(0, test){
		solve(i);
	}

	return 0;
}