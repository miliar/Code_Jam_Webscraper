#include <iostream>
#include <cstdio>
#include <string.h>
#define p printf
#define loop(i,n) for(int i=0;i<n;i++)
using namespace std;

int main()
{
	int t,k;
	char s[2000];
	cin>>t;
	int pos=0;
	for(int j=1;j<=t;j++)
	{
		scanf("%s",s);
		cin>>k;
		int flip=0;
		pos=0;
		while(1)
		{
			while(s[pos]=='+')
			{
				pos++;
			}
			if(pos==strlen(s))
			{
				cout<<"Case #"<<j<<": "<<flip<<"\n";
				break;
			}
			if((pos+k)>strlen(s))
			{
				cout<<"Case #"<<j<<": IMPOSSIBLE\n";
				break;
			}
			flip++;
			loop(i,pos+k)
			{
				if(s[i]=='+')
					s[i]='-';
				else
					s[i]='+';
			}
		}
	}
	return 0;
}