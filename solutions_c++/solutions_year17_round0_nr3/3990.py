#pragma GCC optimize "Ofast,omit-frame-pointer,inline"
#include <bits/stdc++.h>
using namespace std;

struct Range{
	int left;
	int right;	
	Range(int l, int r){
		left = l;
		right = r;
	}
};

struct compare{
	bool operator()(const Range &a, const Range& b){
		int diff1 = a.right - a.left;
		int diff2 = b.right - b.left;
		if(diff1 == diff2){
			return a.left > b.left;
		}
		return diff1 < diff2;
	}
};

priority_queue<Range, vector<Range>, compare> ranges;

void splitRange(){
	Range r = ranges.top();
	// cout<<"splitting range : "<<r.left<<" "<<r.right<<endl;
	ranges.pop();
	if(r.left == r.right)
		return;
	else if(r.left + 1 == r.right){
		Range r(r.right, r.right);
		ranges.push(r);
	}
	else{
		int mid = (r.left + r.right)/2;
		Range r1(r.left, mid-1), r2(mid+1, r.right);
		ranges.push(r1);
		ranges.push(r2);	
	}
}

int main(){
    ios::sync_with_stdio(false);
    freopen("gcj3small2.in","r",stdin);
    freopen("gcj3out2.txt","w",stdout);
	int t,c=1,n,k;
    cin>>t;
    while(t--){
    	ranges = priority_queue<Range, vector<Range>, compare>();
    	cin>>n>>k;
    	Range t(0, n-1);
    	ranges.push(t);
    	for(int i=0;i<k-1;i++){
    		splitRange();
    	}
    	cout<<"Case #"<<c++<<": ";
    	Range r = ranges.top();
		if(r.left == r.right){
			cout<<"0 0"<<endl;
		}
		else if(r.left + 1 == r.right){
			cout<<"1 0"<<endl;
		}
		else{
			int mid = (r.left + r.right)/2;
			cout<<(r.right-(mid+1)+1)<<" "<<((mid-1)-r.left+1)<<endl;
		}
    }

	return 0;
}