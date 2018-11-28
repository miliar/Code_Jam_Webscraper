#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define mp make_pair
#define pb push_back
#define scan(x) scanf("%lld",&x)
#define MAX 100005
#define INF 1000000000000000007ll
#define mod 1000000007
#define pii pair<int,int>
#define hashmod 300007
#define hashmod1 300023

int main()
{
	freopen("C:\\Users\\watson\\Documents\\B-large.in","r",stdin);
	freopen("C:\\Users\\watson\\Documents\\output.txt","w",stdout);

	int t;
	cin>>t;
	for(int T=1;T<=t;T++)
	{
		ll n;
		cin>>n;

		int arr[32];
		fill(arr,arr+32,0);
		int k=0;
		while(n>0)
		{
			int d=n%10;
			arr[k++]=d;
			n/=10;
		}
		
		arr[k]=arr[k-1]-1;
		k--;
		
		for(int i=k;i>=1;i--)
		{
			if(arr[i-1]>=arr[i])
				continue;
			else
			{
				int j=i+1;
				while(arr[i]==arr[j])
				{
					j++;
				}
				j--;
				arr[j]=arr[i]-1;
				j--;
				while(j>=0)
				{
					arr[j]=9;
					j--;
				}
			}
		}
		cout<<"Case #"<<T<<": ";
		if(arr[k]==0)
			k--;
		for(int i=k;i>=0;i--)
			cout<<arr[i];
		cout<<"\n";
	}

}