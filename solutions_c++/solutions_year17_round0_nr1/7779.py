#include <iostream>
#include<bits/stdc++.h>

using namespace std;
int main()
{
	
	
	freopen("flip.in","r",stdin);
	freopen("flip.out","w",stdout);
	
	
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		int count=0;
		string s;
		int k;
		cin>>s>>k;
		int n= s.size();
		int g=0;
		for(int i=0;i<n;i++)
		{
			
			//cerr<<"________"<<s[i]<<endl;
			if(s[i]=='-' && i+k<=n)
			{
			//	cerr<<"sssssssss";
				count++;
				for(int j=i,l=1 ; l<=k; j++,l++)
				{
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
			else if (i+k>n)
			{
				for(int j=i;j<n;j++)
				{
					if(s[j] == '-')
					{
						g=1;
						break;
						
					}
				}	
			}
			else
				continue;	
		}
		
		if(g==1)
	//	cerr<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<endl;
		cout<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<endl;
		else
	//		cerr<<"Case #"<<z<<": "<<count<<endl;
			cout<<"Case #"<<z<<": "<<count<<endl;
	
		
	}
  
	
	
	
	
	
	
	
	//	cout<<"Case #"<<i<<": "<<j<<" "<<k-arr.begin()<<endl;
	//	cerr<<"Case #"<<i<<": "<<j<<" "<<k-arr.begin()<<endl;
		
	
	return 0;
	
}
