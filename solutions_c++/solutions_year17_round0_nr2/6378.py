// nerdyninja
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007

typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<PII> VII;

int checkSol(char x[], int l)
{
	for(int i = l-1; i > 0; i--){
		if(x[i]-'0' >= x[i-1]-'0')continue;
		else return 0;
	}
	return 1;
}

void solve(char x[], int qq)
{
	int l = strlen(x);
	int j, i;
	if(checkSol(x, l))printf("%s\n", x);
	else{
		i = l-1;
		while(1){
			if(x[i]-'0' < x[i-1]-'0'){
				for(j = i; j < l; j++)x[j] = '9';
				if(x[i-1]-'0' == 0){
					for(j = i-1; j > 0; j--){
						if(x[j] == '0')x[j] = '9';
						else break;
					}
					x[j] = (x[j]-'0')+47;
				}
				else x[i-1] = (x[i-1]-'0')+47;
			}
			i--;
			if(checkSol(x, l))break;
		}
		if(x[0] == '0'){
			for(int i = 1; i < l; i++)printf("%c", x[i]);
			printf("\n");
		}
		else printf("%s\n", x);
	}
}

int main()
{

	freopen("B-l.in", "r", stdin);
	freopen("B-l.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int qq = 1; qq <= t; qq++){
		char x[110];
		scanf("%ss", x);
		printf("Case #%d: ", qq);
		solve(x, qq);
	}
	return 0;
}