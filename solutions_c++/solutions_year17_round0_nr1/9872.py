#include <iostream>

using namespace std;

int strlen(char * s)
{
    int len = 0;
    while (s[len]!='\0')
        len++;
    return len;
}

void change(char * S, int a, int K)
{
	int i;
	for(i=a;i<a+K;i++)
	{
		S[i]=(S[i]=='+')?'-':'+';
	}

}

int flip(char * S,int K)
{
	int i,l,Times=0;
	l=strlen(S);
	for(i=0;i<=l-K;i++)
	{	
		if(S[i]=='-')
		{
			change(S,i,K);
			Times++;
		}
	}
	return Times;
}

int checkneg(char *S)
{
	int i,v=0;
	for(i=0;S[i]!='\0';i++)
		v=(S[i]=='-')?1:v;
	return v;
}

int main()
{
    int T,K,i,j,v;
	char S[100];
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cin>>S>>K;
		if(checkneg(S)==0)
		{
			cout<<"Case #"<<i<<": "<<0<<"\n";
		}
		else
		{
			v=0;
			for(j=0;j<=strlen(S)-K;j++)
			{
				if(checkneg(S)==0) break;
				v+=flip(S,K);
			}	
			if(checkneg(S)) cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<"\n";
			else cout<<"Case #"<<i<<": "<<v<<"\n";
		}
	}

	return 0;	

}






















