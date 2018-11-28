#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
  	ll t,n,f,i,j,k,m;
	char x;
  	cin>>t;
	for(m=0;m<t;m++)
	{
		cin>>n;
		char s[100];
		sprintf(s,"%lld",n);
		int l = strlen(s);
		if(l==1)
		{
			cout<<"Case #"<<m+1<<": "<<s<<endl;
			continue;
		}
		for(int i=1;i<l;i++)
        {
			if(s[i]>=s[i-1])
			{
				while(s[i]>=s[i-1])
				{
					i++;
				}
				if(i==l)
				{
					if(s[0]=='0')
					{
						for(f=0;f<l-1;f++)
							s[f] = s[f+1];
						s[f] = '\0';
					}
					cout<<"Case #"<<m+1<<": "<<s<<endl;
					break;
				}
				if(s[i-1]!=0)
				{
					for(k=i-1;k>0 && s[k]==s[k-1];k--);
					s[k] = s[k] - 1;
					k++;
					while(k!=l)
                    {
						s[k] = '9';
						k++;
                    }
					if(s[0]=='0')
					{
						for(f=0;f<l-1;f++)
							s[f] = s[f+1];
						s[f] = '\0';
					}
					cout<<"Case #"<<m+1<<": "<<s<<endl;
					break;
				}
				else
				{
					for(j=i-1;j>=0 && s[j]==0;j--);
					if(s[j]!=0)
					s[j] = s[j] - 1;
				}
				while(i!=l)
			    	{
					s[i] = '9';
					i++;
			    	}
				cout<<"Case #"<<m+1<<": "<<s<<endl;
				break;
			}
			else
			{
				s[i-1] = s[i-1] - 1;
				while(i!=l)
			    	{
					s[i] = '9';
					i++;
			    	}
				if(s[0]=='0')
				{
					for(f=0;f<l-1;f++)
						s[f] = s[f+1];
					s[f] = '\0';
				}
				cout<<"Case #"<<m+1<<": "<<s<<endl;
				break;
			}
		}
	}
}
