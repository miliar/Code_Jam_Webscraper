#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#define REPP(a,b,c,d) for(int a=b; a<=c; a+=d)
#define REP(a,b,c) REPP(a,b,c,1)
#define REVV(a,b,c,d) for(int a=b; a>=c; a-=d)
#define REV(a,b,c) REVV(a,b,c,1)
typedef long long LL;

struct tdata{
	int K;
	int v;
}temp[1005],dat[1005];

double time[1005];

void merge(struct tdata *A, int left, int right)
{
	int mid=(left+right)/2;
	int cnt1=left, cnt2=mid+1, ix=1;
	while(cnt1<=mid || cnt2<=right)
	{
		if(cnt1>mid)
		{
			temp[ix]=A[cnt2];
			cnt2++;
			ix++;
			continue;
		}
		if(cnt2>right)
		{
			temp[ix]=A[cnt1];
			ix++;
			cnt1++;
			continue;
		}
		if(A[cnt1].K<A[cnt2].K)
		{
			temp[ix]=A[cnt2];
			cnt2++;
			ix++;
			continue;
		}
		temp[ix]=A[cnt1];
		cnt1++;
		ix++;
	}
	REP(i,1,ix-1) A[left+i-1]=temp[i];
}

void mergesort(struct tdata *A, int left, int right)
{
	if(left==right) return;
	int mid=(left+right)/2;
	mergesort(A,left,mid);
	mergesort(A,mid+1,right);
	merge(A,left,right);
}

int main()
{
	int t,D,n;
	scanf("%d",&t);
	REP(tc,1,t)
	{
		scanf("%d %d",&D,&n);
		double mn=1000000000,tmp;
		REP(i,1,n) scanf("%d %d",&dat[i].K,&dat[i].v);
		mergesort(dat,1,n);
		time[0]=0;
		REP(i,1,n)
		{
			time[i]=(double)(D-dat[i].K)/(double)dat[i].v;
			if(time[i]<time[i-1]) time[i]=time[i-1];
		}
		printf("Case #%d: %.7lf\n",tc,(double)D/(double)time[n]);
	}
	return 0;
}
