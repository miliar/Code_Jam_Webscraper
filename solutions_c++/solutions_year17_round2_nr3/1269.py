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

#define INF 2000000000000
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

int n, q;
pair <int, int> horse[10000];

int D[110][110];
int sumD[110];
double dp[110][110];

double fct(int pos, int currHorse) {
	if(pos == n-1) return 0;
	else if(dp[pos][currHorse] > -0.5) {
		return dp[pos][currHorse];
	}
	else {
		double mini = INF;
		//cout << D[pos][pos+1] << endl;
		if(sumD[pos+1] - sumD[currHorse] <= horse[currHorse].first) {
			mini = fct(pos+1, currHorse)+D[pos][pos+1]/(1.0*horse[currHorse].second);
		}
		if(horse[pos].first >= D[pos][pos+1])
			mini = min(mini, fct(pos+1, pos)+D[pos][pos+1]/(1.0*horse[pos].second));
			
		//cout << pos << " " << currHorse << " " << mini << endl;
		dp[pos][currHorse] = mini;
		return mini;
	}
}

signed main () {
	int nTest; cin >> nTest;
	
	for(int iTest = 0; iTest < nTest; iTest++) {
	
		for(int i= 0; i <110; i++) {
			for(int j= 0; j < 110; j++) {
				dp[i][j] = -1.0;
			}
		}
	
		cin >> n >> q;
		for(int i= 0; i < n; i++) {
			int energy, speed; cin >> energy >> speed;
			horse[i] = make_pair(energy, speed);
		}
		
		int sum = 0;
		sumD[0] = 0;
		for(int i = 0; i < n; i++) {
			for(int j= 0; j <n; j++) {
				int a; cin >> a;
				D[i][j] = a;

				if(i+1 == j) {sum += a; sumD[i+1] = sum;}
			}
		}
		sumD[n] = sumD[n-1];
		//for(int i =0; i <= n; i++) cout << sumD[i] << endl;
		/*if(iTest == 5) {
				for(int i = 0; i < n; i++) {
				cout << horse[i].first << " " << horse[i].second << " "<< sumD[i+1]  << endl;
				for(int j= 0; j <n; j++) {
					cout << 	D[i][j] << " ";


				}
				cout << endl;
			}
		}*/
		
		
		for(int i = 0; i < q; i++) {
			int a, b;
			cin >> a >> b;
			//cout << n << " " << q << endl;
			printf("Case #%lld: %lf\n", iTest+1, fct(0,0));
		}
		
	}
	
	return 0;
}
