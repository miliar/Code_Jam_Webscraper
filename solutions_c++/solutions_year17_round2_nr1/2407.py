#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <ctime>
#include <cctype>
#include <cstring>
#include <bitset>
#include <algorithm>
#include <iomanip>
#include <string>

#define ld long double
#define ll long long
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define y0 _y0
#define y1 _y1

using namespace std;

int d, n;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("outputA.txt","w",stdout);
	
	int t;
	cin >> t;
	for (int ii = 1; ii <= t; ii++){
		double timeToArrive = 0;
		cin >> d >> n;
		for (int i = 0; i < n; i++){
			int k, s;
			cin >> k >> s;
			timeToArrive = max(1.0*(d-k)/s, timeToArrive);
		}
		
				
		cout.precision(9);
		cout << "Case #" << ii << ": " << d*1.0/timeToArrive << fixed << endl;;

	}

 	return 0;
}
