#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

string s;
int k,c;
bool f;

int main()
{
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("As.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("Al.out","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		f=1;c=0;
		cin>>s;
		cin>>k;
		int l=s.size();
		for(int i=0;i<l-k+1;i++)
		{
			if(s[i]=='-') 
			{
				c++;
			for(int j=0;j<k;j++) if(s[j+i]=='-') s[i+j]='+';else s[i+j]='-';
			}
		}
		for(int i=0;i<l;i++) if(s[i]=='-') {f=0;break;}
		if(f) printf("Case #%d: %d\n",t,c);
		else printf("Case #%d: IMPOSSIBLE\n",t);
	}

	return 0;
}


