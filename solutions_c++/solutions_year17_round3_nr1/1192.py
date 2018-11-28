#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;
double pi = 3.14159265358979323;

long long calc(vector<pair<long long,long long> >v,int j,int k){
	if(j+k-1>=v.size())return 0;
	vector<pair<long long,long long > > u;
	vector<long long>x;
	for(int i=j+1;i<v.size();i++){
		u.push_back(v[i]);
	}
	long long ans=0;
	ans +=v[j].first*v[j].first+2*v[j].first*v[j].second;
	for(int i=0;i<u.size();i++){
		x.push_back(2*u[i].first*u[i].second);
	}
	sort(x.begin(),x.end(),greater<long long>());
	for(int i=0;i<k-1;i++){
		ans += x[i];
	}
	return ans;
}


int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t; ++i){
		long long n,k,tmp1,tmp2;
		cin >> n >> k;
		vector<pair<long long ,long long> > v;
		for(int j=0;j<n;j++){
			cin >> tmp1 >> tmp2;
			v.push_back(make_pair(tmp1,tmp2));
		}
		sort(v.begin(),v.end(),greater<pair<long long,long long> >() );
		long long ans;
		long long max=0;
		for(int j=0;j<n;j++){
			ans = calc(v,j,k);
			if(max<ans){
				max = ans;
			}
		}
		cout.precision(15);
		std::cout.setf(std::ios_base::fixed,std::ios_base::floatfield);
		cout << "Case #" << i << ": " << max*pi << endl;
	}
	return 0;
}