#include <iostream>
#include <math.h>
#include <cmath>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <string>
#include <string.h>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <limits>
#include <list>
#include <functional>
#include <bitset>
#include <numeric>
#include <iomanip>
#include <ctime>
#include <ctype.h>
#include <stdio.h>

using namespace std;
typedef long long ll;
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define sz size()

ll t, n;
vector<int> vec;

bool calc(ll q) {
	while(q != 0) {
		vec.pb(q % 10);
		q /= 10;
	}
	for (int i = 0; i < vec.sz - 1; i++) 
		if (vec[i] < vec[i + 1]) 
			return false;
	return true;
}

int main()
{	
	ios_base::sync_with_stdio(0);
    	cin.tie(NULL); 
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
		for (ll j = n; j >= 0; j--) {
			if (calc(j)) {
				cout << "Case #" << i + 1 << ": " << j << endl;
				break;
			}
			vec.clear();
		}
		vec.clear();
	}


	
	return 0;
	//cerr << (double)clock() * 1.0 / CLOCKS_PER_SEC << endl;	                      	
}