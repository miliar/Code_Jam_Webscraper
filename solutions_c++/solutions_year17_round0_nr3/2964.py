#include <bits/stdc++.h>

#define rep2(x,fr,to) for(int (x)=(fr);(x)<(to);(x)++)
#define rep(x,to) for(int (x)=0;(x)<(to);(x)++)
#define repr(x,fr,to) for(int (x)=(fr);(x)>=(to);(x)--)
#define all(c) (c).begin(),(c).end()
#define sz(v) (int)(v).size()

using namespace std;
typedef long long ll; typedef vector<int> VI; typedef pair<int,int> pii;
const ll mod = 1e9+7;

vector<ll> lv;
void init(){
	rep(i,62) lv.emplace_back(1LL<<i);
}

void fnc00(int qt, ll n, ll k){
	if(n<1002){
		vector<int> v(n+2);
		v[0]=v[n+1]=1;
		priority_queue<pii> q;
		q.push(pii(n, 0) );
		
		rep(i,k-1){
			int len, ps;
			tie(len, ps) =q.top();
			q.pop();
			int w = (len-1)/2;
			if(w>0) q.push(pii(w, ps));
			if(len-1-w>0) q.push(pii(len-1-w, ps-w-1));
			v[-ps+w+1] = 1;
			//printf("%d:%d::%d:%d  ", w,ps,len-1-w,ps-w-1);
		}
		
		ll w = q.top().first;
		ll ans1 = w/2, ans2 = (w-1)-ans1;

		if(q.empty()) printf("Case #%d: 0 0\n", qt+1);
		else printf("Case #%d: %lld %lld\n", qt+1, ans1, ans2);
		//rep(i,n+2) if(v[i]) printf("%d ",i);
		return;
	}
	
	
	if(k==1){
		ll bb = (n-1)/2;
		printf("Case #%d: %lld %lld\n", qt+1, bb+(n-1)%2, bb);
		return;
	}
	int ci = lower_bound(all(lv), k) - lv.begin();
	if(lv[ci] !=k) ci--;
	
	ll slen = (n -(lv[ci]-1))/ lv[ci];
	ll smd = n -(lv[ci]-1)- slen*lv[ci]; 
	ll zan = k - lv[ci];
	//printf("slen=%lld smd=%lld zan=%lld\n", slen,smd,zan);
	ll ans=-1;
	if(smd >0 && smd > zan) slen++;
	printf("Case #%d: %lld %lld\n", qt+1, (slen-1)/2+(slen-1)%2, (slen-1)/2);
	
	
}


int main()
{
	//cin.tie(0); ios_base::sync_with_stdio(false);
	init();
	int t; cin >> t;
	rep(qt,t){
		ll n,k;
		cin >> n >> k;
		fnc00(qt, n, k);
	}
	
	return 0;
}

/*
1000000 475713
500000 237857
999999 475712
*/