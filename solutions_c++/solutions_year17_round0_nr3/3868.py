#include<bits/stdc++.h>
using namespace std;

#define MAX 1000005


struct compare {
	bool operator()(pair<int,int> x,pair<int,int> y) {
		int len1 = x.second - x.first + 1;
		int len2 = y.second - y.first + 1;
		return len1>len2;
	}
};

multiset<pair<int,int>,compare> collection;

int main() {
	
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	
	int t;
	cin>>t;
	
	for(int tst = 1;tst<=t;tst++) {
		
		int n,k;
		cin>>n>>k;
		collection.clear();
		collection.insert(make_pair(1,n+2));
		
		for(int i =0;i<k-1;i++) {
			
			pair<int,int> top = *(collection.begin());
		//	cout<<top.first<<" "<<top.second<<endl;
			set<pair<int,int>,compare >::iterator it = collection.begin();
			collection.erase(it);
			
			int len = max(top.second - top.first - 1,0);
		//	cout<<collection.size()<<" "<<len<<endl;
			int mid = (len+1)/2;
			
		//	cout<<top.first<<" "<<top.first+mid<<endl;
			collection.insert(make_pair(top.first,top.first+mid));
			
		//	cout<<top.first+mid<<" "<<top.second<<endl;
			collection.insert(make_pair(top.first+mid,top.second));
			
		/*	for(set<pair<int,int>,compare >::iterator it = collection.begin();it!=collection.end();it++) {
				pair<int,int> temp = *it;
				cout<<"["<<temp.first<<","<<temp.second<<"] ";
			}
			cout<<endl;*/
		}
		
		pair<int,int> top = (*collection.begin());
	
		int len = max(top.second - top.first - 1,0);
		int mid = (len+1)/2;
		
		int side1 = max(top.first + mid - top.first - 1,0);
		int side2 = max(top.second - (top.first+mid) -1,0);
		cout<<"Case #"<<tst<<": "<<max(side1,side2)<<" "<<min(side1,side2)<<endl;
	}
	
	return 0;
}
