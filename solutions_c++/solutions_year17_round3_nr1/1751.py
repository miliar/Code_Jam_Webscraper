#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <cstdlib>
#include <cstring>
using namespace std;

//Google Code Jam 2017 Round 1C, Problem A code.google.com/codejam
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
	const int nmin = 1, nmax = 1000, amax = 1000000000;
	const long double pi = 3.141592653589793;
	int test, cases, n, m, mt, res, rt, i, j, k, t, ax, bx;
	int i0, i1, i2, j0, j1, h, h0, h1;
	int r, r0, r1, a, a0, a1, b, b0, b1, x, y;
	long long rr, rrt, delta0, delta1;
	char ch, ch0;
	//string sres[2]={"YES", "NO"};
	//string sres[2]={"Bad magician!", "Volunteer cheated!"};
	string s, st, sr;
	long double dr, dt, dt0;

	//if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	//static int vv0[nmax][nmax], vv1[nmax][nmax];
	static int w[nmax];
	//vector<int> vr;
	vector<vector<char> > vvc;
	//deque<int> dq;
	multiset<pair<int, int> > ss;
	multiset<long long> ss0;
	multiset<pair<int, int> >::iterator it, it0, it1;
	//map<char, char> mc;
	//map<long long, long long>::iterator it;
	//typedef map<string, long long>::const_iterator CI;


	scanf("%d\n", &cases);
	//cin >> cases;
	for(int test = 1;test <= cases;++test){
		scanf("%d %d\n", &n, &k);
		//memset(w, 0, sizeof(w));
		//cin >> s;
		//memset(w, 0, n*sizeof(int));

		for(int i = 0;i < n;++i){
			scanf("%d %d\n", &r, &h);
			ss.insert(make_pair(r, h));
		}

		
		it0 = ss.begin();
		it1 = ss.end();
		rr = rrt = 0;
		r0 = 0;
		mt = 0;
		for(it = it0;it != it1;++it){
			r1 = it->first;
			h1 = it->second;
			if(r1 > r0){
				delta0 = 1LL*r1*r1 - 1LL*r0*r0;
			}else delta0 = 0;

			rrt += 2LL*r1*h1;

			//printf("%lld %llf\n", rrt, pi*rrt);
			++mt;
			if(mt > k){
				delta1 = -(*ss0.begin());
				//rrt -= *ss0.begin();
			}else delta1 = 0;

			if(rrt + delta0 + delta1 > rr){
				rrt += delta0 + delta1;
				rr = rrt;
				r0 = r1;
				if(mt > k){
					ss0.erase(ss0.begin());
				}
				ss0.insert(2LL*r1*h1);
			}else{
				ss0.insert(2LL*r1*h1);
				if(mt > k){
					rrt -= *ss0.begin();
					ss0.erase(ss0.begin());
				}
			}
		}


		dr = pi*rr;

		printf("Case #%d: %.12e\n", test, dr);


		//printf("Case #%d:\n", test);
		//for(int i = 0;i < n;++i){
		//	for(int j = 0;j < m;++j){
		//		ch = vvc[i][j];
		//		printf("%c", ch);
		//	}
		//	printf("\n");
		//}


		//if(r == -1) printf("Case #%d: IMPOSSIBLE\n", test);
		//else printf("Case #%d: %d\n", test, r);

		//cout<<"Case #"<<test<<": "<<r<<endl;
		//else if(t==0) cout<<"Case #"<<test<<": "<<sres[1]<<endl;
		//else cout<<"Case #"<<test<<": "<<sres[0]<<endl;

		//cout<<"Case #"<<test<<": "<<sres[ax]<<endl;
		ss0.clear();
		ss.clear();
	}

	return 0;
}
