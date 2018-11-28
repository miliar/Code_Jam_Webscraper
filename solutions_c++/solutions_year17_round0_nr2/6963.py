#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	
	for(int i=1; i<=t; i++)
	{
		string n;
		cin>>n;
		cout<<"Case #"<<i<<": ";
		int s=n.size();
		for(int j=n.size()-1; j>0; j--)
		{
			if(n[j-1]>n[j])
			{
				n[j-1]=n[j-1]-1;
				s=j;
				
			}
		}
		
		for(int k=s; k<n.size(); k++)
		{
			n[k]='9';
		} 
		
		if(n[0]=='0')
		{
			for(int j=1; j<n.size(); j++)
		 {
			cout<<n[j];
		 }
		 cout<<endl;
		}
		else
		{
			cout<<n<<endl;
		}	
	}
	return 0;
}
