#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <cstdlib>
#include <cstring>
using namespace std;

//Google Code Jam 2017 Round 1B, Problem A code.google.com/codejam
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
	int test, cases, n, m, mt, res, rt, i, j, k, t, ax, bx;
	int i0, i1, i2, j0, j1;
	int r, r0, r1, a, a0, a1, b, b0, b1, x, y;
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
	//map<char, char> mc;
	//map<long long, long long>::iterator it;
	//typedef map<string, long long>::const_iterator CI;


	scanf("%d\n", &cases);
	//cin >> cases;
	for(int test = 1;test <= cases;++test){
		//scanf("%d ", &n);
		//memset(w, 0, sizeof(w));
		//cin >> s;
		//memset(w, 0, n*sizeof(int));
		scanf("%d %d\n", &a1, &n);



		//vvc.resize(n);
		scanf("%d %d\n", &a0, &b0);
		for(int i = 0;i < n - 1;++i){

			scanf("%d %d\n", &a, &b);

			if(1LL*(a1 - a0)*b < 1LL*(a1 - a)*b0){
				a0 = a;
				b0 = b;
			}
		}


		dr = (1.0*a1/(a1 - a0))*b0;

		printf("Case #%d: %e\n", test, dr);


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
		//vvc.clear();
	}

	return 0;
}
