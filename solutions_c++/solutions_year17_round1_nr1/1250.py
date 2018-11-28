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

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

using namespace std;

int main(){
	int T;
	cin >> T;

	for(int case_num = 0; case_num < T; case_num++){
		int R;
		int C;

		cin >> R;
		cin >> C;

		vector< vector<char> > grid(R, vector<char>(C, '?'));

		for(int row = 0; row < R; row++){
			for(int column = 0; column < C; column++){
				char inp;
				cin >> inp;

				if(inp != '?')
					grid[row][column] = inp;
			}
		}

		vector<int> full_rows(R, -1);
		for(int row = 0; row < R; row++){
			char last_char = '?';

			for(int col = 0; col < C; col++){
				if(grid[row][col] != last_char && grid[row][col] != '?'){
					char new_char = grid[row][col];

					if(last_char == '?'){
						for(int a = 0; a < col; a++){
							grid[row][a] = new_char;
						}
					}

					last_char = new_char;
				}
				grid[row][col] = last_char;
			}

			if(last_char != '?')
				full_rows[row] = row;
		}

		int last_row = -1;
		for(int x = 0; x < R; x++){
			if(full_rows[x] != last_row && full_rows[x] != -1){
				int new_row = full_rows[x];
				if(last_row == -1){
					for(int b = 0; b < x; b++){
						full_rows[b] = new_row;
					}
				}
				last_row = new_row;
			}

			full_rows[x] = last_row;
		}

		cout << "Case #" << case_num+1 << ":" << endl;
		tr(full_rows, it){
			tr(grid[*it], iit){
				cout << *iit;
			}
			cout << endl;
		}
	}
    return 0;	
}

