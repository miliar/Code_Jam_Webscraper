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
#define fou(i,j,k) for (int i=j;i<=k;i++)
#define fod(i,j,k) for (int i=j;i>=k;i--)
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;

const int maxn=300;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

struct node{
	int x,y,c;
}a[maxn];

struct node2{
	int c,d;
};

struct cmp{
	bool operator()(node2 i,node2 j){
		if (i.d==j.d) return i.c>j.c;
		else return i.d>j.d;
	}
};

priority_queue<node2, vector<node2>, cmp> q;

int n,m,N,sum[5];

void init(){
	scanf("%d%d",&n,&m);
	sum[0]=sum[1]=0;
	fou(i,1,n){
		scanf("%d%d",&a[i].x,&a[i].y);
		a[i].c=0;
		sum[0]+=a[i].y-a[i].x;
	}
	fou(i,1,m){
		scanf("%d%d",&a[i+n].x,&a[i+n].y);
		a[i+n].c=1;
		sum[1]+=a[i+n].y-a[i+n].x;
	}
	N=n+m;
}

bool cmp(node i,node j){
	return i.x<j.x;
}

void solve(){
	int ans=0;
	node2 tmp;
	sort(a+1,a+N+1,cmp);
	if (a[1].c==1){
		fou(i,1,N) a[i].c^=1;
		swap(n,m);
		swap(sum[0],sum[1]);
	}
	while (!q.empty()) q.pop();
	ans=n*2+m*2;
	fou(i,2,N){
		if (a[i].c==a[i-1].c){
			tmp.c=a[i].c;
			tmp.d=a[i].x-a[i-1].y;
			q.push(tmp);
		}else ans--;
	}
	if (a[1].c==a[N].c){
		tmp.c=a[1].c;
		tmp.d=a[1].x-a[N].y+1440;
		q.push(tmp);
	}else ans--;

	if (N==1) ans=2; else
	if (N==2){
		if (n==1) ans=2;
		else if (a[2].y-a[1].x<=720 || a[1].y-a[2].x+1440<=720) ans=2;
		else ans=4;
	}else
	{
		while (!q.empty()){
			tmp=q.top();
			q.pop();
			if (sum[tmp.c]+tmp.d<=720){
				sum[tmp.c]+=tmp.d;
				ans-=2;
			}
		}
	}
	printf("%d\n",ans);
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
