#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
    ifstream input;
    input.open("input.cpp");
    ofstream output;
    output.open("output.cpp");
	int t;
	input>>t;
	for(int test=1;test<=t;test++)
    {
		int n,k,mid,low,high;
		int arr[1005];
		bool h[1005]={0};
		input>>n>>k;
		for(int i=1;i<=n+2;++i)
			arr[i] = i;
			low=1;
			high=n+2;
			h[low]=1;
			h[high]=1;
			int c=1;
			mid=(low+high)/2;
			int ans=0,pos;
			k--;
			int p=1,q=1;
		while(k--)
		{
			h[mid] = 1;
			c=1; ans=0;
			for(int j=1;j<=n+2;++j){
				if(h[j]==1)
            {
				if(abs(arr[j]-arr[c])>ans)
				{
					ans=arr[j]-arr[c];
					pos=(arr[j]+arr[c])/2;
				}
				c = j;

			}
			}
			mid = pos;
		}
		int x;
		for(x=mid+1;x<=n+2;++x){
			if(h[x])
			break;
		}
		int rs = x-mid;

		for( x = mid-1;x>=1;--x){
			if(h[x])
			break;
		}
		int ls = mid-x;
		output<<"Case #"<<test<<": "<<max(rs,ls)-1<<" "<<min(rs,ls)-1<<endl;
	}
	return 0;
}
