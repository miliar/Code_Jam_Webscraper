#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#define inputt int t;cin>>t;
#define pi acos(-1.0)
#define lson o*2,l,m
#define rson o*2+1,m+1,r
#define INF 0x7f7f7f7f
#define lowbit(X) ((X)&(-X))
#define clr(X,Y) memset(X,Y,sizeof(X))
typedef long long ll;
using namespace std;
struct node{
	int maxlr,minlr;
	node(int a=0,int b=0){
		maxlr=max(a,b),minlr=min(a,b);
	}
	bool operator <(const node& a)const{
		if(minlr<a.minlr)return 1;
		else if(minlr==a.minlr&&maxlr<a.maxlr)return 1;
		else return 0;
	}
}p;
int main(){
	inputt
	int n,k;
	for(int cas=1;cas<=t;cas++){
		scanf("%d%d",&n,&k);
		k--;
		priority_queue<node>q;
		q.push(node((n-1)/2,n-1-(n-1)/2));
		while(k--){
			p=q.top();
			q.pop();
			//if(p.maxlr==0&&p.minlr==0)continue;
			if(p.maxlr>0)q.push(node((p.maxlr-1)/2,p.maxlr-1-(p.maxlr-1)/2));
			if(p.minlr>0)q.push(node((p.minlr-1)/2,p.minlr-1-(p.minlr-1)/2));
		}
		p=q.top();
		printf("Case #%d: %d %d\n",cas,p.maxlr,p.minlr);
	} 
	return 0;
}

