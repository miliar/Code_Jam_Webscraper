#include<bits/stdc++.h>
using namespace std;
struct str
{
	long long n,k;
};
bool acomp(struct str a,struct str b)
{
	return a.n>b.n;
}
void create(long long n,map<long long,long long> &m)
{
	if(n==0)
		return;
		m[n]++;
//	printf("%lld %lld\n",n,m[n]);
	if(n&1)
	{
		create(n/2,m);
                create(n/2,m);
	}
	else
	{
		create(n/2,m);
		create(n/2-1,m);
	}
}
int main()
{
	int k,i,j,t,T,n;
	cin>>t;
	for(T=0;T<t;++T)
	{
		cin>>n>>k;
		printf("Case #%d: ",T+1);
		map<long long,long long> m;
	//	m[n]=1;
		create(n,m);
		int l=m.size();
		struct str s[l];
		i=0;
		for (map<long long,long long>::iterator it=m.begin(); it!=m.end(); ++it)
		{
			s[i].n=it->first;
			s[i++].k=it->second;
		}
		sort(s,s+l,acomp);				
		i=0;
		if(k==1)
		{
			if(s[i].n&1)
                                        printf("%lld %lld\n",s[i].n/2,s[i].n/2);
                                else
                                        printf("%lld %lld\n",s[i].n/2,s[i].n/2-1);
			continue;
		}
		for(i=1;i<l;++i)
		{
			s[i].k+=s[i-1].k;
			if(k<=s[i].k)
			{
				if(s[i].n&1)
					printf("%lld %lld\n",s[i].n/2,s[i].n/2);
				else
					printf("%lld %lld\n",s[i].n/2,s[i].n/2-1);
				break;
			}
		}
		
	}
	return 0;
}
