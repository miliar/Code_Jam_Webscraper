#include <bits/stdc++.h>
#define M 1000
using namespace std;

struct Ticket{
	int p,b;
	bool operator<(const Ticket &r)const{return p>r.p;}
} a[M+1];
int n,m,c,mx,ans;
int cnt[M+1];

void input(void){
	int i;
	scanf("%d %d %d",&n,&c,&m);
	for(i=1;i<=n;i++) cnt[i]=0;
	mx=0;
	for(i=1;i<=m;i++){
		scanf("%d %d",&a[i].p,&a[i].b);
		cnt[a[i].b]++;
		if(mx<cnt[a[i].b]) mx=cnt[a[i].b];
	}
	sort(a+1,a+m+1);
}

bool check(int l){
    int i,j,cn=0;
    ans=0;
	for(i=1;i<=n;i++) cnt[i]=0;
    for(i=n,j=1;i>=1;i--){
		while(cnt[i]<l && j<=m && a[j].p==i){
			cnt[i]++;
			j++;
		}
		while(j<=m && a[j].p==i){
			cn++;
			ans++;
			j++;
		}
		cn=max(0,cn-(l-cnt[i]));
    }
    return !cn;
}

void process(void){
	int s,e,md;
	for(s=mx,e=m;s<e;check(md=(s+e)/2) ? e=md : s=md+1);
	check(s);
	printf("%d %d\n",s,ans);
}

int main(){
	freopen("input.txt","r",stdin);

	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		input();
		process();
	}

	return 0;
}
