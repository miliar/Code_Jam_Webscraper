//#include <bits/stdc++.h>

#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <string.h>
#include <iostream>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long number;
using namespace std;

inline number min (number a, number b) {
	return a <= b ? a : b;	
}

typedef struct horse_t {
	number K;
	number S;
	float t;
} horse;

inline float get_speed(number k1, number s1, number k2, number s2, number D) {
	float dt1 = ((k2 - k1)*1.0) / ((s1 - s2)*1.0);
	cout << dt1 << endl;
	float x = k1*1.0 + s1*dt1;
	
	if (!(x>=0 && x <= D)) return -1;
	
	
	float dt2 = ((D - x)*1.0) / (min(k1,k2)*1.0);
	

	
	cout << ( D*1.0 )/ (float)(dt1 + dt2);
	return 0;
}

int main(void) {
	int T,D,N;
	cin >> T;
	number x,y;
	
	for (int t = 0; t < T; t++) {
		cin >> D >> N;
		vector<horse*> H;
		int  max_ind = -1;
		for (int i = 0; i < N; i++) {
			cin >> x >> y;
			horse *h = new horse();
			h->K = x;
			h->S = y;
			h->t = ((D - h->K)*1.0) / (h->S*1.0);
			H.push_back(h); 
		}
		max_ind = 0;
		for (int i = 1; i < N; i++) {
			if (max_ind == -1 || H[max_ind]->t < H[i]->t) max_ind = i;
			
		}
		
		
		double b = (1.0*D) / H[max_ind]->t;
		printf("Case #%d: ", t+1);	
		printf("%.7f\n", b);
	}	

}
