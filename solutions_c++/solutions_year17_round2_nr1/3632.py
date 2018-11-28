/*
 * GCJ_17_1B_A.cpp
 *
 *  Created on: 22-Apr-2017
 *      Author: neeraj
 */


#include<iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/A-large.in", ios::in);
	fout.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/A-large-out.txt",ios::trunc);
	int t;
	fin>>t;
	for(int tt=1;tt<=t;tt++) {
		double d;
		int n;
		fin>>d>>n;
		double k[n],s[n];
		double maxx=0;
		for(int i=0;i<n;i++) {
			fin>>k[i]>>s[i];
			maxx = max(maxx,(d-k[i])/s[i]);
		}
		double ans = d/maxx;
		fout << "Case #" << tt << ": ";
		fout<<std::setprecision(6)<<std::fixed<<ans<<"\n";
	}
}

