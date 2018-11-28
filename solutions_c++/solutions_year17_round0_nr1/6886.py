#include<iostream>
#include<string.h>

using namespace std;

FILE *fin = freopen("in.txt","r",stdin);
FILE *fout = freopen("out.txt","w",stdout);

char s[1005];

void invert(int i)
{	
	if(s[i]=='+')
		s[i]='-';

	else if(s[i]=='-')
		s[i]='+';
}


int main()
{
int t;
 cin>>t;

 int x=t;

while(x--)
{
int k,i,count=0,flag=0;

{
	cin>>s;

	cin>>k;

for(i=0;i<=(strlen(s)-k);i++)
{
	if(s[i]=='-')
	{
		for(int j=i;j<(k+i);j++)
		{
			invert(j);
		}

		count++;
	}
}

for(i=0;s[i]!='\0';i++)
{
	if(s[i]=='-')
	{
		cout<<"Case #"<<(t-x)<<": IMPOSSIBLE"<<endl;
		flag=1;
		break;
	}

}

if(flag==0)
	cout<<"Case #"<<(t-x)<<": "<<count<<endl;

}
}
}