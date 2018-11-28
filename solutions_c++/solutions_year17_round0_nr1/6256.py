#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
#define mp make_pair
#define f first
#define s second

using namespace std;
string s;


int main()
{
	int t;
	cin>>t;
	
	for(int i=0;i<t;i++)
	{
		int k,l;
		cin>>s>>k;
		int j=0,counter=0,flag=0;
		
		for(j=0;j<s.size();j++)
		{
			if(s[j]=='-')
			{
				if(j>s.size()-k)
				{
					cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"	<<endl;
					break;
				}
			
				counter++;
				for(l=j;l<j+k && l<s.size();l++) 
				{
					
					if(s[l]=='-') s[l]='+';
					else	s[l]='-';
				}
			}
		}
		
		for(j=0;j<s.size();j++)
		{
			if(s[j]=='-')
			{
				flag=1;
				break;
			}
		}
		
		
		
		
		if(flag==0)
		cout<<"Case #"<<i+1<<": "<<counter<<endl;
	}
}
