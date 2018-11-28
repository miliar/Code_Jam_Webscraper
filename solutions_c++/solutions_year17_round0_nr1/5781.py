#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp> 
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
#define fs first
#define sc second
#define Max 10000000000007
#define mod 1000000007
#define pb push_back
#define mp make_pair
typedef long long Int;
typedef pair<Int,Int> pii;
typedef vector<Int> vi;
typedef vector<pii> vii;
typedef tree<pii,null_type,less<pii>,rb_tree_tag,tree_order_statistics_node_update> ordered_set;

int main()
{
	Int T,k,z;
	string S;
	cin>>T;
	for(int z=1;z<=T;z++)
	{
		Int ans=0;
		cin>>S>>k;
		for(int i=0;i<S.length();i++)
		{
			if(S[i]=='-'&&i+k-1<S.length())
			{
				for(int j=i;j<=i+k-1;j++)
				{
					S[j]=(S[j]=='-')?'+':'-';
				}
				ans++;
			}
		}
		Int flag=true;
		for(int i=0;i<S.length();i++)
		{
			if(S[i]=='-')
				flag=false;
		}

		if(ans!='0'&&flag==true)
		printf("Case #%lld: %lld\n",z,ans);

		else
			printf("Case #%lld: IMPOSSIBLE\n",z);

	}
}