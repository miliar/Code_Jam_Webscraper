// In the name of Allah
// #Isart

#include<bits/stdc++.h>

#define pii pair<int, int>
#define pb push_back
#define F first
#define S second
#define ll long long
#define ld long double

using namespace std;

const int MAXN = 1e5 + 10;
ll po[30], a[MAXN];

inline ll calc(ll n){
	po[0] = 1;
	for(int i = 1; i < 20; i ++) po[i] = 1ll * po[i - 1] * 10;

	ll x = n, ptr = 0;
	while(x > 0){
		a[ptr ++] = x % 10;
		x /= 10;
	}

	reverse(a, a + ptr);
	int id = ptr - 1;
	for(int i = 0; i < ptr - 1; i ++){
		if(a[i] > a[i + 1]){
			id = i;
			break;
		}
	}
	
	ll ans = 0, now = 0;
	for(int i = 0; i <= id; i ++){
		int val = 0;
		if(i > 0) val = a[i - 1];
		for(int j = val; j < a[i]; j ++){
			ans = max(ans, now + j * po[ptr - i - 1] + po[ptr - i - 1] - 1);
		}
		now = now + a[i] * po[ptr - i - 1];
	}

	if(id == ptr - 1) ans = n;
	return ans;
}


int main(){
	ios::sync_with_stdio(false); cin.tie(0);
	ifstream fin("salam2.txt");
	ofstream fout("salam.txt");
	int t; fin >> t;
	for(int i = 0; i < t; i ++){
		ll n; fin >> n;
		fout << "Case #" << i + 1 << ": " << calc(n) << endl;
	}
	system("pause");
	return 0;	
}