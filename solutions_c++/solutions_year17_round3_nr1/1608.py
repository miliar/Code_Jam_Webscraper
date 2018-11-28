#include <bits/stdc++.h>
const double PI  =3.141592653589793238463;

using namespace std;
int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		int n,k;
		cin>>n>>k;
		vector<pair<int,int>> a(n);
		for(int i=0;i<n;i++){
			cin>>a[i].first>>a[i].second;
		}
		sort(a.begin(),	a.end(),greater<pair<int,int>>());
		multiset<double> s;
		for(int i=0;i<n;i++){
			s.insert(2*PI*a[i].first*a[i].second);
		}
		double ans=0.0;
		for(int i=0;i<n-k+1;i++){
			double temp=0.0;
			temp+=PI*(double)a[i].first*a[i].first+2*PI*(double)a[i].first*a[i].second;
			auto it=s.find(2*PI*a[i].first*a[i].second);
			s.erase(it);
			auto its=s.rbegin();int c;
			for(its=s.rbegin(),c=0;its!=s.rend()&&c<k-1;its++,c++){
				temp+=*its;
			}
			if(temp>ans)
				ans=temp;
		}
		cout<<"Case #"<<t<<": ";printf("%.7f\n",ans);
	}
	return 0;
}