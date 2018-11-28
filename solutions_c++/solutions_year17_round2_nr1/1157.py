#include <bits/stdc++.h>

using namespace std;

int main(void){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	cin>>test;
	for(int t=1;t<=test;t++){
		int d,n;
		cin>>d>>n;
		vector<pair<int,int> > v(n);
		for(int i=0;i<v.size();i++)cin>>v[i].first>>v[i].second;
		sort(v.begin(),v.end());
		double mx = 1e20;
		
		for(int i=v.size()-1;i>=0;i--){
			int dist = d-v[i].first;
			double req_t = 1.0*dist/v[i].second;
			//~ cout<<i<<" "<<req_t<<" "<<mx<<" "<<(d/mx)<<endl;
			if(d/mx < req_t){
				mx = d/req_t;
			}
		}
		printf("Case #%d: %.6lf\n", t, mx);
		//~ cout<<"Case #"<<t<<": "<<mx<<endl;
	}
	return 0;
}
