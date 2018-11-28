#include<bits/stdc++.h>
using namespace std;

#define lld long long

vector<pair<lld,lld> > store;

int main() {
	
	freopen("input.in","r",stdin);
	//freopen("output.txt","w",stdout);
	
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	
	
	
	int t;
	cin>>t;
	
	for(int tst = 1;tst<=t;tst++) {
		
		
		int d,n;
		cin>>d>>n;
		
		store.clear();
		
		for(int i = 0;i<n;i++) {
			int x,y;
			cin>>x>>y;
			store.push_back(make_pair(x,y));			
		}
			
		sort(store.begin(),store.end());
		
		lld sum = store[0].first;
		lld rem = 0ll + d  - sum;
		
		double v = ((1.00 * store[0].second * d)/(1.00 * rem));
		
		for(int i = 1;i<store.size();i++) {
			
			sum = store[i].first;
			rem = 0ll + d - sum;
			
			double temp = ((1.00 * store[i].second * d)/(1.00 * rem));
			v = min(temp,v);
		}
		
		cout.precision(10);
		cout<<"Case #"<<tst<<": "<<fixed<<v<<endl;
	}
	
	
	
	return 0;
}
