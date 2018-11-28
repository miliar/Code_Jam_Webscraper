#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	cout.precision(17);
	for(int i=1; i<=T; i++) {
		int N;
		cin>>N;
		pair<int,int> col[6];
		int sum = 0;
		string sol = "RVYVBV";
		string ans = "";
		int a;
		for(int j=0;j<6;j++) {
			cin>>a;
			col[j] = make_pair(a, j);
			sum+=a;
		}
		sort(col, col+6);
		//cout<<col[5].second<<endl;
		if(col[5].first>(col[3].first+col[4].first)) {
			ans = "IMPOSSIBLE";
			printf("Case #%d: ", i);
			cout<<ans<<endl;
		}else{
			//cout<<sum<<endl;
			int j =0;
			while(col[4].first>0) {
				
				if(col[5].first > 0)
					//cout<<sol[col[5].second]<<endl;
					ans += sol[col[5].second];
					//cout<<ans<<endl;
				j++;
				col[5].first--;
				if(col[4].first > 0)
					//cout<<sol[col[4].second]<<endl;
					ans += sol[col[4].second];
				j++;
				col[4].first--;
				
			}
			// cout<<"Here"<<endl;
			while(col[5].first > 0) {
				if(col[5].first > 0)
					//cout<<sol[col[5].second]<<endl;
					ans += sol[col[5].second];
					//cout<<ans<<endl;
				j++;
				col[5].first--;
				if(col[3].first > 0)
					//cout<<sol[col[4].second]<<endl;
					ans += sol[col[3].second];
				j++;
				col[3].first--;
			}
			// cout<<"Here"<<endl;
			int k = 1;
			string s = "";
			s += sol[col[3].second];
			while(col[3].first > 0) {
				//cout<<col[3].first<<endl;
				ans.insert(k, s);
				col[3].first--;
				k+=3;
			}
			printf("Case #%d: ", i);
			cout<<ans<<endl;
		}
		//cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}