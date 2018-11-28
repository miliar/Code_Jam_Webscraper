#include <iostream>
#include <string>
#include <utility>
#include <math.h>
#include <vector>
#include <algorithm>
#define _USE_MATH_DEFINES
using namespace std;
bool pairCompare(pair<pair<long long, long long>, long long>& firstElem, pair<pair<long long, long long>, long long>& secondElem) {
	if(firstElem.first.first == secondElem.first.first) return firstElem.first.second < secondElem.first.second;
 	return firstElem.first.first < secondElem.first.first;

}
bool pairCompare2(pair<long long,long long>& firstElem, pair<long long,long long>& secondElem) {
 	return firstElem.first < secondElem.first;

}
int main() {
	freopen ("output.txt","w",stdout);
	freopen ("A-large.in","r",stdin);
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		cout<<"Case #"<<i+1<<": ";
		int n,k;
		cin>>n>>k;
		int r[n],h[n];
		for(int j=0;j<n;j++){
			cin>>r[j]>>h[j];
		}
		vector<pair<pair<long long,long long>,long long> > a;
		for(int j=0;j<n;j++){
			a.push_back(make_pair(make_pair(r[j],h[j]),j));
		}
		
		sort(a.begin(), a.end(), pairCompare);
		
        double ans=0.0;
        double maxAns=0.0;
        for (int j=n-1;j>=k-1;j--){
        	ans=M_PI*double(a[j].first.first*(a[j].first.first+2*a[j].first.second));
        	
        	vector<pair<long long,long long> > b;
        	for(int l=j-1;l>=0;l--){
        		b.push_back(make_pair(a[l].first.first*a[l].first.second,a[l].second));
			}
			sort(b.begin(), b.end(), pairCompare2);
			for(int l=j-1;l>j-k;l--){
				ans+=(2.0*M_PI*double(b[l].first));
			}
			if(ans>maxAns) maxAns=ans;
			
		}  
        printf ("%.10f", maxAns);
		cout<<endl;
	}
	
	return 0;
}
