#include<iostream>
using namespace std;
int isyes(long long int x)
{
long long int prev,temp,i,j,flag=1;	
	prev=x%10;x=x/10;
	if(x==0)
	{
	return 1;
	}
	
	while(x>0)
	{
		temp=x%10;
		if(prev<temp)
		{flag=0;
		break;
		}
		prev=temp;
	x=x/10;
	}
	
	
	return flag;
}


int main()
{
	int t;
	cin>>t;long long int mn=1;
	while(t--)
{
	long long int i,j,k,n,m;
	cin>>n;
	while(n>1)
	{
	
		if(isyes(n)==1)
		{break;}
	n--;
	}
	cout<<"Case #"<<mn<<": "<<n<<endl;
mn++;
//cout<<isyes(n);
}
	
	
	
	return 0;
}
