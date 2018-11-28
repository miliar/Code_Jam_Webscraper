#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
	ll int t;
	cin>>t;
	while(t--){
		
		ll int A[1100]={0};
	
		static int j=1;
		ll int n,l=0,i=0,flag=0;
		cin>>n;
//		cout<<n<<endl;
		while(n!=0){
			A[i++]=n%10;
			if(n%10==0) flag=1;
			n/=10;
			l++;
		}
		
		if(flag==1){
	//		cout<<"kutta";
			ll int temp=-1;
			for(ll int i=0;i<l;i++)
			{
				if(A[i]<A[i+1]&&A[i]!=0) {
					A[i]=9;A[i+1]--;
				}
				else
				if(A[i]==0&&i<l-1)
				{
					temp=i;
					A[i]=9;A[i+1]--;	
				}
				if(temp!=-1)
				{
					while(temp>=0){
						A[temp--]=9;
					}
				}
			}	
				
		}
		else{
		
		for(ll int i=0;i<l-1;i++)
		{
			if(A[i]<A[i+1])
			{
				A[i]=9;
				A[i+1]--;
				if(A[i+1]==0) A[i+1]=9;	
			}
			
		}
		for(ll int i=l-1;i>=0;i--)
		{
			if(A[i]==9)
			{
				while(i>=0)
				{
					A[i--]=9;
				}
				break;
			}
			
		}
		
		}
		ll int ans=0;
		for(ll int i=l-1;i>=0;i--)
		{
//			cout<<A[i]<<"*";
			ans=ans*10+A[i];
		}
		
		cout<<"Case #"<<j<<": "<<ans<<endl;
		j++;
		
	}
	
	
}
