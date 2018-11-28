#include <bits/stdc++.h>
using namespace std;
#define lli long long int

int main()
{
	lli t,n,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		lli a;
		while(n>0)
		{	
			a=n;
			vector <int> x,y;
			while(a>0)
			{
				int temp=a%10;
				a=a/10;
				x.push_back(temp);
			}
			y=x;
			sort(x.begin(),x.end(),greater<int>());
			if(x==y)
			{
				cout<<"Case #"<<i<<": "<<n<<endl;
				break;
			}	
			else
				n--;
		}
	}
}