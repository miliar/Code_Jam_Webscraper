#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#define REPP(a,b,c,d) for(int a=b; a<=c; a+=d)
#define REP(a,b,c) REPP(a,b,c,1)
#define REVV(a,b,c,d) for(int a=b; a>=c; a-=d)
#define REV(a,b,c) REVV(a,b,c,1)
typedef unsigned long long LLU;

using namespace std;

double prob[55],tmp[55],unit,ttp,res;

void merge(double *A,int left, int right)
{
	int mid=(left+right)/2;
	int cnt1=left, cnt2=mid+1, idx=1;
	while(cnt1<=mid || cnt2<=right)
	{
		if(cnt1>mid)
		{
			tmp[idx]=A[cnt2];
			cnt2++;
			idx++;
			continue;
		}
		if(cnt2>right)
		{
			tmp[idx]=A[cnt1];
			cnt1++;
			idx++;
			continue;
		}
		if(A[cnt1]>A[cnt2])
		{
			tmp[idx]=A[cnt1];
			cnt1++;
			idx++;
			continue;
		}
		tmp[idx]=A[cnt2];
		cnt2++;
		idx++;
	}
	REP(i,1,idx-1) A[left+i-1]=tmp[i];
}

void mergesort(double *A ,int left, int right)
{
	if(left==right) return;
	int mid=(left+right)/2;
	mergesort(A,left,mid);
	mergesort(A,mid+1,right);
	merge(A,left,right);
}

int main()
{
	int t,ix,n,k;
	scanf("%d",&t);
	REP(tc,1,t)
	{
		scanf("%d %d",&n,&k);
		scanf("%lf",&unit);
		REP(i,1,n) scanf("%lf",&prob[i]);
		ix=0;
		res=prob[0]=1.0;
		mergesort(prob,1,n);
		while(ix<n && unit>0.0)
		{
			ttp=(double)min(prob[k-ix-1]-prob[k],unit/(ix+1));
			REV(i,k,k-ix) prob[i]+=ttp;
			unit-=(ix+1)*(double)ttp;
			ix++;
		}
		REP(i,1,k) res*=prob[i];
		printf("Case #%d: %.6lf\n",tc,res);
	}
	return 0;
}
