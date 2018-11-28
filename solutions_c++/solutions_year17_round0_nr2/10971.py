#include<bits/stdc++.h>
using namespace std;
int check(long int n)
{
	int temp;
	int flag=0;
	temp=n/10;
	while(n>0)
	{
		if(n%10<temp%10)
		{
		
			flag=1;
			break;
		}
		n/=10;
		temp/=10;
	}
	
	return flag;
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int ilc,t,num;
	cin>>t;
	//cout<<t;
	for(int olc=0;olc<t;olc++)
	{
	
		cin>>num;
		cout<<"Case #"<<olc+1<<": ";	
//		int num,ilc;
	//cout<<"nefdkbn";	
		for(ilc=num;ilc>0;ilc--)
		{
			if(!check(ilc))
			break;
		}
		cout<<ilc<<"\n";
	}
}
