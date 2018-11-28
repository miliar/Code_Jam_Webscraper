#include<cstdio>
#include<cstring>
#include<algorithm>
const int MAXN=1000+5;
struct Calc{int ls,rs,leftest,max,min,ind;};
int t,k,n;bool use[MAXN];Calc calc[MAXN];
/*bool comp(Calc a,Calc b)
{
	int mia=std::min(a.ls,a.rs),mib=std::min(b.ls,b.rs);
	if(mia!=mib) return mia>mib;
	int mxa=std::max(a.ls,a.rs),mxb=std::max(a.ls,a.rs);
	if(mxa!=mxb) return mxa>mxb;
	return a.ind<b.ind;
}*/
int main()
{
	scanf("%d",&t);
	freopen("o.txt","w",stdout);
	for(int CASE=1;CASE<=t;CASE++)
	{
		int fnlans;
		scanf("%d %d",&n,&k);
		memset(use,0,sizeof(use));
		for(int i=1;i<=n;i++)
			calc[i].ind=i;
		for(int i=1;i<=k;i++)
		{
			for(int j=1;j<=n;j++)
				calc[j].rs=calc[j].ls=0;
			for(int j=1;j<=n;j++)
			{
				if(use[j]) {calc[j].ls=calc[j].rs=-1;continue;}
				for(int A=j-1;A>=1;A--)
					if(use[A]) break; else {calc[j].leftest=A;calc[j].ls++;}
				for(int A=j+1;A<=n;A++)
					if(use[A]) break; else calc[j].rs++;
				//printf("%d: %d %d\n",j,calc[j].ls,calc[j].rs);
			}
			int sel1=0,sel2=0;
			for(int j=1;j<=n;j++)
			{
				calc[j].min=std::min(calc[j].ls,calc[j].rs);
				calc[j].max=std::max(calc[j].ls,calc[j].rs);
			}
			for(int j=1;j<=n;j++)
				sel1=std::max(sel1,calc[j].min);
			for(int j=1;j<=n;j++)
				if(sel1==calc[j].min) sel2=std::max(sel2,calc[j].max);
			for(int j=1;j<=n;j++)
			{
				if(sel1==calc[j].min && sel2==calc[j].max)
				{
					//printf("USE %d: %d %d\n",j,sel1,sel2);
					use[j]=1;
					fnlans=j;
					break;
				}
			}
			//std::sort(calc+1,calc+n+1,comp);
			//for(int j=1;j<=n;j++)
			//	printf("%d %d %d\n",j,calc[j].ls,calc[j].rs);
			//use[calc[1].ind]=1;
			//printf("[USE] %d: %d %d\n",calc[1].ind,std::min(calc[1].ls,calc[1].rs),std::max(calc[1].ls,calc[1].rs));
		}
		printf("Case #%d: %d %d\n",CASE,std::max(calc[fnlans].ls,calc[fnlans].rs),std::min(calc[fnlans].ls,calc[fnlans].rs));
	}
	return 0;
}
