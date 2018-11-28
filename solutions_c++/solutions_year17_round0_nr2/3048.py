#include<bits/stdc++.h>
using namespace std;
#define llu unsigned long long
int main()
{
	int t;
	cin>>t;
	int cn=1;
	while(t--)
	{
		llu n;
		cin>>n;
		vector<llu>m;
		llu tmp=n;
		while(tmp)
		{
			m.push_back(tmp%10);
			tmp/=10;
		}
		reverse(m.begin(),m.end());
/*		for(int i=0;i<m.size();i++)
			cout<<m[i];
		cout<<"\n";
	*/int d=0;
		for(llu i=0;i<m.size();)
		{
			if(i==0)
			{
				i++;
				continue;
			}
			if(m[i]<m[i-1] || m[i]==0) 
			{
				for(int j=i;j<m.size();j++)
				{
					m[j]=9;
					d=1;
				}
				m[i-1]-=1;
				if(m[i-1]==0)
				{
				//	m[i-1]-=1;
					i--;
					continue;
				}
				else if(i-2>=0 && m[i-1]<m[i-2])
				{
					i--;
					continue;
				}
				else
				{
					if(d)
						break;
				}
			}
			else if(d)
				break;
			i++;
		}
		cout<<"Case #"<<cn<<": ";	
		for(int i=0;i<m.size();i++)
		{
			if(m[i]!=0)
				cout<<m[i];
		}
		cout<<"\n";
		cn++;
	}
}




		
