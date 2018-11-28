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
	fin.open("/home/nishant/Downloads/A-large.in");
	fout.open("/home/nishant/Downloads/loutput.txt");
	int t;
	fin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		fout<<"Case #"<<tt<<": ";
		string s;
		int k;
		fin>>s>>k;
		int n=s.length();
		int f=0,ans=0;
		for(int i=0;i<n-k+1;i++)
		{
			if(s[i]=='+')
				continue;
			ans++;
			for(int j=i;j<i+k;j++)
			{
				if(s[j]=='+')
					s[j]='-';
				else
					s[j]='+';
			}
		}
		for(int i=0;i<n;i++)
			if(s[i]=='-')
				f=1;
		if(f)
			fout<<"IMPOSSIBLE"<<endl;
		else
			fout<<ans<<endl;
	}
	return 0;
}