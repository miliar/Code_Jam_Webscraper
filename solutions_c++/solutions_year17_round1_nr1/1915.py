// ProblemA_AlphabetCake.cpp

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

#define LIMIT 30

char grid[LIMIT][LIMIT];
set<char> myS;

void readGrid(int r, int c){

	forn(i, r){

		string line;
		cin>>line;

		forn(j, c)
			grid[i][j] = line[j];
	}
}

void extend(int r, int c, char d, int y, int x, int dir){

	while(y < r && y >= 0 && grid[y][x] == '?'){

		grid[y][x] = d;
		y += dir;
	}
}

bool isFinished(int r, int c){

	forn(i, r)
		forn(j, c)
			if(grid[i][j] == '?')
				return false;

	return true;
}

void solveHor(int r, int c){

	forn(i, r){

		forn(j, c){

			if(grid[i][j] == '?'){

				if(j > 0){

					extend(r, c, grid[i][j - 1], i + 1, j, 1);
					extend(r, c, grid[i][j - 1], i - 1, j, -1);
				}
			}
		}
	}
}

void fixRows(int r, int c){

	forn(i, r){

		forn(j, c){

			if(grid[i][j] == '?'){

				if(j == 0 && grid[i][j + 1] != '?')
					grid[i][j] = grid[i][j + 1];

				else{

					int auxJ = j;

					while(auxJ < c && grid[i][auxJ] == '?')
						auxJ++;

					if(auxJ < c)
						grid[i][j] = grid[i][auxJ];
				}

				if(grid[i][j] == '?'){

					int auxJ = j;

					while(auxJ >= 0 && grid[i][auxJ] == '?')
						auxJ--;

					if(auxJ >= 0)
						grid[i][j] = grid[i][auxJ];
				}
			}
		}
	}
}

void solve(int r, int c){

	forn(i, r){

		forn(j, c){

			if(myS.find(grid[i][j]) != myS.end())
				continue;

			extend(r, c, grid[i][j], i + 1, j, 1);
			extend(r, c, grid[i][j], i - 1, j, -1);
			myS.insert(grid[i][j]);
		}
	}

	if(!isFinished(r, c))
		fixRows(r, c);
}

void displayGrid(int r, int c){

	forn(i, r){

		forn(j, c)
			printf("%c", grid[i][j]);
		
		printf("\n");
	}
}

int main(){

	int cases, r, c;
	S(cases);

	forn(i, cases){

		myS.clear();
		S2(r, c);
		readGrid(r, c);
		printf("Case #%d:\n", i + 1);
		//displayGrid(r, c);
		solve(r, c);
		displayGrid(r, c);

		// printf("\n");
	}

	return 0;
}
