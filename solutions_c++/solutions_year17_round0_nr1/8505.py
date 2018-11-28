#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;

int count=0;

int getLength(char str[])
{
	int i=0;
	while(str[i]!='\0')
		i++;
	return i;
}

int flip(char str[], int i, int k)
{
	bool flag=true;
	int n=i;
	while( i < (n+k))
	{
		if(str[i]=='-')
			str[i++]='+';
		else
		{
			str[i++]='-';
			flag=false;
		}
	}
	count++;
	
	if(flag==true)
		return n+k;
	else 
		return n+1;
}

void fun(char str[], int k)
{
	int i=0;
	int l=getLength(str);
	while(i<l)
	{
		if(str[i]=='+')
			i++;
		else
			i=flip(str, i, k);    //calling clip to flip the cakes
	}
}

int main()
{
	int t, i, k, j;
	char str[1000];
	cin>>t;
	for(i=1; i<=t; i++)
	{
		count=0;   // for counting number of flips
		cin>>str;
		cin>>k;
		fun(str, k);  // calling fun() for performing action
				
		j=0;
		while(j<getLength(str))
		{
			if(str[j]=='+')
				j++;
			else
				break;
		}
		if(j==getLength(str))
			cout<<"Case "<<"#"<<i<<": "<<count<<endl;
		else
			cout<<"Case "<<"#"<<i<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
