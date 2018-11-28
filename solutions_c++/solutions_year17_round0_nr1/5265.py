#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;
int check(char *word,int len)
{
for(int i=0;i<len;i++)
{
if(word[i]=='-')
return 0;

}
return 1;
}
char * generate(int x)
{
char * word=new char[1001];
for(int i=0;i<x;i++)
{
int a=random()%2;
if(a)
	word[i]='+';
else
	word[i]='-';
}

return word;
}
int main()
{
int T;
cin>>T;
for(int k=0;k<T;k++)
{int c1=0;
	char *word=new char[10000];
	int lim;
	cin>>word>>lim;
	char *word1=new char[10000];
	strcpy(word1,word);
	for(int i=0;i<strlen(word)-lim+1;i++)
	{
		if(word[i]=='-')
		{c1++;
			for(int j=i;j<i+lim;j++)
				{
					if(word[j]=='+')
						word[j]='-';	
					else
						word[j]='+';
				}
		}
	}
int c2=0;
for(int i=strlen(word1)-1;i>lim-1;i--)
{
	if(word1[i]=='-')
		{c2++;
			for(int j=i;j>i-lim;j--)
				{
					if(word1[j]=='+')
						word1[j]='-';	
					else
						word1[j]='+';
				}
		}
}
char * wordf=NULL;
int *cw=NULL;
if(check(word,strlen(word)) && !check(word1,strlen(word1)))
{
	cw=&c1;
	wordf=word;
}
else if(!check(word,strlen(word)) && check(word1,strlen(word1)))
{
	cw=&c2;
	wordf=word1;
}
else if(check(word,strlen(word)) && check(word1,strlen(word1)))
{
	if(c1<c2)
		{
			cw=&c1;
			wordf=word;
		}
	else 	
		{
			cw=&c2;
			wordf=word1;
		}
}
cout<<"Case #"<<k+1<<": ";
if(cw==NULL)
	{
		cout<<"IMPOSSIBLE"<<endl;
		continue;
	}
cout<<*cw;
cout<<endl;
}


return 0;
}
