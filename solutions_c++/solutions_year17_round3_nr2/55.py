#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
struct data{
	int l,r,v;
}a[5101];
int ans,t1,t2,i,j,k,n,m,tests,tc,p[21001],q[21001];
bool cmp(data x,data y){
	return x.l<y.l;
}
int main(){
	for (scanf("%d",&tests),tc=1;tc<=tests;tc++){
		scanf("%d%d",&n,&m);t1=t2=720;
		for (i=1;i<=n;i++) scanf("%d%d",&a[i].l,&a[i].r),a[i].v=0,t2-=a[i].r-a[i].l;
		for (i=1;i<=m;i++) scanf("%d%d",&a[i+n].l,&a[i+n].r),a[i+n].v=1,t1-=a[i+n].r-a[i+n].l;
		if (n+m==1){
			printf("Case #%d: 2\n",tc);continue;
		}
		ans=p[0]=q[0]=0;
		sort(a+1,a+1+n+m,cmp);
		for (i=2;i<=n+m;i++)
		 if (a[i-1].v==a[i].v){
		 	if (a[i].v==0) p[++p[0]]=a[i].l-a[i-1].r;else q[++q[0]]=a[i].l-a[i-1].r;
		 	ans+=2;
		 }else ans++;
		if (a[1].v==a[n+m].v){
			if (a[1].v==0) p[++p[0]]=a[1].l+1440-a[n+m].r;else q[++q[0]]=a[1].l+1440-a[n+m].r;
			ans+=2;
		}else ans++;
		if (p[0]>1) sort(p+1,p+1+p[0]);
		if (q[0]>1) sort(q+1,q+1+q[0]);
		for (i=1;i<=p[0];i++){
			if (p[i]>t2) break;
			ans-=2;t2-=p[i];
		}
		for (i=1;i<=q[0];i++){
			if (q[i]>t1) break;
			ans-=2;t1-=q[i];
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}
