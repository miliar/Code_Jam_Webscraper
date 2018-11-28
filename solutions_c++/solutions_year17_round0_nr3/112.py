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
long long mod = 1000000007LL;
long long base = 37;
long long large = 1000000000000000000LL;

long long f(map<long long,long long> x){
	long long sum = 0LL;
	for(map<long long,long long>::iterator it = x.begin();it!=x.end();it++){
		sum+=it->second;
	}
	return sum;
}

int main(){
	int t;
	cin>>t;
	int test=0;
	ofstream out;
	out.open("result.txt");
	while(t--){
		test++;
		out<<"Case #"<<test<<": ";
		long long n,k;
		cin>>n>>k;
		if(k==1LL){
			long long x = (n-1)/2LL;
			out<<n-1-x<<" "<<x<<endl;
			continue;
		}
		k--;
		map<long long,long long> c;
		long long x = (n-1)/2LL;
		c[x]++;
		c[n-1-x]++;
		while(k>f(c)){
			k-=f(c);
			map<long long,long long>::iterator it = c.begin();
			long long p1 = it->first;
			it++;
			map<long long,long long> temp;
			if(it==c.end()){
				long long x = (p1-1)/2;
				temp[x]+=c[p1];
				temp[p1-1-x]+=c[p1];
				c=temp;
			}else{
				long long p2 = it->first;
				long long x = (p1-1)/2LL;
				temp[x]+=c[p1];
				temp[p1-1-x]+=c[p1];
				x=(p2-1)/2LL;
				temp[x]+=c[p2];
				temp[p2-1-x]+=c[p2];
				c=temp;
			}
		}
		if(c.size()==1){
			map<long long,long long>::iterator it = c.begin();
			long long p = it->first;
			long long x = (p-1)/2;
			out<<p-1-x<<" "<<x<<endl;
		}else{
			map<long long,long long>::iterator it = c.begin();
			long long p1 = it->first;
			it++;
			long long p2 = it->first;
			long long x = (p2-1)/2;
			if(k<=c[p2]){
				out<<p2-1-x<<" "<<x<<endl;
			}else{
				x=(p1-1)/2;
				out<<p1-1-x<<" "<<x<<endl;
			}
		}


	}

	out.close();
	return 0;
}
