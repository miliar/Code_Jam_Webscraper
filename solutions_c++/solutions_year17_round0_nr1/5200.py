#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>

#define endl "\n"

using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<ll,ll> pll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;


int main(){
	ios::sync_with_stdio(0);

	int T, n;
	string str;
	cin >> T;
	for(int i = 1; i <= T; i++){
		cout << "Case #" << i << ": ";

		cin >> str >> n;
		int cnt = 0;
		while(true){
			while(str.size() > 0 && str[0] == '+') str = str.substr(1);
			if(str.size() < n) break;
			cnt++;
			for(int i = 0; i < n; i++){
				if(str[i] == '+') str[i] = '-';
				else str[i] = '+';
			}
		}


		if( str.size() == 0 ) cout << cnt;
		else cout << "IMPOSSIBLE";

		cout << endl;
//Case #2: 0
//Case #3: IMPOSSIBLE

	}

	
}
