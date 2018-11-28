#include <cstdio>
#include <map>
#include <queue>
#include <set>

#define LL long long

using namespace std;

LL n,k;
queue<LL> que;
map<LL,LL> cnt;
map<LL,bool> inQue;

struct Number{
	LL x;
	LL cnt;
	Number(){}
	Number(LL x0,LL c0){
		x=x0;
		cnt=c0;
	}
	bool operator < (const Number &b) const{
		return x>b.x;
	}
};
set<Number> sot;


inline void solve(int T){
	while(!que.empty()) que.pop();
	cnt.clear();
	sot.clear();
	inQue.clear();

	scanf("%lld%lld",&n,&k);
	k--;
	//printf("=> %lld %lld\n",n,k);

	cnt[n]=1;
	que.push(n);
	inQue[n]=true;

	while(!que.empty()){
		LL now=que.front();que.pop();

		cnt[now/2LL]+=cnt[now];
		cnt[(now-1LL)/2LL]+=cnt[now];

		if (!inQue[now/2LL]){
			inQue[now/2LL]=true;
			que.push(now/2LL);
		}

		if (!inQue[(now-1LL)/2LL]){
			inQue[(now-1LL)/2LL]=true;
			que.push((now-1LL)/2LL);
		}
	}

	for (map<LL,LL>::iterator it=cnt.begin();it!=cnt.end();it++) sot.insert(Number(it->first,it->second));

	LL AnsUnachieve=-1LL;
	for (set<Number>::iterator it=sot.begin();it!=sot.end();it++){
		if (AnsUnachieve==-1LL && k<(it->cnt)) AnsUnachieve=it->x;
		k-=(it->cnt);
	}
	
	printf("Case #%d: %lld %lld\n",T,AnsUnachieve/2LL,(AnsUnachieve-1LL)/2LL);
}

int main(){
	freopen("C-large.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T=0;
	scanf("%d",&T);
	for (int i=1;i<=T;i++) solve(i);
	return 0;
}