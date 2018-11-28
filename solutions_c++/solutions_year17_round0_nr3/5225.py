#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<queue>
#define ll long long
#define fo(i,x,y) for(int i=x;i<=y;i++)
using namespace std;
const char* fin="3.in";
const char* fout="3.out";
const int inf=0x7fffffff;
const int maxn=1000060;
int t,n,m;
struct node{
	int l,r,x,ls,rs,mx,mn;
	node(int _l=0,int _r=0){
		l=_l;r=_r;x=(l+r)/2;
		ls=x-l;rs=r-x;
		mx=max(ls,rs);mn=min(ls,rs);
	}
	bool operator <(const node &b)const{
		return mn<b.mn || mn==b.mn && mx<b.mx || mn==b.mn && mx==b.mx && x>b.x;
	}
};
int main(){
	freopen(fin,"r",stdin);
	freopen(fout,"w",stdout);
	scanf("%d",&t);
	fo(tt,1,t){
		scanf("%d%d",&n,&m);
		priority_queue<node> a;
		a.push(node(0,n+1));
		int ans1,ans2;
		fo(i,1,m){
			node tmp=a.top();
			a.pop();
			ans1=tmp.mx-1;
			ans2=tmp.mn-1;
			if (tmp.l<=tmp.x-2) a.push(node(tmp.l,tmp.x));
			if (tmp.x<=tmp.r-2) a.push(node(tmp.x,tmp.r));
		}
		printf("Case #%d: %d %d\n",tt,ans1,ans2);
	}
	return 0;
}