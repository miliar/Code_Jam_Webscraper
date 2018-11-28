#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	std::ifstream input;
    input.open("input.cpp");
    std::ofstream output;
    output.open("output.cpp");
	input>>t;
	for(int tc=1;tc<=t;tc++){
		int n,k;
		int mid,low,high;
		input>>n>>k;
		int array[1005];
		bool h[1005]={0};
		for(int i=1;i<=n+2;++i)
			array[i] = i;
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
				if(abs(array[j]-array[c])>ans){
					ans = array[j]-array[c];
					pos = (array[j]+array[c])/2;
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
		int r_s = x-mid;

		for( x = mid-1;x>=1;--x){
			if(h[x])
			break;
		}
		int l_s = mid-x;

		output<<"Case #"<<tc<<": "<<max(r_s,l_s)-1<<" "<<min(r_s,l_s)-1<<endl;
	}
	return 0;
}
