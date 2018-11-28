#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iomanip>
#include<sstream>
#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<bitset>
#define fou(i,j,k) for (LL i=j;i<=k;i++)
#define fod(i,j,k) for (LL i=j;i>=k;i--)
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;

const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

struct node{
	LL l,r,len;
};

struct cmp{
	bool operator()(node i,node j){
		if (i.len==j.len) return i.l>j.l;
		else return i.len<j.len;
	}
};

priority_queue<node, vector<node>, cmp> q;
LL n,K;

void init(){
	scanf("%lld%lld",&n,&K);
}

void solve(){
	node now,A,B;
	LL mid;
	now.l=0;now.r=n+1;now.len=n;
	while (!q.empty()) q.pop();
	q.push(now);
	fou(i,1,K){
		now=q.top();
		q.pop();
		mid=(now.l+now.r)/2;
		A.l=now.l;A.r=mid;A.len=mid-now.l-1;
		B.l=mid;B.r=now.r;B.len=now.r-mid-1;
		q.push(A);
		q.push(B);
		if (i==K){
			printf("%lld %lld\n",max(A.len,B.len),min(A.len,B.len));
		}
	}
}

int main(){
	freopen("C-small-2-attempt3.in","r",stdin);
	freopen("C-small-2-attempt3.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
