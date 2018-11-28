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

string toStr(ll v){
	string ret = "";
	while(v){
		ret += (char)(v%10 + '0');
		v /= 10;
	}
	reverse(ret.begin(), ret.end());
	return ret;
}

bool check(string &s){
	fi(0, sz(s) - 1){
		if(s[i] > s[i+1]){
			--s[i];
			fj(i+1, sz(s)) s[j] = '9';
			reverse(s.begin(), s.end());
			while(s.size() && s.back() == '0') s.pop_back();
			reverse(s.begin(), s.end());
			return false;
		}
	}
	return true;
}

void solve(int test){
	ll n;
	cin >> n;
	string ans = toStr(n);
	while(!check(ans)){
		
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