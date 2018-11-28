#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<deque>

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

long long d, n, k[N], s[N];
double t[N];

void print(int t, double ans){
	printf("Case #%d: %.6lf\n",t+1,ans);
}

bool comp(int a, int b){
	return (k[a] > k[b]);
}

void solve(int test){
	cin >> d >> n;
	fi(0, n){
		cin >> k[i] >> s[i];
	}
	vector<int> p;
	fi(0, n) p.pb(i);
	sort(p.begin(), p.end(), comp);
	double maxi = 0;
	for(int i=n-1;i>=0;--i){
		maxi = max(maxi, (d * 1.0 - k[i]) / s[i]);
		t[i] = max(t[i], maxi);
	}
	
	double ans = d * 1.0 / maxi;
	print(test, ans);
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