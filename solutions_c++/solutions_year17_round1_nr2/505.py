/*
 * test.cpp
 *
 *  Created on: Sep 26, 2016
 *      Author: SCE15-0683
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

bool lesss(int a,int b){
	return 10*a<9*b;
}

bool belong(int a,int b){
	return 10*a>=9*b&&10*a<=11*b;
}

int main(){
	int tt;
	int test=0;
	cin>>tt;
	ofstream out;
	out.open("result.txt");
	while(tt--){
		test++;
		out<<"Case #"<<test<<": ";
		int n,p;
		cin>>n>>p;
		vector<int> r(n,0);
		for(int i=0;i<n;i++) cin>>r[i];
		vector<vector<int> > q(n,vector<int>(p,0));
		for(int i=0;i<n;i++){
			for(int j=0;j<p;j++){
				cin>>q[i][j];
			}
			sort(q[i].begin(),q[i].end());
		}
		vector<int> pos(n,0);
		int cnt = 0;
		for(int u=1;;){
			for(int i=0;i<n;i++){
				while(pos[i]<p&&lesss(q[i][pos[i]],u*r[i])) pos[i]++;
			}
			bool flag = true;
			for(int i=0;i<n;i++) {
				if(pos[i]>=p) {
					flag=false;
					break;
				}
			}
			if(!flag) break;


			flag = true;
			for(int i=0;i<n;i++){
				if(!belong(q[i][pos[i]],u*r[i])) {
					flag=false;
					break;
				}
			}
			if(!flag){
				u++;
				continue;
			}
			cnt++;
			for(int i=0;i<n;i++) pos[i]++;
		}
		out<<cnt<<endl;
	}
	out.close();
	return 0;
}
