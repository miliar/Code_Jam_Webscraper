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
#define inp "input.in"
using namespace std;

char N[20];
int L;
int dp[20][2][128];
int nxt[20][2][128];

int solve(int pos,bool eq,char lst){
	if(lst > '9') return 0;
	if(pos == L) return 1;
	if(dp[pos][eq][lst] != -1) return dp[pos][eq][lst];
	int & adv = nxt[pos][eq][lst];
	int & ret = dp[pos][eq][lst];
	if(!eq){
		if(solve(pos,0,lst + 1)) {
			adv = 4;
			ret = 1;
		}
		else {
			adv = 1;
			ret = solve(pos + 1,0,lst);
		}
	}
	else{
		if(lst > N[pos]) return ret = 0;
		if(solve(pos,1,lst + 1)){
			adv = 6;
			ret = 1;
		}
		else {
			adv = 1;
			if(lst == N[pos]) adv = 3;
			ret = solve(pos + 1,lst == N[pos],lst);
		}
	}
	return ret;
}

int main(){
	//freopen("logger.out","w",stderr);
	#ifndef ONLINE_JUDGE
	//	freopen(inp, "r", stdin);
	//	freopen("output.out", "w", stdout);
	#endif
	int T; scanf("%d",&T);
	for(int t = 1;t <= T;t++){
		scanf("%s",N);
		L = strlen(N);
		memset(dp,-1,sizeof dp);
		assert(solve(0,1,'0'));
		char lst = '0';
		int pos = 0,eq = 1;
		string out ;
		for(;pos < L;){
			int adv = nxt[pos][eq][lst];
			if(adv & 1) {
				out = lst + out;
				pos ++;
			}
			if(adv & 2) eq = 1;
			else eq = 0;
			if(adv & 4) lst++;
		}
		while(!out.empty() && out.back() == '0') out.pop_back();
		if(out.empty()) out = "0";
		sort(all(out));
		printf("Case #%d: %s\n",t,out.c_str());
	}
	return 0;
}
