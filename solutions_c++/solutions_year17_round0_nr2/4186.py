#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <algorithm>
#include <utility>
#include <string>
#include <cstring>
#include <cassert>
#include <cctype>
using namespace std;

int main() {
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("B-large.out");

	int t;
	fin>>t;
	for(int ii=0;ii<t;ii++){
		long long int n;
		fin>>n;
		long long int dum=n;
		int log=0;
		while(dum>0){
			dum=dum/10;
			log++;
		}
		int a[log];
		dum=n;
		for(int jj=log-1;jj>-1;jj--){
			a[jj]=dum%10;
			dum=dum/10;
		}
		int flag=0;
		for(int jj=1;jj<log;jj++){
			if(a[jj]<a[jj-1]){
				a[flag]--;
				for(int zz=flag+1;zz<log;zz++){
					a[zz]=9;
				}
				break;
			}
			if(a[jj]>a[jj-1])flag=jj;
		}
		long long int answer=0;
		for(int jj=0;jj<log;jj++){
			answer+=(long long int )pow(10,jj)*a[log-1-jj];
		}
		fout <<"Case #" << ii+1<<": "<<answer << endl;
	}
    return 0;
}


