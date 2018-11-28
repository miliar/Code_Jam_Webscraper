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
string s; int k;

void flip(int i) {
	for(int j = i; j < i+k; j++) {
		if(s[j] == '+') s[j] = '-';
		else s[j] = '+';
	}
}

int main () {
	int nTest; scanf("%d\n", &nTest);
	
	for(int iTest = 0; iTest  < nTest; iTest++) {
	

		cin >> s;
		scanf("%d", &k);
		int ans = 0;
		for(int i= 0; i <= s.size()-k; i++) {

			if(s[i] == '-') {
				flip(i);
				ans++;
			}		
		}
		bool ok = true;
		for(int i = 0; i < s.size(); i++) {
			if(s[i] == '-') ok = false;
		}				
		if(ok)
		printf("Case #%d: %d\n", iTest+1,ans);
		else
		printf("Case #%d: IMPOSSIBLE\n", iTest+1);
	}
    return 0;
}
