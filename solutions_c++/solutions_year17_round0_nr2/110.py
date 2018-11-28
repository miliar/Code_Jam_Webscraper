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

int main(){
	int t;
	cin>>t;
	int test=0;
	ofstream out;
	out.open("result.txt");
	while(t--){
		test++;
		out<<"Case #"<<test<<": ";
		string s;
		cin>>s;
		if(s.length()==1){
			out<<s<<endl;
			continue;
		}
		int p=-1;
		for(int i=0;i<(int)s.length();i++){
			if(i&&s[i]<s[i-1]){
				p=i-1;
				break;
			}
		}
		if(p==-1) {
			out<<s<<endl;
			continue;
		}
		int pre = -1;
		for(int i=0;i<(int)s.length();i++){
			if(s[i]==s[p]) break;
			if(s[i]<s[p]) pre=i;
		}
		if(pre==-1){
			if(s[pre+1]=='1'){
				for(int i=0;i<(int)s.length()-1;i++) out<<'9';
				out<<endl;
				continue;
			}else{
				out<<(char)(s[pre+1]-1);
				for(int i=0;i<(int)s.length()-1;i++) out<<'9';
				out<<endl;
				continue;
			}
		}
		out<<s.substr(0,pre+1);
		out<<(char)(s[pre+1]-1);
		for(int i=pre+2;i<(int)s.length();i++) out<<'9';
		out<<endl;

	}

	out.close();
	return 0;
}
