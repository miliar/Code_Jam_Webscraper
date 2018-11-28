#include <stdio.h>
#include <string>
#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <list>
#include <cstdlib>
#include <time.h>
using namespace std;

//Google Code Jam 2017 Qualification Round, Problem C code.google.com/codejam
//Disable warning messages C4996.
#pragma warning(disable:4996)

#define INPUT_FROM 0
#if INPUT_FROM
#define fromc from
#else
#define fromc cin
#endif

//long long fr(vector<long long>&, long long);
string lltostr(long long);

int main(int argc, char **argv)
{
	//ifstream from;
	const int nmin = 1, nmax = 5;
	int test, cases, n, m, mt, res, i, j, k, t, rt, ax, bx;
	int i0, i1, j0, j1, t0, t1, r, c;
	int a, b, a0, a1, r0, r1;
	long long qq, xx, yy, zz, jj, kk, nn;
	char ch, ch0, ch1;
	//string sres[2]={"YES", "NO"};
	//string s, st, sr, s0, s1, s2;
	//long double dt;

	//if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	//static long long v[nmax+1], v10[pmax], vt[pmax];
	//vector<int> v, vr;
	//vector<vector<int> > vv;
	//static long long vr[qmax];
	//deque<int> dq, dq0, dq1, dq2;
	//map<char, int> mc;
	map<long long, long long> mii;
	map<long long, long long >::iterator it;
	//map<long long, vector<long long> > miv;
	//map<long long, vector<long long> >::iterator it;
	//typedef map<string, long long>::const_iterator CI;
	//time_t ltime0, ltime1;

	//time(&ltime0);

	scanf("%d\n", &cases);
	//fromc>>cases;
	for(int test = 1;test <= cases;++test){
		scanf("%lld %lld\n", &nn, &kk);
		//cin >> n >> xx;

		mii[nn] = 1;

		yy = zz = -1;
		while(kk){
			it = mii.end();
			--it;
			qq = it->first;
			xx = it->second;
			mii.erase(it);
			if(kk <= xx){
				--qq;
				yy = zz = (qq>>1);
				if(qq&1) ++yy;
				kk = 0;
			}else{
				kk -= xx;
				if(qq&1){
					qq >>= 1; // kk <= nn => "> 0"
					xx <<= 1;
					if(mii.count(qq)) mii[qq] += xx;
					else mii[qq] = xx;
				}else{
					qq >>= 1; // > 0
					if(mii.count(qq)) mii[qq] += xx;
					else mii[qq] = xx;

					--qq;
					if(qq){
						if(mii.count(qq)) mii[qq] += xx;
						else mii[qq] = xx;
					}
				}
			}
		
		}


		printf("Case #%d: %lld %lld\n", test, yy, zz);

		//if(ax==0) cout << "Case #" << test << ": " << "NO"  << endl;
		//else      cout << "Case #" << test << ": " << "YES" << endl;

		//printf("%lld\n", res);
		//cout<<"Case #"<<test<<": "<<res<<endl;
		mii.clear();
	}

	//time(&ltime1);

	//printf("Runtime in seconds:\t%ld\n", ltime1 - ltime0);

	return 0;
}

