/*
 * test.cpp
 *
 *
 *      Author: Fireworks
 */

#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
#include<map>
#include<cmath>
#include<bitset>
#include<set>
#include<iomanip>
#include<fstream>
#include<bitset>
#include<cstring>
#include<cstdlib>
#include<complex>
#include<list>
#include<sstream>

using namespace std;

typedef pair<int,int> ii;
typedef pair<int,long long> il;
typedef pair<long long,long long> ll;
typedef pair<ll,int> lli;
typedef pair<long long,int> li;
typedef pair<double,double> dd;
typedef pair<ii,int> iii;
typedef pair<double,int> di;
long long mod = 1000000007LL;
long long base = 37;
long long large = 1000000000000000000LL;


int main(){


	int totalcase;
	int testcase=0;
	cin>>totalcase;
	ofstream out;
	out.open("result.txt");

	while(totalcase--){
		testcase++;
		out<<"Case #"<<testcase<<": ";
		cout<<testcase<<": "<<endl;

		//GOGOGO

		int n,p;
		cin>>n>>p;
		vector<int> a(p,0);
		for(int i=0;i<n;i++){
			int x;
			cin>>x;
			x%=p;
			x=p-x;
			x%=p;
			a[x]++;
		}
		int ans = a[0];
		if(p==2){
			if(a[1]>0) ans+=(a[1]-1)/2+1;
		}
		if(p==3){
			int t = min(a[1],a[2]);
			ans+=t;
			a[1]-=t;
			a[2]-=t;
			if(a[1]>0) ans+=(a[1]-1)/3+1;
			if(a[2]>0) ans+=(a[2]-1)/3+1;
		}
		if(p==4){

		}
		out<<ans<<endl;


		//END
	}
	out.close();

	return 0;
}
