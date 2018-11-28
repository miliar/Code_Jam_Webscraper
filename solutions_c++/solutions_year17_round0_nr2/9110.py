#include<iostream>
#include<string.h>
#define ll long long int
using namespace std;
int main()
{
	ll t,t1;
	cin>>t;
	for(t1=1; t1<=t; t1++)
	{
		char n[30];
		cin>>n;
		
		ll len = strlen(n),i,flag=0;
		for(i=1; i<len; i++)
		{
			if(n[i]<n[i-1])
			{
				flag=1;
				break;
			}
		}
		cout<<"Case #"<<t1<<": ";
		if(flag==0){
			cout<<n<<"\n";
			continue;
		}
		
		ll start = 0,prev = n[0];
		for(i=1; i<len; i++)
		{
			if(n[i]==prev){
				continue;
			}
			else if(n[i]>prev){
				start = i;
				prev = n[i];
			}
			else{
				break;
			}
		}
		//cout<<start<<"\n";
		n[start]-=1;
		for(i=start+1; i<len; i++)
		{
			n[i]='9';
		}
		
		//o/p
		//leading 0
		for(i=0; i<len; i++)
		{
			if(n[i]!='0')
			{
				break;
			}
		}
		
		for(; i<len; i++){
			cout<<n[i];
		}
		cout<<"\n";
	}
}
