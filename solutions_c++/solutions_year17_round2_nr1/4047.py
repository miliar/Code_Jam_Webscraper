#include <bits/stdc++.h>
using namespace std;

int main() {
	//freopen("in.in", "rt", stdin);
	int tc;
	cin>>tc;
	for(int z=1;z<=tc;z++){
		int n;
		double d;
		cin>>d>>n;
		double t=0;
		vector<pair<double,long long> > arr(n);
		for(int i=0;i<n;i++) cin>>arr[i].first>>arr[i].second;
		sort(arr.rbegin(),arr.rend());
		for(int i=0;i<n-1;i++){
			if(arr[i].first==arr[i+1].first){
				arr[i+1].first=min(arr[i+1].first,arr[i].first);
				continue;
			}
			if(arr[i].second>=arr[i+1].second) continue;
			double y=arr[i].first-arr[i+1].first,v1=arr[i+1].second,v2=arr[i].second;
			double x=(y*v2)/(v1-v2);
			//cout<<x<<" "<<y<<" "<<v1<<" "<<v2<<"\n";
			if(x+arr[i].first>=d) continue;
			arr[i+1].first=x+arr[i].first;
			arr[i+1].second=arr[i].second;
			t+=(x/v2);
		}
		t+=(d-(arr[n-1].first))/arr[n-1].second;
		//cout<<t<<"<<\n";
		double ans=d/t;
		cout<<"Case #"<<z<<": "<<fixed<<setprecision(6)<<ans<<"\n";
	}
}

