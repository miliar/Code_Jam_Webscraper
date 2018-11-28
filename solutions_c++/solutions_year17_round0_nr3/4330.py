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
	fin.open("C-large.in");
	ofstream fout;
	fout.open("C-large.out");

	int t;
	fin>>t;
	for(int ii=0;ii<t;ii++){
		long long int n,k;
		fin>> n>>k;
		long long int p=1;
		long long int x=0;
		while(k>=p){
			p=p*2;
			x++;
		}
		x--;
		p=p/2;
		long long int m=(n-k)/((long long int ) pow(2,x));
		//cout << x<<" "<<p<<" " <<m<<" ";

		fout <<"Case #" << ii+1<<": "<<m/2 + m%2<< " "<<m/2 << endl;
	}
    return 0;
}


