#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#define fo(i,a,b) for(i=a;i<=b;i++)
#define fod(i,a,b) for(i=a;i>=b;i--)
using namespace std;
typedef long long ll;
const int maxn=20;
ll i,j,k,l,t,n,m,ans,cas,r,ci,c,z,l1,l2,r1,r2,ge1,ge2,num;
bool bz;
struct node{
    ll a,b,l,r;
}a[5];
bool cmp(node x,node y){return x.a<y.a;}
int main(){
//	freopen("fan.in","r",stdin);
//	freopen("fan.out","w",stdout);
	scanf("%lld",&cas);
    fo(j,1,cas){
    	printf("Case #%d: ",j);
    	scanf("%lld%lld",&n,&k);
    	ci=1,c=0;z=0;
    	while(k>ci)z+=ci,k-=ci,ci*=2,c++;
    	if(k)z+=ci;
    	l=(n-z)/ci;
    	t=(n-z)%ci;
    	l1=r1=l/2;if(l%2)l1++;
    	if(k<=t){
    		if(l1>r1)r1++;else l1++;
		    printf("%lld %lld\n",l1,r1);
		}
		else printf("%lld %lld\n",l1,r1);
    /*	sl1=sl2=sr1=sr2=0;
    	ci=1;c=1;
    	if(n%2)l=r=n/2;else l=n/2-1,r=n/2;ge1=ge2=1;sl1=l,sr1=r;sl2=l,sr2=r;
    	while(k>ci){
		    k-=ci;
		    if(l==r)ge1+=ge2,r=0,ge2=0;num=2;if(ge2)num=4;
		    if(l%2)a[1].a=a[2].a=l/2;else a[1].a=l/2-1,a[2].a=l/2;
		    a[1].b=ge1,a[2].b=ge1;a[1].l=a[2].l=a[1].a,a[1].r=a[2].r=a[2].a;
		    if(r%2)a[3].a=a[4].a=r/2;else a[3].a=r/2-1,a[4].a=r/2;
		    a[3].b=ge2,a[4].b=ge2;a[3].l=a[4].l=a[3].a,a[3].r=a[4].r=a[4].a;
		    sort(a+1,a+1+num,cmp);
		    bz=1;
		    fo(i,2,num)if(a[i].a!=a[i-1].a)bz=0;
		    l=a[1].a;sl1=a[1].l,sr1=a[1].r;
			ge1=0;fo(i,1,num)if(a[i].a==l)ge1+=a[i].b;
		    r=-1;ge2=0;
		    if(!bz){
		    	r=a[num].a;sl2=a[num].l,sr2=a[num].r;
			    fo(i,1,num)if(a[i].a==r)ge2+=a[i].b;
			}
		    ci*=2;
		    c++;
		}
		if(l<r)swap(l,r),swap(ge1,ge2),swap(sl1,sl2),swap(sr1,sr2);
		if(k<=ge1){
		    if(sl1<sr1)swap(sl1,sr1);
		    printf("%lld %lld\n",sl1,sr1);
		}
		else{
		    if(sl2<sr2)swap(sl2,sr2);
		    printf("%lld %lld\n",sl2,sr2);
		}*/
		//printf("Case #%d: %d\n",ans);
	}
}
