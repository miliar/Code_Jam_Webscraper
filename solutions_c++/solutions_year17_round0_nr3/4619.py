//IIT Kanpur FacelessMen India
#include <iostream>
#include <vector>
#include <cstdlib>
#define ull unsigned long long
using namespace std;
vector<ull int> getAns(ull n,ull k)
{
	vector<ull int> ans;
	if(k==1)
	{
		ull int l,r;
		ull int mid=(n+1)/2;
		l=mid-1;
		r=n-mid;
		if(l>r)
		{
			ans.push_back(l);
			ans.push_back(r);
		}
		else
		{
			ans.push_back(r);
			ans.push_back(l);
		}
		return ans;
	}
	else
	{
		ull int i;
		for(i=0;i<n;i++)
		{
			ull temp=((unsigned long int)1 << i);
			if(temp < k)
			{
				k-=temp;
				n-=temp;
			}
			else
				break;
		}
		ull int d = ((unsigned long int)1 << i);
		ull int m = n/d;
		ull int r = n%d;
		if(k<=r)
			return getAns(m+1,1);
		else
			return getAns(m,1);
	}
}
int main()
{ 
	int t;
	cin >> t;
	int z;
	for(z=0;z<t;z++)
	{
		ull int n,k;
		cin >> n;
		cin >> k;
		vector<ull int> ans = getAns(n,k);
		int i;
		cout << "Case #" << (z+1) << ": ";
		for(i=0;i<=1;i++)
			cout<< ans[i] <<" ";
		cout<<"\n";
	}
	return 0;
}
