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

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt0.in");
	fout.open("A-small-attempt0.out");

	int t;
	fin>> t;
	for(int tt=0;tt<t;tt++){
		int n;
		double d;
		fin>>d>>n;
		double time[n+1];
		double u[n+1];
		double k[n+1];
		for(int ii=0;ii<n;ii++){
			fin>>k[ii+1]>>u[ii+1];
		}
		time[n]=(d-k[n])/u[n];
		for(int ii=n-1;ii>-1;ii--){
			double x=(k[ii+1]+time[ii+1]*u[ii+1]-k[ii])/time[ii+1];
			if(ii!=0)u[ii]=min(u[ii],x);
			else{u[0]=x;}
			time[ii]=(d-k[ii])/u[ii];
		}
		fout <<"Case #"<<tt+1<<": "<<fixed<<setprecision(6)<< u[0]<<endl;
	}
	return 0;
}
