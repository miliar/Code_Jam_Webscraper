#include <bits/stdc++.h>


using namespace std;
typedef long long ll;


int main(){
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("outCsmall2.txt","w",stdout);
	ll t,n;
	cin>>t;
	priority_queue<ll> left;
	priority_queue<ll> right;
	ll k;
	for(int z=1;z<=t;z++){
		cin>>n>>k;
		n--;
		ll mid;
		if (n%2==0){
			mid=n/2;
			left.push(mid);
			right.push(mid);
		}else{
			mid=n/2;
			left.push(mid);
			right.push(mid+1);
		}
		k--;
		ll l=left.top(),r=right.top(),temp;
		while(k--){
			l=left.top();
			r=right.top();
			if (l>r){
				left.pop();
				l--;
				temp=l/2;
				r=temp;
				l=l-r;
				left.push(l);
				right.push(r);
			}else {
				right.pop();
				r--;
				temp=r/2;
				l=temp;
				r=r-l;
				left.push(l);
				right.push(r);
			}
		}
		
		
		printf("Case #%d: ",z);
		cout<<max(l,r)<<" "<<min(l,r)<<endl;
		while(!left.empty()) {
	        left.pop();
	    }
	    while(!right.empty()) {
	        right.pop();
	    }
	    
	}
		
	
	return 0;
}

		
	
