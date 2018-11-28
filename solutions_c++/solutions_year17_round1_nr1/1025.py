// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 105;
const int INF = 0x3f3f3f3f;
const bool debug = true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector < int >VI;
typedef vector < string > VS;
typedef vector < VI > VVI;
typedef pair < int, int >PII;
typedef pair < int, PII > PIII;

int main()
{
    int tc;
    cin >> tc;

    for (int t = 1; t <= tc; ++t) {

	int r, c;
	cin >> r >> c;
	string grid[r];

	for (int i = 0; i < r; ++i) {
	    cin >> grid[i];
	}


	for (int i = 0; i < r; ++i) {
	    for (int j = 0; j < c; ++j) {
		if (grid[i][j] == '?')
		    continue;

		for (int x = i - 1; x >= 0; --x) {
		    if (grid[x][j] != '?')
			break;
		    grid[x][j] = grid[i][j];
		}

		for (int x = i + 1; x < r; ++x) {
		    if (grid[x][j] != '?')
			break;
		    grid[x][j] = grid[i][j];
		}
	    }
	}

        if(grid[0][0] == '?') {
            int cj = INF;
            for(int j=1;j<c;++j) {
                if(grid[0][j] != '?') {
                    cj= j;
                    break;
                }
            }

            for(int j=0;j<cj;++j) {
                for(int i=0;i<r;++i) {
                    grid[i][j] = grid[i][cj];
                }
            }
        }

        for(int j=1;j<c;++j) {
            if(grid[0][j] != '?') continue;
                for(int i=0;i<r;++i) {
                    grid[i][j] = grid[i][j-1];
                }
        }

	cout << "Case #" << t << ":\n";
	for (int i = 0; i < r; ++i) {
	    cout << grid[i] << "\n";
	}
    }
    return 0;
}
