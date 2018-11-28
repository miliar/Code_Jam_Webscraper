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
#include<cmath>
#define fou(i,j,k) for (int i=j;i<=k;i++)
#define fod(i,j,k) for (int i=j;i>=k;i--)
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;

const int maxn=1010;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;
const long double pi=acos(-1.0);

struct node{
	int r,h;
	long double c;
}a[maxn],b[maxn];

int n,K;

void init(){
	scanf("%d%d",&n,&K);
	fou(i,1,n){
		scanf("%d%d",&a[i].r,&a[i].h);
		a[i].c=2.0*pi*a[i].r*a[i].h;
	}
}

bool cmp(node i,node j){
	if (i.r==j.r) return i.h>j.h;
	else return i.r>j.r;
}

void find(node *a,int l,int r,int K){
	int i,j;
	node tmp;
	i=l;j=r;
	swap(a[l],a[(l+r)/2]);
	tmp=a[l];
	while (i<j){
		while (a[j].c<tmp.c && i<j) j--;
		if (i<j) {a[i]=a[j];i++;}
		while (a[i].c>tmp.c && i<j) i++;
		if (i<j) {a[j]=a[i];j--;}
	}
	a[i]=tmp;
	if (i==K) return;
	i++;j--;
	if (l<=j && K<=j) find(a,l,j,K);
	if (i<=r && i<=K) find(a,i,r,K);
}

void solve(){
	long double ans,now;
	int tot;
	sort(a+1,a+n+1,cmp);
	ans=0;
	fou(i,1,n-K+1){
		tot=0;
		fou(j,i+1,n) b[++tot]=a[j];
		find(b,1,tot,K-1);
		now=pi*a[i].r*a[i].r+a[i].c;
		fou(j,1,K-1) now+=b[j].c;
		if (ans<now) ans=now;
	}
	printf("%.9lf\n",ans);
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
