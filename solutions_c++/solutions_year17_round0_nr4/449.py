#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;


int N,M;
int grid[111][111];
int res[111][111];



bool full_cross(int x,int y){
	int dirx[] = {1,1, -1,-1};
	int diry[] = {1,-1, 1,-1};
	for (int j=0;j<4;j++){
		for (int i=1;i<=N;i++){
			int x2 = x + i * dirx[j];
			int y2 = y + i * diry[j];
			if (x2 >= N || y2 >= N || x2 < 0 || y2 < 0) break;
			if (grid[x2][y2] == 0) 
				continue;
			if (grid[x2][y2] != 'x')
				return false;
		}
	}
	return true;
}

bool full_plus(int x,int y){
	int dirx[] = {1,-1, 0,0};
	int diry[] = {0,0, 1,-1};
	for (int j=0;j<4;j++){
		for (int i=1;i<=N;i++){
			int x2 = x + i * dirx[j];
			int y2 = y + i * diry[j];
			if (x2 >= N || y2 >= N || x2 < 0 || y2 < 0) break;
			if (grid[x2][y2] == 0) 
				continue;
			if (grid[x2][y2] != '+')
				return false;
		}
	}
	return true;
}

void solve(){
	memset(grid, 0, sizeof (grid));
	memset(res, 0, sizeof (res));

	scanf("%d",&N);
	scanf("%d",&M);

	int score = 0;
	for (int i=0;i<M;i++){
		char c;
		int a,b;
		cin>>c>>a>>b;
		grid[--a][--b] = (int) c;
		if (c == 'o') score+=2;
		else score++;
	}
	int kagi = 0;
	vector<int> order;
	order.push_back(0);
	order.push_back(N-1);

	for (int i=1;i<N-1;i++)
		order.push_back(i);

	for (int ii=0;ii<N;ii++){
		int i = order[ii];
		for (int j=0;j<N;j++){
			if (grid[i][j] > 0) continue;
			// + x o
			if ((i == 0 || i == N -1 ) && full_cross(i,j) ){
				grid[i][j] = '+';
				res[i][j] = '+';	
				kagi++;
				score++;
			} 
			else if (full_plus(i,j)){
				grid[i][j] = 'x';
				res[i][j] = 'x';
				kagi++;
				score++;
			}
			else if (full_cross(i,j) ){
				grid[i][j] = '+';
				res[i][j] = '+';	
				kagi++;
				score++;
			} 
		}
	}



	for (int i=0;i<N;i++){
		for (int j=0;j<N;j++){
			if (grid[i][j] == 0 || grid[i][j] == 'o') continue;
			// + x o
			if (full_cross(i,j) && full_plus(i,j) ){
				if (res[i][j] == 0)
					kagi++;
				grid[i][j] = 'o';
				res[i][j] = 'o';
				score++;

			} 
		}
	}

	printf("%d %d\n",score, kagi);
	for (int i=0;i<N;i++){
		for (int j=0;j<N;j++){
			if (res[i][j] == 0) continue;
			printf("%c %d %d\n", res[i][j],i+1,j+1);
		}
	}

}

int main(){
	int T;
	scanf("%d",&T);
	for (int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}
}