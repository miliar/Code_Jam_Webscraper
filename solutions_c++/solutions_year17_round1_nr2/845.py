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

//Google Code Jam 2017 Round 1A, Problem B code.google.com/codejam
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
	const int nmin=1, nmax=1000, amax=1000000;
	int test, cases, n, nt, m, mt, res, rt, i, j, k, t, ax, bx, cx;
	int i0, i1, j0, j1;
	int k0, k1, k2;
	int a, a0, a1, r, r0, r1;
	long long rrt, aa, ff, cc, xx, yy;
	//char ch;
	//string sres[2]={"YES", "NO"};
	string s, st, sr;
	//long double dt, dt0, dt1;
	//long double dc, df, dx, dy;


	//if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	vector<int> v, vi, vt;
	vector<vector<int> > vv;
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
		scanf("%d %d\n", &n, &m);
		//cin >> s;
		//n = s.size();

		v.resize(n);
		vi.resize(n, 0);
		vv.resize(n);
		vt.resize(n);
		for(int i = 0; i < n;++i){
			scanf("%d", &a);
			v[i] = a;
		}

		for(int i = 0; i < n;++i){
			vv[i].resize(m);
			for(int j = 0; j < m;++j){
				scanf("%d", &a);
				vv[i][j] = a;
			}
		}

		for(int i = 0; i < n;++i){
			sort(vv[i].begin(), vv[i].end());
		}

		r = 0;
		ax = 1;
		for(int t = 1; (t <= amax)&&ax;++t){// multiplier
			for(int i = 0; (i < n)&&ax;++i){
				//rt = t*v[i];
				if(9LL*t*v[i] > amax*10LL) ax = 0;
				if(vi[i] == m) ax = 0;
			}

			if(ax){
				bx = 1;
				for(int i = 0; (i < n)&&bx;++i){
					rrt = 1LL*t*v[i];
					cx = 0;
					for(int j = vi[i]; (j < m)&&(bx == 1)&&(cx == 0);++j){
						if(vv[i][j]*10LL < rrt*9LL) ++vi[i];
						else if(vv[i][j]*10LL > rrt*11LL) bx = 0;
						else{
							vt[i] = j + 1;
							cx = 1;
						}
					}
					if(bx) bx = cx;
				}
				if(bx){
					for(int i = 0; i < n;++i) vi[i] = vt[i];
					++r;
					--t;	// check the same t next time
				}
			}
		}

		

		printf("Case #%d: %d\n", test, r);
		//cout<<"Case #"<< test << ": " << sr <<endl;
		//cout<<"Case #"<< test << ": " << r <<endl;
		//printf("Case #%d: %.7Lf\n", test, dt);

		//cout<<"Case #"<<test<<": "<<sres[1-ax]<<endl;
		v.clear();
		vi.clear();
		vt.clear();
		vv.clear();
	}

	return 0;
}
