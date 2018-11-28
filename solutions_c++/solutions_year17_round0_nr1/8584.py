#include<iostream>
#include<string.h>
using namespace std;
void find(char *S,int k,int s,int e,int t,int times)
{
	//char symb=S[s];
	int i;
	for(i=s;i<=e && S[i]=='+';i++);
	if(i<=e)
	{
		if(i+k-1<=e)
		{
			for(int p=i;p<=i+k-1;p++)
			{
				S[p]=(S[p]=='+'?'-':'+');
			}
			find(S,k,i+1,e,t,times+1);
		}
		else
		{
			cout<<"Case #"<<t<<": IMPOSSIBLE\n";
		}
	}
	else
	{
		cout<<"Case #"<<t<<": "<<times<<"\n";
	}
}
int main()
{
	int t,k,len,i=0;
	char S[1000];
	//test cases 
	cin>>t;
	while(i++<t)
	{
		cin>>S>>k;
		len=strlen(S);
		find(S,k,0,len-1,i,0);
	}
	return 0;
}
