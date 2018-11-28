#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define rep(a,n) for(i=a;i<n;i++)
#define lld long long int
#define mod 1000000007
using namespace std;
int main()
{	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{	lld n,num,p,temp,x,y;
		cin>>n;
		temp=n;
		p=1;
		num=0;
		while(temp)
		{	x=temp%10;
			temp/=10;
			y=temp%10;
			temp/=10;
			num+=x*p;
			//cout<<"num"<<num<<endl;
			p*=10;
			if(y>x)
			{	n-=(num+1);
				temp=n;
				temp/=p;
				num=n%p;
			}
			else
				temp=n/p;
		}
		cout<<"Case #"<<i<<": "<<n<<endl;
	}
}