#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <unordered_map>
#include <set>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;

#define IN_FILE "inputlol.in"
#define OUT_FILE "outputlol.txt"

pair<long long int,long long int> p[1009];
set< pair<double,double> > s;
pair<double,double> temp1,temp2,temp3;

int main() {
	ios::sync_with_stdio(0);
	
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	
	long long int i,j,t1,t2,t3,t4,t,cnt=0,dis,n;
	double ans,p1,p2,p3,p4,temp;
	cin>>t;
	while(t--){
		cin>>dis>>n;
		s.clear();
		p1=0;
		for(i=0;i<n;i++){
			cin>>p[i].first>>p[i].second;
			temp=(dis-p[i].first)/(double)p[i].second;
			if(temp-p1>1e-7)
				p1=temp;
		}
		cnt++;
		ans=(double)dis/p1;
		cout<<"Case #"<<cnt<<": "<<std::fixed<<std::setprecision(6)<<ans<<endl;
	}
	return 0;
}

