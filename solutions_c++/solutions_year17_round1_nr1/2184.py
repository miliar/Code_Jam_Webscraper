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
#include <sstream>
using namespace std;

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("A-large.out");
	int t;
	fin>>t;
	for(int ii=0;ii<t;ii++){
		int n,m;
		fin>>n>>m;
		char c[n][m];
		int R[n];
		int r[n];
		for(int jj=0;jj<n;jj++){
			r[jj]=-1;
			for(int zz=0;zz<m;zz++){
				fin>> c[jj][zz];
				if(c[jj][zz]!='?' && r[jj]==-1){
					r[jj]=jj;
					R[jj]=zz;
				}
			}
		}
		int near=-1;
		for(int jj=0;jj<n;jj++){
			if(r[jj]==jj){
				if(near==-1){
					for(int zz=0;zz<jj;zz++)r[zz]=jj;
				}
				near=jj;
				int x=R[jj];
				for(int zz=0;zz<m;zz++){
					if(c[jj][zz]=='?'){
						c[jj][zz]=c[jj][x];
					}
					else{
						x=zz;
					}
				}
			}
			else{
				r[jj]=near;
			}
		}
		fout << "Case #"<<ii+1<<":"<<endl;
		for(int jj=0;jj<n;jj++){
			for(int zz=0;zz<m;zz++){
				fout << c[r[jj]][zz];
			}
			fout << endl;
		}

	}
	return 0;
}
