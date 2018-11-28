#include<iostream>
#include<cstring>
#include<cstdlib>
using namespace std;

void correct (char number[])
{
int i,a;
if(number[0]=='0')
{a=strlen(number); for(i=0;i<a;i++) number[i]=number[i+1]; }			
}

void func( char number[])
{	//cout<<number<<endl;
	correct(number);

	int i,j,check=1; int len= strlen(number);
	
	if(len==1) return;

	for(i=0;i<len-1&&check==1;i++)
		if(number[i]>number[i+1]) check=0;
	if(check==1) return;

	
	for(i=0;i<len-1;i++)
	{
		if(number[i]>number[i+1])
		{for(j=i+1;j<len;j++) number[j]='9'; number[i]=number[i]+'0'-'1'; break;} 	
	}
	func(number);
	return;
}


int main()
{
	int i,j,k,a,b;
	int n;
	char number[20],tn[20];
	
	cin>>n;
	for(j=1;j<=n;j++)
	{
		cin>>number;
		
		func(number);		
		correct(number);
		cout<<"Case #"<<j<<": "<<number<<endl;
			
		number[0]='\0';
	}
	
	return 0;
}
