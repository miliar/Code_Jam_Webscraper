#include<cstdio>
#include<set>
using namespace std;
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,cas=1;
	scanf("%d",&T);
	while(T--)
	{
		long long n,k;
		scanf("%I64d %I64d",&n,&k);
		set<long long> S;
		S.insert(1);
		S.insert(n+2);
		long long mi=0,ma=0;
		long long stall;
		for(int i=1;i<=k;i++)
		{
			set<long long>::iterator it=S.begin();
			mi=0,ma=0;
			while(it!=S.end())
			{
				long long L=*it,R;
				it++;
				R=*it;
				if(R-L==1) continue;
				long long tmp=(R+L)/2;
				if(tmp-L-1>mi) mi=tmp-L-1,ma=R-tmp-1,stall=tmp;
				else if(tmp-L-1==mi&&R-tmp-1>ma) ma=R-tmp-1,stall=tmp;
			}
			S.insert(stall);
		}
		printf("Case #%d: %d %d\n",cas,ma,mi);
		cas++;
	}
}
