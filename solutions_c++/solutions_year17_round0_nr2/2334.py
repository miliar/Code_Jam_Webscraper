#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define ll long long int
#define nn 2001
#define inf -15000000000000ll
#define logn 21
#define ff first
#define se second
#define mod 1000000007ll
#define pdd pair<double,double>
#define db double
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define mt make_tuple
using namespace std;
using namespace __gnu_pbds;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> OST;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	ifstream fin;
	ofstream fout;
	fin.open("/home/nishant/Downloads/B-large.in");
	fout.open("/home/nishant/Downloads/loutputB.txt");
	int t;
	fin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		fout<<"Case #"<<tt<<": ";
		ll n;
		fin>>n;
		ll v=n;
		int arr[20];
		int sz=0,i;
		while(v)
		{
			sz++;
			v/=10;
		}
		v=n;
		if(sz==1)
		{
			fout<<n<<endl;
			continue;
		}
		i=sz-1;
		while(v)
		{
			arr[i--]=v%10;
			v/=10;
		}
		int f=0;
		for(i=0;i<sz-1;i++)
		{
			if(arr[i]>arr[i+1])
			{
				f=1;
				break;
			}
		}
		if(!f)
		{
			fout<<n<<endl;
			continue;
		}
		for(;i>=0;i--)
			if(arr[i]<arr[i+1])
				break;
		i++;
		arr[i]--;
		for(i=i+1;i<sz;i++)
			arr[i]=9;
		v=0;
		for(int i=0;i<sz;i++)
			v=(v*10+arr[i]);
		fout<<v<<endl;
	}
	return 0;
}