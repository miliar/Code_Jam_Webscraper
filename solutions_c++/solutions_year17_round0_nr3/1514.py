#include <bits/stdc++.h>
#define loop(i,n) for(int i = 0;i < (n);i++)
#define range(i,a,b) for(int i = (a);i <= (b);i++)
#define all(A) A.begin(),A.end()
#define pb push_back
#define mp make_pair
#define sz(A) ((int)A.size())
#define vi vector<int>
#define vl vector<long long>
#define vd vector<double>
#define vp vector<pair<int,int> >
#define ll long long
#define pi pair<int,int>
#define pl pair<ll,ll>
#define popcnt(x) __builtin_popcount(x)
#define LSOne(x) ((x) & (-(x)))
#define xx first
#define yy second
#define PQ priority_queue
#define print(A,t) cerr << #A << ": "; copy(all(A),ostream_iterator<t>(cerr," " )); cerr << endl
#define prp(p) cerr << "(" << (p).first << " ," << (p).second << ")";
#define prArr(A,n,t)  cerr << #A << ": "; copy(A,A + n,ostream_iterator<t>(cerr," " )); cerr << endl
#define PRESTDIO() cin.tie(0),cerr.tie(0),ios_base::sync_with_stdio(0)
#define what_is(x) cerr << #x << " is " << x << endl
#define bit_lg(x) (assert(x > 0),__builtin_ffsll(x) - 1)
const double PI = acos(-1);
using namespace std;



pl solve(ll N,ll K){
	map<ll,ll> cnt;
	cnt[N] = 1;

	while(K){
		ll len = cnt.rbegin()->xx,ctr = cnt.rbegin()->yy;
		ll lft = (len - 1)/2,rght = len/2;
		if(ctr >= K) return mp(rght,lft);
		K -= ctr;
		cnt[lft] += ctr;
		cnt[rght] += ctr;
		cnt.erase(len);
	}
	assert(0);
}

int main(){
	/*freopen("logger.out","w",stderr);
	#ifndef ONLINE_JUDGE
		freopen("input.in", "r", stdin);
		freopen("output.out", "w", stdout);
	#endif
	*/

	int T; scanf("%d",&T);
	range(t,1,T){
		cerr << "processing case#" << t << endl;
		ll N,K; scanf("%lld %lld",&N,&K);
		pl ans = solve(N,K);
		printf("Case #%d: %lld %lld\n",t,ans.xx,ans.yy);
	}
	return 0;
}
