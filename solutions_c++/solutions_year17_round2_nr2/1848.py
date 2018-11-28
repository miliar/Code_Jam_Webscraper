// problemB.cpp

#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <math.h>
#include <functional>
#include <sstream>
#include <cstring>
#include <set>
#include <map>
#include <cstdio>
#include <algorithm>
#include <bitset> 	
#include <ctime> 
#include <chrono>
#include <thread> 	
using namespace std;

// Shortcuts for "common" data types in contests

#define rep(i, a, b) for(int i = a; i < b; i++)
#define S(x) scanf("%d", &x)
#define S2(x, y) scanf("%d%d", &x, &y)
#define P(x) printf("%d\n", x)
#define all(v) v.begin(), v.end()
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

/*
	A mane with only one color of hair appears to be that color. For example, a mane with only blue hairs is blue.
	A mane with red and yellow hairs appears orange.
	A mane with yellow and blue hairs appears green.
	A mane with red and blue hairs appears violet.
*/

int arr[300];
int auxArr[300];
char colors[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

void resetArrs(){

	forn(i, 300){

		arr[i] = 0;
		auxArr[i] = 0;
	}
}

int activeColors(int n){

	int count = 0;

	forn(i, 6)
		count += (arr[colors[i]] > 0);

	return count;
}

bool isPossible(int n){

	forn(i, 6){

		// cout<<"auxArr["<<colors[i]<<"] = "<<auxArr[colors[i]]<<endl;
		// cout<<n<<"/2 = "<<n/2<<endl;

		if(auxArr[colors[i]] > n/2)
			return false;
	}

	return true;
}

struct color{

	int amount;
	char c;
	int index;
};

bool areGoodNeighbors(int prevColorIndex, int currColorIndex){

	return abs(prevColorIndex - currColorIndex) > 1;
}

int computeNext(int prevColorIndex, struct color totColors[]){

	int ans = -1;
	int maxAm = -1;

	forn(i, 6){

		if(areGoodNeighbors(i, prevColorIndex)){

			if(maxAm < totColors[i].amount){

				maxAm = totColors[i].amount;
				ans = i;
			}
		}
	}

	return ans;
}

string getArrangement(int n, int startingIndex){

	string ans = "";
	struct color c;
	int prevColorIndex = -1000;

	struct color totColors[6];

	forn(i, 6){

		c.amount = arr[colors[i]];
		c.c = colors[i];
		c.index = i;
		totColors[i] = c;
	}	

	int nextColorIndex = startingIndex;

	forn(i, n){

		if(i > 0)
			nextColorIndex = computeNext(prevColorIndex, totColors);
		
		ans += totColors[nextColorIndex].c;
		totColors[nextColorIndex].amount--;
		prevColorIndex = nextColorIndex;
	}

	return ans;
}

void readColors(){

	forn(j, 6){
			
		S(arr[colors[j]]);

		if(colors[j] == 'O'){

			auxArr['R'] += arr[colors[j]];
			auxArr['Y'] += arr[colors[j]];
		}

		else if(colors[j] == 'G'){

			auxArr['B'] += arr[colors[j]];
			auxArr['Y'] += arr[colors[j]];
		}

		else if(colors[j] == 'V'){

			auxArr['R'] += arr[colors[j]];
			auxArr['B'] += arr[colors[j]];
		}

		else
			auxArr[colors[j]] = arr[colors[j]];
	}
}

bool isGoodAns(string s){

	forn(i, s.size() - 1)
		if(s[i] == s[i + 1])
			return false;

	return true;
}

int main(){

	int tc, n;
	S(tc);

	forn(i, tc){

		S(n);

		resetArrs();
		readColors();

		printf("Case #%d: ", i + 1);

		if(isPossible(n)){

			string ans = "AA";
			
			forn(j, 6){

				if(!arr[colors[j]])
					continue;

				ans = getArrangement(n, j);

				if(ans[0] != ans[ans.size() - 1])
					break;
			}
		
			if(ans[0] != ans[ans.size() - 1])
				cout<<ans<<endl;

			else
				printf("IMPOSSIBLE\n");
		}

		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}