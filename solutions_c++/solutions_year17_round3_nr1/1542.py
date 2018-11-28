#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <string.h>
#include <cstdio>
using namespace std;

double pi = 3.14159265358979;
double dp[1001][1001] = {0};

int main() {
	// your code goes here
	int t, n, k;
	double r, h;
	cin >> t;
	for (int l = 1; l <= t; l++) {
	    cin >> n >> k;
	    vector < pair <double, double> > p(n);
	    for (int x = 0; x < n; x++) {
	        cin >> p[x].first >> p[x].second;
	    }
	    sort (p.begin(), p.end());
	    double total = 0;
	    //cout << p[n - 1].first << " " << p[n - 1].second << endl;
	    dp[n - 1][1] += pi*pow(p[n - 1].first, 2)+(double)2*p[n - 1].first*pi*p[n - 1].second;
	    for (int x = n - 1; x >= 0; x--) {
	        dp[x][1] = (double)2*p[x].first*pi*p[x].second + pi*pow(p[x].first, 2); 
	        if (x < n - 1) {
	            dp[x][1] = max (dp[x + 1][1], dp[x][1]);
	        }
	        for (int i = 1; i < 1001; i++) {
	            if (x < n - 1) {
	            dp[x][i] = max((double)2*p[x].first*pi*p[x].second + dp[x + 1][i - 1], dp[x][i]);
	            dp[x][i] = max (dp[x][i], dp[x + 1][i]);
	            }
	            dp[x][i] = max (dp[x][i], dp[x][i - 1]);
	            if (i == k) {
	                total = max (total, dp[x][i]);
	            }
	        }
	    }
	    //cout << total << endl;
	    if (l == 2) {
	        /*for (int x = 0; x < n; x++) {
	            for (int i = 1; i <= k; i++) {
	                cout << dp[x][i] << " ";
	            } cout << endl;
	        }*/
	    }
	    printf ("Case #%d: %.9f\n", l, total);
	    memset(dp, 0, sizeof(double)*1001*1001);
	}
	return 0;
}