#include<bits/stdc++.h>
using namespace std;
int tidy(int n)
{   int prev=9,t;
	while(n!=0)
	{
		t = n%10;
		if(t<=prev)
		n=n/10;
		else
		break;
		prev=t;
	}
	if(n==0)
	return 1;
	else
	return 0;
}
int main()
{
	int t,n,i=1;
	cin>>t;
	while(t--)
	{
		cin>>n;
		while(n)
		{
			if(tidy(n))
			break;
			n--;
		}
		cout<<"Case #"<<i<<": "<<n<<endl;
		i++;
	}
}
