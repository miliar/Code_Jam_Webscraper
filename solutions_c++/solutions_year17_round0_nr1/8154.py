/*
 * GCJ_17_A.cpp
 *
 *  Created on: 08-Apr-2017
 *      Author: neeraj
 */

#include<iostream>
#include <fstream>
using namespace std;


int main()
{
	int t;

	ifstream fin;
	ofstream fout;
	fin.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/A-large.in", ios::in);
	fout.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/A-large-out.txt",ios::trunc);

	fin>>t;
	for(int test=1;test<=t;test++)
	{
		string str;
		int k;
		fin>>str>>k;
		int sz = str.size();
		int s[sz],a[sz];
		for(int i=0;i<sz;i++) {
			s[i]=0;
			a[i]=str[i]=='+'?1:0;
		}
		int sum=0,ans=0,f=1;
		for(int i=0;i<sz;i++) {
			s[i] = (a[i]+sum)%2!=1;
			sum += s[i]-(i>=k-1?s[i-k+1]:0);
			ans += s[i];
			if(i>sz-k && s[i]!=0) {
				fout<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
				f=0;
				break;
			}
		}
		if(f)
			fout<<"Case #"<<test<<": "<<ans<<endl;
	}
}
