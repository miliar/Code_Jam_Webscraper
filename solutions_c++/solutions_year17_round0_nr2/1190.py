#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <list>
#include <set>
#include <cstdlib>
#include <algorithm>
using namespace std;

//Google Code Jam 2017 Qualification Round, Problem B code.google.com/codejam
//Disable warning messages C4996.
#pragma warning(disable:4996)

#define INPUT_FROM 0
#if INPUT_FROM
#define fromc from
#else
#define fromc cin
#endif

//long long fr(vector<long long>&, long long);

int main(int argc, char **argv)
{
	//ifstream from;
	const int nmin=1, nmax=1000, amax=100000;
	int test, cases, n, nt, m, mt, res, rt, i, j, k, t, ax;
	int i0, i1, j0, j1;
	int k0, k1, k2;
	int a, a0, a1, r, r0, r1;
	long long aa, ff, cc, xx, yy;
	//char ch;
	//string sres[2]={"YES", "NO"};
	string s, st, sr;
	//long double dt, dt0, dt1;
	//long double dc, df, dx, dy;


	//if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	//vector<int> v;
	//vector<int>::iterator it, it0, it1;
	//deque<int> dq;
	//set<pair<int,int> > ss;
	//set<pair<int,int> >::iterator it, it0, it1;
	//pair<int,int> pr;
	//map<int, int> mi;
	//typedef map<string, long long>::const_iterator CI;

	scanf("%d\n", &cases);
	//fromc>>cases;
	for(int test = 1;test <= cases;++test){
		//scanf("%d\n", &n);
		cin >> s;

		n = s.size();

		//v.resize(n);
		nt = n;
		for(int i = n - 2; i >= 0;--i){
			if(s[i] > s[i + 1]){
				--s[i];
				for(int j = i + 1;j < nt;++j){
					s[j] = '9';
				}
				nt = i + 1;
			}
		}

		sr.clear();

		i0 = 0;
		while((i0 < n)&&(s[i0] == '0')) ++i0;
		for(int i = i0; i < n;++i) sr += s[i]; // s >= "...1" => sr != ""

		//v.clear();

		//printf("Case #%d: %d\n", test, r);
		cout<<"Case #"<< test << ": " << sr <<endl;
		//cout<<"Case #"<< test << ": " << r <<endl;
		//printf("Case #%d: %.7Lf\n", test, dt);

		//cout<<"Case #"<<test<<": "<<sres[1-ax]<<endl;
		sr.clear();
		s.clear();
	}

	return 0;
}
