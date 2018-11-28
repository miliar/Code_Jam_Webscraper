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
Int T,N;

Int check(Int x)
{
	vi digit;
	Int temp=x;
	while(x!=0)
	{
		digit.pb(x%10);
		x/=10;	
	}
	reverse(digit.begin(),digit.end());
	if(digit.size()==1)
	{
		return temp;
	}

	for(int i=0;i<digit.size()-1;i++)
	{
		if(digit[i]>digit[i+1])
		{
			digit[i]--;
			for(int j=i+1;j<digit.size();j++)
			{
				digit[j]=9;
			}
		}
	}
	Int ans=0;

	for(int i= 0;i<digit.size();i++)
	{
		ans=ans*10;
		ans+=digit[i];
	}
	return ans;
}
Int check2(Int x)
{
	vi digit;
	Int temp=x;
	while(x!=0)
	{
		digit.pb(x%10);
		x/=10;	
	}
	reverse(digit.begin(),digit.end());
	if(digit.size()==1)
	{
		return true;
	}

	for(int i=0;i<digit.size()-1;i++)
	{
		if(digit[i]>digit[i+1])
		{
			return false;
		}
	}
	return true;
}

Int check1(Int N)
{
	while(1)
	{
		Int ans=check(N);
		if(check2(ans))
			return ans;
		N=ans;
	}
}

int main()
{
	

	
	cin>>T;
	for(int z=1;z<=T;z++)
	{
		Int ans=0;
		cin>>N;
		ans=check1(N);
		


		printf("Case #%lld: %lld\n",z,ans);
	}
}