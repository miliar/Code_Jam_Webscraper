// Author: Xujie Si
// Email: six@gatech.edu
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
using namespace std;

#define FOR(i,X) for(int i=0;i<(X);++i)
#define PB(X) push_back( (X) )

typedef long long LL;
typedef vector<int> VI;

priority_queue<int> maxQ; // largest on the top
priority_queue<int, VI, greater<int> > minQ; // smallest on the top

auto cmp1 = [](int& a, int& b) -> bool {return a>b;};
auto dbg = ostream_iterator<int>(cerr, ",");


const int N = 100;
char buf[N][N];

int R, C;

void out(){
	for(int r = 0; r < R; ++r) puts(buf[r]);
}

void solve(){
	// exact implementation appears here
	set<int> index;
	
	scanf("%d%d",&R,&C);
	for(int i=0;i<R;++i){
		scanf("%s",buf[i]);
	}


	int preC = 0;
	for(int col = 0; col < C; ++col) {
		int preR = 0;

		bool updated = false;
		for(int row = 0; row < R; ++row) {
			if(buf[row][col] == '?') continue;

			char target = buf[row][col];
			//printf("prop  %c, col=%d row=%d\n", buf[row][col], col, row);

			bool s = false;
			for(int i=preR; i <= row; ++i){
				for(int j= preC; j <= col; ++j) {
					buf[i][j] = target;
					s = true;
				}
			}
			if(s){
				preR = row + 1;
				updated = true;
			}
		}

		if(updated) {
			if(preR != R) {
				char target = buf[preR-1][preC];
				//printf("post prop preC=%d preR=%d:  %c\n", preC, preR, target );

				for(int i=preR; i < R; ++i){
					for(int j= preC; j <= col; ++j) {
						buf[i][j] = target;
					}
				}
			}
			preC = col + 1;
		}
	}

	if(preC != C) {
		for(int i=0; i< R; ++i) {
			for(int j=0; j < C; ++j) {
				if(buf[i][j] == '?') {
					if(j == 0) {
						std::cerr << "preC is zero" << endl;
					}
					buf[i][j] = buf[i][j-1];
				}
			}
		}
	}

	for(int i=0; i< R; ++i) {
		for(int j=0; j < C; ++j) {
			if(buf[i][j] == '?') {
				std::cerr << "something was wrong!!" << endl;
			}
		}
	}

	out();
}

int main()
{
  int cs = 0, T;
  scanf("%d",&T);
  while(++cs <= T){
	  if(cs == 99999) {
	  	puts("");
	  	puts("");

		scanf("%d%d",&R,&C);
		for(int i=0;i<R;++i){
			scanf("%s",buf[i]);
			puts(buf[i]);
		}

		break;
	  }
    printf("Case #%d:\n", cs);
    solve();
  }
  return 0;
}
