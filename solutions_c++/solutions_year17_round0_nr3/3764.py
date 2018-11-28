#include<bits/stdc++.h>
#define T() int t; cin>>t; while(t--)
#define f(i,start,lim) for(long long i=start;i<lim;i++)
#define ll long long
#define YES printf("YES\n")
#define NO printf("NO\n")
#define MOD 1000000007
#define MAX 9001
using namespace std;

long long maxi(int a,int b)
{
	if(a>b)
	return a;
	else
	return b;
}
long long mini(int a,int b)
{
	if(a>b)
	return b;
	else
	return a;
}

int main()
{
	FILE *fin = freopen("C-small.in","r",stdin);
	assert(fin!=NULL);
	FILE *fout = freopen("C-output.out","w",stdout);
	int t;
	cin>>t;
	f(r,1,t+1)
	{
		long long n,k,x,y,z;
		cin>>n>>k;
		multiset <long long > s;
		std::multiset<long long>::iterator it;
		s.insert(n);
		while(k--)
		{
			it = s.end();
			it--;
			z=(*it);
			x=z/2;
			y = (z/2) - ((z%2 == 0 && z>0)?1:0);
			s.erase(it);
			s.insert(x);
			s.insert(y);
		}
		cout<<"Case #"<<r<<": ";
		cout<<x<<" "<<y<<endl;
	}
}











