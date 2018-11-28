#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("inp151.txt","r",stdin);
	freopen("out1234.txt","w",stdout);
	int t,i,j,k,p=0,point,f,l,zar;
	string s;
	char pre;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>s;
		p=-1;
		point=-1;
		pre=' ';
		for(j=1;j<s.length();j++)
		{
			if(p>-1  && pre == s[j-1] && s[j]>s[j-1])
			{
				  	p=-1;
			}
		    else if(s[j]==s[j-1])
			{
				if(p==-1)
				{
				   point=j-1;pre=s[j-1];
				  
			    }
				
				p++;
					
			}
			else if(s[j]<s[j-1] && s[j-1]!=pre )
			{
				
			
				int n = (int)(s[j-1])-49;
				s[j-1] = n+'0';
				zar=0;
				for(k=j;k<s.length();k++)
				{
					s[k]='9';zar=1;
				}
				if(zar==1)
				  break;
			}
			
		
			else if(s[j]<s[j-1] && p!=-1 && pre==s[j-1])
			{
					int m = (int)(s[point])-49;
					s[point]=m+'0';
				//	cout<<m<<endl;
				//	cout<<s[point]<<endl;
					for(l=point+1;l<s.length();l++)
					{
						s[l] = '9';
					}
			}
			
		}
		cout<<"Case #"<<i<<": ";
		for(f=0;s[f]=='0' && f<s.length();f++);
        for(j=f;j<s.length();j++)
          cout<<s[j];
        cout<<endl;  
	}
}
