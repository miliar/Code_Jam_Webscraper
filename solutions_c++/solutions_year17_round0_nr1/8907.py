#include<iostream>
#include<string.h>
using namespace std;

void flip(char *a)
{
	if(*a=='-')*a='+';
	else *a='-';
}

main()
{
	char s[1000];
	int T,K,i,j,t,trn,fl;
	cin>>T;
	for(t=1;t<=T;t++)
	{   trn=0; fl=1;
		cin>>s>>K;
		for(i=0;i<strlen(s);i++)
		{
			if(s[i]=='-')
			{   if(i>(strlen(s)-K)&&s[i]=='-')
			{
				fl=0;
				break;
			}
				for(j=0;j<K;j++)flip(&s[i+j]);
				trn++;
			}
		}
		if(fl)cout<<"Case #"<<t<<": "<<trn<<endl;
		else cout<<"Case #"<<t<<": IMPOSSIBLE\n";
	}
}
