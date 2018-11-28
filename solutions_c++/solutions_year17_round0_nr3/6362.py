/*
 * GCJ_17_C.cpp
 *
 *  Created on: 08-Apr-2017
 *      Author: neeraj
 */

#include<iostream>
#include <fstream>
#include<vector>
#include<climits>
#include<cmath>
#include <queue>
using namespace std;

typedef long long int lli;

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/C-small-2-attempt2.in",ios::in);
	fout.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/C-small-out-2.txt",ios::trunc);

	int tc;
	fin >> tc;
	for(int i=0;i<tc;i++) {
		lli n,k;
		std::priority_queue<lli> loc;
		fin >> n >> k;
		lli j=1, ls, rs;
		lli curr = n;
		while(j<=k && curr>0) {
			if(!loc.empty()) {
				curr = loc.top();
				loc.pop();
			}

			if(curr>0) {
				if(curr%2==0) {
					ls = (curr/2)-1;
					rs = curr/2;
				} else {
					ls = (curr-1)/2;
					rs = (curr-1)/2;
				}
			}

			loc.push(rs);
			loc.push(ls);
			j++;
		}
		fout << "Case #" << i+1 << ": " << rs << " " << ls << endl;
	}

}
