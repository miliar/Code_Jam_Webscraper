#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <vector>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <fstream>
#include <iomanip>
#include <sstream>
using namespace std;

const long double pie=3.14159265358979323846;

struct pancake{
	int name;
	long double s;
	long long h;
};

bool operator<(pancake a,pancake b){
	return a.s<b.s;
}

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("A-large.out");

	int t;
	fin>> t;
	for(int tt=0;tt<t;tt++){
		int n,k;
		fin>>n>>k;
		pancake E[n];
		pancake A[n];
		for(int ii=0;ii<n;ii++){
			long double r,h;
			fin>>r>>h;
			E[ii].s=r*r;
			E[ii].name=ii;
			A[ii].s=(long double)2*r*h;
			E[ii].h=A[ii].s;
			A[ii].h=E[ii].s;
			A[ii].name=ii;
		}
		sort(E,E+n);
		sort(A,A+n);
		long double answer=0;
		for(int ii=n-1;ii>-1;ii--){
			long double cur=E[ii].s;
			int dum=k-1;
			int jj=n-1;
			bool found =false;
			while(dum>0 && jj>-1){
				//cout << dum<<" " <<jj<<" " <<A[jj].h<<" "<<ii<<endl;
				if(A[jj].h<=E[ii].s ){
					if(A[jj].name==E[ii].name)found =true;
					cur+=A[jj].s;
					jj--;
					dum--;
				}
				else{jj--;}
			}
			if(found ==false){
				cur+=E[ii].h;
			}
			else{
				for(int zz=jj;zz>-1;zz--){
					//cout << dum<<" zz " <<zz<<endl;
					if(A[zz].h<E[ii].s){
						cur+=A[zz].s;
						break;
					}
				}
			}
			if(cur>answer)answer=cur;
			cur=0.0;
		}
		fout <<"Case #"<<tt+1<<": "<< fixed<<setprecision(6)<<answer*pie<<endl;
		//cout<<(double)199*pie<<endl;
	}
	return 0;
}
