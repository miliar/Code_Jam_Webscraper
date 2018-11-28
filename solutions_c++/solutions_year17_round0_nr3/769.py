#include <bits/stdc++.h>

using namespace std;

struct room
{
	long long n,v;
	inline room():n(0),v(0){}
	inline room(long long N,long long V):n(N),v(V){}

	inline friend bool operator<(room x,room y)
	{
		return x.n>y.n||x.n==y.n&&x.v<y.v;
	}
};
set<room>s;

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		long long n,k;
		scanf("%I64d%I64d",&n,&k);
		s.clear();
		s.insert(room(n,1));

		printf("Case #%d: ",tt);
		while(k)
		{
			auto iter=s.begin();
			long long num2=(iter->n-1)/2;
			long long num1=iter->n-1-num2;
			//printf("%I64d %I64d %I64d\n",k,num1,num2);

			if(iter->v>=k)
			{
				printf("%I64d %I64d\n",num1,num2);
				break;
			}
			else
			{
				k-=iter->v;

				auto iter1=s.lower_bound(room(num1,0));
				if(iter1!=s.end()&&iter1->n==num1)
				{
					room temp=*iter1;
					s.erase(iter1);
					temp.v+=iter->v;
					s.insert(temp);
				}
				else
					s.insert(room(num1,iter->v));

				iter1=s.lower_bound(room(num2,0));
				if(iter1!=s.end()&&iter1->n==num2)
				{
					room temp=*iter1;
					s.erase(iter1);
					temp.v+=iter->v;
					s.insert(temp);
				}
				else
					s.insert(room(num2,iter->v));

				s.erase(iter);
			}
		}
	}

	return 0;
}