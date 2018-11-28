#include<bits/stdc++.h>
using namespace std;
#define FALSE 0
#define TRUE 1
#define ll long long
#define loop(i,j,k) for(i=j ; i<k ; i++)
 
int main()
{
	ll ii,t,n,ans;
	cin>>t;
	loop(ii,1,t+1)
	{
		cin>>n;
		ll str[30];
		ll i=0,count=0;
		ll temp=n;
		while(n>0)
		{
			n=n/10;
			count++;
		}
		n=temp;
		while(n>0)
		{
			str[--count]=n%10;
			n=n/10;
			i++;
		}
		ll j;
		ll l=i;
		for(j=l-2 ; j>=0 ; j--)
		{
			if(str[j+1]<str[j])
			{
				for(ll k =j+1 ; k<l ; k++)
					str[k]=9;
				str[j]=str[j]-1;
			}
		}
		j=0;
		if(str[0]==0)
			j=1;
		cout<<"Case #"<<ii<<": ";
		for( ; j<l ; j++)
			cout<<str[j];
		cout<<endl;
		
	}
}