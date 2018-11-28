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
using namespace std;

struct node{
	int Hd,Ad,Hk,Ak;
public :
	bool operator < (const node & o) const {
		return tie(Hd,Ad,Hk,Ak) < tie(o.Hd,o.Ad,o.Hk,o.Ak);
	}
	void move1(){
		Hk = max(Hk - Ad,0);
		if(Hk) Hd = max(Hd - Ak,0);
	}
	void move2(int B){
		Ad += B;
		if(Hk) Hd = max(Hd - Ak,0);
	}
	void move3(int O){
		Hd = O;
		if(Hk) Hd = max(Hd - Ak,0);
	}
	void move4(int D){
		Ak = max(Ak - D,0);
		if(Hk) Hd = max(Hd - Ak,0);
	}
	friend ostream& operator << (ostream & st,const node & t) {
		st << "(" << t.Hd << " ," << t.Ad << " ," << t.Hk << " ," << t.Ak << ")";
		return st;
	}
};

int solve(int Hd,int Ad,int Hk,int Ak,int B,int D){
	auto root = node({Hd,Ad,Hk,Ak});
	queue<node> q;
	q.push(root);
	set<node> vis;
	vis.insert(root);

	for(int d = 0;!q.empty();d++){
		for(int i = 0,L = q.size();i < L;i++){
			auto cur = q.front(); q.pop();
		//	cerr << cur << endl;
			if(cur.Hd == 0) continue;
			if(cur.Hk == 0) return d;
			auto nxt = cur;
			nxt.move1();
			if(vis.find(nxt) == vis.end()) q.push(nxt),vis.insert(nxt);
			nxt = cur;
			nxt.move2(B);
			if(vis.find(nxt) == vis.end()) q.push(nxt),vis.insert(nxt);
			nxt = cur;
			nxt.move3(Hd);
			if(vis.find(nxt) == vis.end()) q.push(nxt),vis.insert(nxt);
			nxt = cur;
			nxt.move4(D);
			if(vis.find(nxt) == vis.end()) q.push(nxt),vis.insert(nxt);
		}
	}
	return -1;
}

int main(){
	#ifndef ONLINE_JUDGE
	//	freopen("input.in", "r", stdin);
	//	freopen("output.out", "w", stdout);
	#endif
	int T; scanf("%d",&T);
	range(t,1,T){
		cerr << "processing " << t << endl;
		int Hd,Ad,Hk,Ak,B,D;
		scanf("%d %d %d %d %d %d",&Hd,&Ad,&Hk,&Ak,&B,&D);
		int ans = solve(Hd,Ad,Hk,Ak,B,D);
		printf("Case #%d: ",t);
		if(ans == -1) puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	return 0;
}
