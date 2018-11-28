#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
         long long n,k;
         cin>>n>>k;
         set<pair<long long,pair<long long,long long> > > s;
         s.insert(make_pair(0-(n+1),make_pair(0,n+1)));
         long long x,y;
         while(!s.empty()&&k)
         {
         	pair<long long,pair<long long,long long> > p=*(s.begin());
         	s.erase(s.begin());
         	k--;
         	long long a=p.second.first;
         	long long b=p.second.second;
            long long c=(a+b)/2;
            x=a;y=b;
            s.insert(make_pair(a-c,make_pair(a,c)));
            s.insert(make_pair(c-b,make_pair(c,b)));
         }
         long long p=(x+y)/2-x;
         long long q=y-(x+y)/2;
         cout<<"Case #"<<z<<": "<<max(p,q)-1<<" "<<min(p,q)-1<<endl;
	}
	return 0;
}
