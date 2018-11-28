#include <bits/stdc++.h>

#define rep2(x,fr,to) for(int (x)=(fr);(x)<(to);(x)++)
#define rep(x,to) for(int (x)=0;(x)<(to);(x)++)
#define repr(x,fr,to) for(int (x)=(fr);(x)>=(to);(x)--)
#define all(c) (c).begin(),(c).end()
#define sz(v) (int)(v).size()

using namespace std;
typedef long long ll; typedef vector<int> VI; typedef pair<int,int> pii;
const ll mod = 1e9+7;

void fnc00(int qt, ll n){
	if(n<10000){
		ll ans =0LL;
		for(ll i=n; i>=1; i--){
			int lmn=99, ng=0;
			for(ll w = i;w>0;w/=10){
				if(lmn < w%10){ ng=1; break;}
				lmn = w%10;
			}
			if(!ng){ ans = i; break;}
		}
		printf("Case #%d: %lld\n", qt+1, ans);
		return;
	}
	
	string s=to_string(n);
	int m=sz(s);
	VI kt(m);
	rep(i,m) kt[i] = s[i] - '0';
	int imn=m;
	repr(i,m-1,1){
		if(kt[i] < kt[i-1]){
			kt[i-1]--;
			imn = i;
		}
	}
	rep2(j,imn,m) kt[j]=9;
	ll rt=0LL;
	rep(i,m) rt = rt * 10 + kt[i];

	printf("Case #%d: %lld\n", qt+1, rt);
	
}


int main()
{
	//cin.tie(0); ios_base::sync_with_stdio(false);
	int t; cin >> t;
	rep(qt,t){
		ll n;
		cin >> n;
		fnc00(qt, n);
	}
	
	return 0;
}