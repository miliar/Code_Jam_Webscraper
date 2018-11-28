#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,tt;
	std::ifstream input;
    input.open("input.cpp");
    std::ofstream output;
    output.open("output.cpp");
	input>>t;
	for(tt=1;tt<=t;tt++){
		int n,k;
		int mid,low,high;
		input>>n>>k;
		int a[1004];
		bool h[1004]={0};
		for(int i=1;i<=n+2;++i)
			a[i] = i;
			low = 1; high = n+2;
			h[low]=1;
			h[high] = 1;
			int c=1;
			mid = (low+high)/2;
			int ans=0,pos;
			k--;
			int p=1,q=1;
		while(k--){
			//mid = (low+high)/2;
			h[mid] = 1;
			c=1;
			//c = 1;
			ans=0;
			for(int j=1;j<=n+2;++j){
				if(h[j]==1){
				if(abs(a[j]-a[c])>ans){
					ans = a[j]-a[c];
					pos = (a[j]+a[c])/2;
				//	c= j;
				}
				c = j;

			}}
			 mid = pos;
			 //cout<<mid<<endl;

		}
		int x;
		for( x = mid+1;x<=n+2;++x){
			if(h[x])
			break;
		}
		int rs = x-mid;

		for( x = mid-1;x>=1;--x){
			if(h[x])
			break;
		}
		int ls = mid-x;

		output<<"Case #"<<tt<<": "<<max(rs,ls)-1<<" "<<min(rs,ls)-1<<endl;
	}
	return 0;
}
