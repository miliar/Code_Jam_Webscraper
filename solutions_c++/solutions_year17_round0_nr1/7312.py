#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int t,k,i,j,l,m;
	char s[1005];
	freopen("al.in","r",stdin);
	
	cin>>t;
	
	freopen("opf.txt","w",stdout);
	
	for(m=1;m<=t;++m)
	{
		cin>>s>>k;
		int cnt=0;
		l=strlen(s);
		
		for(i=0;i<l;++i)
		if(s[i]=='-')
		{
			if((i+k-1)<=(l-1))
				{
					for(j=0;j<k;++j)
					if(s[i+j]=='+')
					s[i+j]='-';
					else
					s[i+j]='+';				
					
					++cnt;
				}
			else
				{
					cnt=-1;
					break;
				}
				
		}
		
		if(cnt!=-1)
		cout<<"Case #"<<m<<": "<<cnt<<"\n";
		else
		cout<<"Case #"<<m<<": "<<"IMPOSSIBLE\n";
	}
		
	return 0;	
}
