//chiragjn
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <climits>
#include <iomanip>
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define gibe_de_fast_io_b0ss ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;
const ll mod = 1e9 + 7;
const ll INF = 0x7FFFFFFFFFFFFFFF/2;
int main(){
    gibe_de_fast_io_b0ss;
    int t;
    cin>>t;
    for(int T=1;T<=t;T++){
    	double ans = 0;
    	int n;
    	double dis;
    	cin>>dis>>n;
    	double x, y;
    	vector<pair<double, double>> xs(n);
    	for(int i=0;i<n;i++){
    		cin>>xs[i].ff>>xs[i].ss;
    	}
    	sort(xs.begin(), xs.end());
    	double lo = 0, hi = 1e18, best = -1;
    	double prevm = -1;
    	while(hi-lo > 1e-7){
    		double mid = (lo + hi)/2;
    		if(prevm == mid) break;
    		prevm = mid;
    		// cout<<mid<<"\n";
    		bool f = 0;
    		for(int i=0;i<n;i++){
    			x = xs[i].ff/(mid - xs[i].ss);
    			y = mid * x;
    			if(x > 0 && y < dis){
    				f = 1;
    				break;
    			}
    		}
    		if(f){
    			hi = mid;
    		}
    		else{
    			lo = mid;
    			best = max(mid, best);
    		}
    	}
    	cout<<"Case #"<<T<<": "<<setprecision(6)<<fixed<<best<<"\n";
    }
    return 0;
}
