#include<iostream>
#include<string>
#define long long int lld
using namespace std;
int check(string n,int cric)
{	cric=100;
	for (int i=0;i<n.length()-1;i++)
	{
		if (n[i]>n[i+1])
		{	
			cric =i;
			break;
		}
	}
	return cric;
}
int main()
{	int t;
	cin>>t;
	string n;
	for (int j=1;j<=t;j++)
	{
	int cric=100;
	cin>>n;
	cric=check(n,cric);
	while(cric!=100)
	{
		n[cric]=n[cric]-1;
		for(int i=cric+1;i<n.length();i++)
		{
			n[i]='9';	
		}
		cric=check(n,cric);
	}

	cout<<"Case #"<<j<<": ";
	int flag=0;
	for (int i=0;i<n.length();i++)
	{
	if (flag!=0 || n[i]!='0')
	{
		flag=1;
		cout<<n[i];
	}
	}
	cout<<endl;
	
	
		
	}
	return 0;
	
}
