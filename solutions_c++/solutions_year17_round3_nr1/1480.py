#include <iostream>
#include <string>
#include <queue>
#include <fstream>
#include <stdio.h>
#include <math.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <climits>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <iomanip>
using namespace std;

const double PI = atan(1) * 4;

typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<long long, long long> pll;

int n, k;
vector<pair<int, int> > pancakes;

double get_exposed_area(int last, int current){
	if(last == -1)
		return PI*pancakes[current].first * pancakes[current].first + 2 * PI * pancakes[current].first * pancakes[current].second;
	
	double r_1 = pancakes[last].first, h_1 = pancakes[last].second;
	double r_2 = pancakes[current].first, h_2 = pancakes[current].second;

	return 2*PI*r_2*h_2 + PI*r_2*r_2 - PI*r_1*r_1;
}
double dp[1001][1001];
bool dpseen[1001][1001];
double solve(int pancakes_left = k, int last_pancake = -1){
	if(pancakes_left == 0){
		return 0;
	}
	double& ret = dp[pancakes_left][last_pancake];
	if(dpseen[pancakes_left][last_pancake])
		return ret;
	double ans = 0;
	for(int i = last_pancake + 1; i < n - (pancakes_left - 1); i ++){
		ans = max(ans, get_exposed_area(last_pancake, i) + solve(pancakes_left - 1, i));
	}
	dpseen[pancakes_left][last_pancake] = true;
	return ret = ans;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "r+", stdout);
#endif
	int t; cin >> t;
	int case_num = 1;
	while(t--){
		memset(dp, -1, sizeof dp);
		memset(dpseen, false, sizeof dpseen);
		pancakes.clear();
		cin >> n >> k;
		for(int i = 0; i < n; i ++){
			int r, h;
			cin >> r >> h;
			pancakes.push_back(make_pair(r,h));
		}
		sort(pancakes.begin(), pancakes.end());
		cout << "Case #" << case_num ++ << ": " << fixed << setprecision(7) << solve() << endl;
	}

	return 0;
}
