#include<map>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream> 
#include<algorithm> 
using namespace std;
int a[101];
map<long long,long long> M;
int main()
{
//	freopen("C-small-2-attempt0.in","r",stdin);
//	freopen("C-small-2-attempt0.out","w",stdout);
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,kk=0;
	scanf("%d",&T);
	while(T>0)
	{
		M.clear();
		T--;
		kk++;
		long long n,k;
		scanf("%lld%lld",&n,&k);
		M[n]=1;
		long long s=1,la=n;
		map<long long,long long>::iterator it;
		while(k>s)
		{
			it=M.end();
			it--;
			long long lx=(*it).second,sx=(*it).first;
			M.erase(it);
			long long xx=(sx-1)/2;
			long long lx1=sx-1-xx,lx2=xx;
			s+=lx;
			M[lx1]+=lx;
			if(k<=s)
			{
				la=lx1;
				break;
			}
			s+=lx;
			M[lx2]+=lx;
			la=lx2;
		}
		long long xx=(la-1)/2;
		printf("Case #%d: %lld %lld\n",kk,la-1-xx,xx);
	}
	return 0;
}
