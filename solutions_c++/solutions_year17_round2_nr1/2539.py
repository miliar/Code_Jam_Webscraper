#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue> 
#include <cctype> 
#include <cassert>

using namespace std;

#define VV vector
#define PB push_back
#define SZ(v) ((int)(v).size()) 
#define ll long long
#define ld long double
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(decltype((b).begin()) a = (b).begin();a!=(b).end();++a)
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi VV<int>
#define vs VV<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))

#define PROB_ID "A"
#define INPUT_SIZE  "small" //"large" // 

typedef long double LD;


int main()
{
	//freopen("my_input.txt", "r", stdin);
	//freopen("my_output.txt", "w", stdout);

   freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	//freopen(PROB_ID "-" INPUT_SIZE "-attempt0.in", "r", stdin);
	//freopen(PROB_ID "-" INPUT_SIZE "-attempt0.out", "w", stdout);

	int T;
	scanf("%d\n", &T); // remember to put \n

	rep(i, T) {
		// inputs
		int D, N;
		scanf("%d %d\n", &D, &N); // remember to put \n
		//vector<int> K;
      //vector<int> S;
      double maxT = -1.0;
		rep(r, N) { // read each row
			int k, s;
         scanf("%d %d\n", &k, &s); // remember to put \n
         double dT = (double)(D - k) / double(s);
         if (maxT < dT) maxT = dT;
		}


		printf("Case #%d: %lf\n", i + 1, (double)D/ maxT);
	}
	return 0;
}

