#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
	ll tc;
	ll k,n,ans1,ans2,temp,lft,rgt,f;
	cin>>tc;
	for(int t=1;t<=tc;t++){
		vector<ll> myheap;
		cin>>n>>k;
		myheap.push_back(n);
		make_heap(myheap.begin(),myheap.end());
		for(int i=0;i<k;++i){
			f=myheap.front();
			pop_heap(myheap.begin(),myheap.end());
			myheap.pop_back();
			if(f>1){
				lft=(f-1)/2;
				rgt=f-lft-1;
				myheap.push_back(lft);
				push_heap(myheap.begin(),myheap.end());
				myheap.push_back(rgt);
				push_heap(myheap.begin(),myheap.end());
			}
		}
		if(f==1){
			ans1=0;
			ans2=0;
		}
		else{
			ans1=(f-1)/2;
			ans2=f-ans1-1;
			if(ans1<ans2){
				temp=ans1;
				ans1=ans2;
				ans2=temp;
			}
		}
		cout<<"Case #"<<t<<": "<<ans1<<" "<<ans2<<endl;
	}	
	return 0;
}