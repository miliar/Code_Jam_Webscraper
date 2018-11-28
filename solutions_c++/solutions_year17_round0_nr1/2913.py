#include <bits/stdc++.h>

#define rep2(x,fr,to) for(int (x)=(fr);(x)<(to);(x)++)
#define rep(x,to) for(int (x)=0;(x)<(to);(x)++)
#define repr(x,fr,to) for(int (x)=(fr);(x)>=(to);(x)--)
#define all(c) (c).begin(),(c).end()
#define sz(v) (int)(v).size()

using namespace std;
typedef long long ll; typedef vector<int> VI; typedef pair<int,int> pii;
const ll mod = 1e9+7;

void fnc00(int qt, string s, int k){
	int n=sz(s);
	vector<char> v(n, 0);
	rep(i,n) if(s[i]=='+') v[i]=1;
	int ans =0;
	rep(i,n-k+1){
		if(v[i]==0){
			rep(j,k) v[i+j] ^= 1;
			ans++;
		}
	}
	if(count(all(v),1) !=n) printf("Case #%d: IMPOSSIBLE\n", qt+1);
	else printf("Case #%d: %d\n", qt+1, ans);

}

void fnc10(int qt, string s, int k){
	int n=sz(s);
	vector<char> v(n, 0);
	rep(i,n) if(s[i]=='+') v[i]=1;
	int ans =0;
	repr(i,n-1,k-1){
		if(v[i]==0){
			rep(j,k) v[i-j] ^= 1;
			ans++;
		}
	}
	if(count(all(v),1) !=n) printf("Case #%d: IMPOSSIBLE\n", qt+1);
	else printf("Case #%d: %d\n", qt+1, ans);

}

int main()
{
	//cin.tie(0); ios_base::sync_with_stdio(false);
	int t; cin >> t;
	rep(qt,t){
		int k; string s;
		cin >>s  >>k;
		fnc00(qt, s, k);
		//fnc10(qt, s, k);
	}
	
	return 0;
}