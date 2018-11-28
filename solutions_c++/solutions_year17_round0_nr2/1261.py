#include<bits/stdc++.h>
using namespace std;
int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("blarge.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		string s;
		cin>>s;
		int n=s.size();
		int brk=0,p=0;
		for(int i=0;i<s.size()-1;i++)
		{
			if(s[i]>s[i+1])
			{	
				if(s[i]=='1')
				{
				//	cout<<"\nimhere1\n";
					cout<<"Case #"<<tc<<": ";
					for(int i=0;i<n-1;i++)
					cout<<"9";
					cout<<"\n";
					p=1;
					break;
				}
				else
				{
					s[i]=s[i]-1;
				for(int j=i;j>=1;j--)
				 {
					if(s[j]<s[j-1])
					{
						s[j]=57;
						s[j-1]=s[j-1]-1;
						
					}
					
					
					
				   }
				   for(int j=i+1;j<n;j++)
				   s[j]=57;
				   
				   //cout<<"\nimhere2\n";
				   cout<<"Case #"<<tc<<": "<<s<<"\n";
					brk=1;
					p=1;
					break;
				}
				
			}
			
			if(brk==1)
			break;
		}
		if(p==0)
		cout<<"Case #"<<tc<<": "<<s<<"\n";
		
	}
}
