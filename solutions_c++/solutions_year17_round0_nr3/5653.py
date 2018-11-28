#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define rep(a,n) for(i=a;i<n;i++)
#define lld long long int
#define mod 1000000007
using namespace std;
bool comp(int i,int j)
{ return i>j;
}
int main()
{	int t,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{	int n,k,i,a,b,x,arr[100005];
	queue<int> q1;
    cin>>n>>k;

		q1.push(n);
		i=1; int p=2;
		while(!q1.empty())
		{	x=q1.front();
			q1.pop();
			arr[i++]=x;
			a= x/2;
			b=x%2==1 ? x/2: (x/2)-1;
			
			if(a!=0)
				q1.push(a);
			if(b!=0)
				q1.push(b);
		} 
		sort(arr+1,arr+n+1,comp);
	//	for(i=1;i<=n;i++)
	//	cout<<i<<". "<<arr[i]<<endl;
		x=arr[k];
		a=x%2==1 ? x/2: (x/2)-1;
		cout<<"Case #"<<j<<": "<<x/2<<" "<<a<<endl;
	}
}

