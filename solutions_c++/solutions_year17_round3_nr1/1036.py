#include<fstream>
using namespace std;
#include<algorithm>
#include<memory.h>
FILE*fin=fopen("input.txt","r");
FILE*fout=fopen("output.txt","w");
struct S
{
	__int64 r,h;
	bool operator()(S a,S b)
	{
		if(a.r!=b.r)return a.r>b.r;
		return a.h>b.h;
	}
}a[1010],b[1010];
bool cmp1(const S &a,const S &b)
{
	if(a.r!=b.r)return a.r>b.r;
	return a.h>b.h;
}
bool cmp2(const S &a,const S &b)
{
	return a.r*a.h>b.r*b.h;
}
int t,n,k;
__int64 out,mx;
int main()
{
	int i,j,l;
	fscanf(fin,"%d",&t);
	for(i=1;i<=t;++i)
	{
		fscanf(fin,"%d%d",&n,&k);
		for(j=1;j<=n;++j)fscanf(fin,"%d%d",&a[j].r,&a[j].h);
		mx=0;
		sort(&a[1],&a[n+1],cmp1);
		memcpy(b,a,sizeof(a));
		for(j=1;j<=n-k+1;++j)
		{
			memcpy(a,b,sizeof(a));
			out=a[j].r*a[j].r;
			sort(&a[j+1],&a[n+1],cmp2);
			for(l=j;l<j+k;++l)out=out+2*a[l].r*a[l].h;
			if(out>mx)mx=out;
		}
		fprintf(fout,"Case #%d: %.14lf\n",i,mx*3.141592653589793238462);
	}
	return 0;
}