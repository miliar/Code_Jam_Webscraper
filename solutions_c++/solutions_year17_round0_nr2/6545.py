#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long
#define N 100005
#define S(x) scanf("%d",&x)
#define S2(x,y) scanf("%d%d",&x,&y)
#define wl(n) while(n--)
#define PB push_back
#define MP make_pair
#define P(x) printf("%d\n",x)
#define fl(i,n) for(i=0;i<n;i++)
#define fil(i,a,n) for(i=a;i<n;i++)
#define rev(i,a,n) for(i=n-1;i>=a;i--)

int main()
{

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll t;
   	cin>>t;
   	ll tmp=1;
   	while(t--)
   	{
   		ll n;
   		cin>>n;

   		ll arr[30],i,sz=0,n1;
   		n1=n;
   		while(n1)
   		{
   			arr[sz++]=n1%10;
   			//cout<<"dig="<<arr[sz-1]<<endl;
   			n1/=10;
   		}

   	/*	cout<<"Digit array:"<<endl;
   		for(i=sz-1;i>=0;i--)
   			cout<<arr[i]<<" ";
   		cout<<endl;

	*/
   		
   		for(i=sz-1;i>0;i--)
   		{
   			
   			//cout<<"arr=="<<arr[i]<<"sec="<<arr[i-1]<<endl;
   			if(arr[i]>arr[i-1])
   			{
   				//cout<<"if--arr=="<<arr[i]<<"sec="<<arr[i-1]<<endl;
   				//go back untill the digits repeat
   				ll j,temp=arr[i];
   				//cout<<"temp="<<temp<<endl;
   				while(temp==arr[i] && i<sz)
   					i++;

   				//cout<<"arr="<<arr[i-1]<<"i="<<i<<endl;
   				arr[i-1]--;
   				for(j=0;j<i-1;j++)
   				{
   					arr[j]=9;
   				}
   				break;	

   			}	

   		}

   		//make the no
   		n1=0;
   		for(i=0;i<sz;i++)
   		{
   			n1+=(ll)pow(10,i)*arr[i];
   			//cout<<"n1="<<n1<<endl;
   		}

   		cout<<"Case #"<<tmp<<": "<<n1<<endl;
   		tmp++;


   	} 
    
   	return 0;
} 