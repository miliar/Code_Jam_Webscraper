#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <bitset>
#include <cstdio>
#include <sstream>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <set>
#include <cctype>
#include <iomanip>
#include <list>
#include <cstring>

#define INF 2000000000
#define ull unsigned long long int
#define vi vector<int>
#define vii vector<ii>
#define int long long int

#define UNVISITED 0
#define OPENED 1
#define CLOSED 2

#define PI 3.14159265359

#define D(x) cout<<#x<<" : "<<x<<endl
#define P(x) cout << x << endl;

using namespace std;

signed main () {
	int nTest; cin >> nTest;
	for(int iTest = 0; iTest < nTest; iTest++) {
		int d,  n;
		cin >> d >> n;
		
		double maxi = 0; 
		
		for(int i = 0; i <n; i++) {
			int a, b;
			cin >> a >> b; 
			double t = (d-a)/(1.0*b);
			maxi = max(maxi, t);

		}

		printf("Case #%lld: %lf\n", iTest+1, d/(1.0*maxi));
	}
	return 0;
}
