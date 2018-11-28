#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <utility>
#include <cmath>
#define pi 3.14159265359
using namespace std;
long double getAr(vector<pair<double, double> > v){
	/*struct c{
		inline bool operator() (const pair<double,double>& p1, const pair<double, double>& p2)
	    {
	    	double a1 = pi*(p1.first*p1.first + 2*p1.first*p1.second);
	    	double a2 = pi*(p2.first*p2.first + 2*p2.first*p2.second);
	        return a1 > a2;
	    }
	}*/
	long double res = 0;
	sort(v.begin(), v.end(), less<pair<double, double> >() );
	int n = v.size();
	for(int i = 0; i < n-1; i++){
		res+= pi*(v[i+1].first*v[i+1].first - v[i].first*v[i].first);
	}
	res += pi*v[0].first*v[0].first;
	for(int i = 0; i < n; i++)
		res+= 2*pi*v[i].first*v[i].second;
	//cout<<res<<endl;
	return res;
}
long double getMax(vector<pair<double, double> > v, int i, int k){
	if(v.size() == k)
		return getAr(v);
	if(v.size() < k || i >= v.size())
		return 0;
	//cout<<"Array"<<endl;
	/*for(int i = 0; i < v.size(); i++){
		cout<<v[i].first<<" "<<v[i].second<<endl;
	}*/
	long double a1 = getMax(v, i+1, k);
	v.erase(v.begin()+i);
	long double a2 = getMax(v, i, k);
	return max(a1, a2);
}
int main(){
	int t = 0;
	cin>>t;
	for(int l = 1; l <= t; l++){	
		int n = 0, k = 0;
		cin>>n>>k;
		vector<pair<double, double> > v(n);
		for(int i = 0; i < n; i++){
			double r = 0, h = 0;
			cin>>r>>h;
			v[i] = make_pair(r, h);
		}
		long double res = getMax(v, 0, k);

		cout<<"Case #"<<l<<": ";
		printf("%.6Lf\n", res);
	}
	return 0;
}