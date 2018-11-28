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

#define UNVISITED 0
#define OPENED 1
#define CLOSED 2

#define PI 3.14159265359

#define dbg(x) cout<<#x<<" : "<<x<<endl


using namespace std;

long long int dp[50][20][20];

string s;
string rep;
long long int ans;
long long int fct(int pos, int left, bool smaller) {
	if(pos > 0) rep[pos-1] = left+'0';
	if(pos == s.size()) {
		if(ans == 0) {
			for(int i= 0; i < rep.size(); i++) {
			
				ans = (ans*10)+ (rep[i]-'0');
			 
			}
		}
		return 1;
	}
	else if(dp[pos][left][smaller] != -1) return dp[pos][left][smaller];
	else {
		long long int count = 0;
		if(smaller) {
			for(int i = s[pos]-'0'; i >= left; i--) {
				if(i == s[pos]-'0') count += fct(pos+1, i, true);
				else count += fct(pos+1, i, false);
			}
		}
		else {
			for(int i= 9; i >= left; i--) {
				count += fct(pos+1, i, false);
			}
		}
		
		dp[pos][left][smaller] = count;
		return count;
	}

}

int main () {
	int nTest = 1;
	scanf("%d", &nTest);
	
	for(int iTest = 1; iTest <= nTest; iTest++) {

		for(int i= 0; i < 50; i++) {
			for(int j= 0; j < 20; j++) {
				for(int k= 0; k < 20; k++) {
					dp[i][j][k] = -1;
				}
			}
		}
		
		cin >> s;
		rep = s;
		ans =0;
		fct(0, 0, true);		

		printf("Case #%d: %lld\n", iTest, ans);
	}
    return 0;
}
