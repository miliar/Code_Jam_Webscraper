#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <utility>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <sstream>
using namespace std;
typedef pair<long double,long double> ii;
long double d;
int n;
vector <ii> a;
bool f(long double speed){
	for(int i=0;i<n;i++){
		//cout<<speed<<":"<<(d-a[i].first)<<":"<<(d-a[i].first)/a[i].second<<endl;
		if(d*a[i].second<(d-a[i].first)*speed) return false;
	}
	return true;
}
int main(){
	ios_base::sync_with_stdio(false);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		cin>>d>>n;
		a.clear();
		for(int i=0;i<n;i++){
			long double k;
			long double p;
			cin>>k>>p;
			a.push_back(make_pair(k,p));
		}
		long double s=0;
		long double e=1e13;
		long double speed;
		while(abs(s-e)>1e-7){	
			speed=(s+e)/2;
			if(f(speed)) s=speed;
			else e=speed;
		}
		printf("Case #%d: %.6Lf\n",tc,speed);
	}
}
