#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
#include<iomanip>
#include<queue>
#include<map>
#include<deque>

using namespace std;

#define VI vector<int>
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define LL long long
#define PB push_back
#define VB vector<bool>
#define VS vector<string>
#define VVS vector<VS>
#define MAXN 1<<7

LL N,K;
bool P[MAXN][MAXN],M[MAXN][MAXN];
bool H[MAXN],V[MAXN],D[2*MAXN],A[2*MAXN];
bool E[MAXN][MAXN];

bool isGoodPlus(int r,int c){
	for(int i=1;i<=N;i++){
		for(int j=1;j<=N;j++){
			if(P[i][j] and (i+j == r+c or i-j == r-c))
				return false;
		}
	}
	return true;
}

bool isGoodCross(int r,int c){
	for(int i=1;i<=N;i++){
		if(M[i][c] or M[r][i])
			return false;
	}
	return true;
}

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/quals/D_input1.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/quals/D_output1.txt", "w", stdout);

	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		cin>>N>>K;

		int score = 0;
		for(int i=1;i<=N;i++) for(int j=1;j<=N;j++) P[i][j] = M[i][j] = E[i][j] = 0;

		for(int i=1;i<=K;i++){
			char x;
			int r,c;
			cin>>x>>r>>c;
			if(x == '+' or x == 'o'){
				P[r][c] = 1;
				score++;
			}

			if(x == 'x' or x == 'o'){
				M[r][c] = 1;
				score++;
			}
		}

		// top row
		for(int i=1;i<=N;i++){
			if(isGoodPlus(1,i)){
				P[1][i] = 1;
				E[1][i] = 1;
				score++;
			}
		}

		// bottom row
		for(int i=1;i<=N;i++){
			if(isGoodPlus(N,i)){
				P[N][i] = 1;
				E[N][i] = 1;
				score++;
			}
		}

		// left column
		for(int i=1;i<=N;i++){
			if(isGoodPlus(i,1)){
				P[i][1] = 1;
				E[i][1] = 1;
				score++;
			}
		}

		// right column
		for(int i=1;i<=N;i++){
			if(isGoodPlus(i,N)){
				P[i][N] = 1;
				E[i][N] = 1;
				score++;
			}
		}

		// crosses
		for(int i=1;i<=N;i++){
			for(int j=1;j<=N;j++){
				if(isGoodCross(i,j)){
					M[i][j] = 1;
					E[i][j] = 1;
					score++;
				}
			}
		}

		int edits = 0;
		for(int i=1;i<=N;i++){
			for(int j=1;j<=N;j++){
				if(E[i][j])
					edits++;
			}
		}
		cout<<"Case #"<<casenum<<": "<<score<<" "<<edits<<endl;

		for(int i=1;i<=N;i++){
			for(int j=1;j<=N;j++){
				if(E[i][j]){
					if(P[i][j] == 0)
						cout<<"x "<<i<<" "<<j<<endl;
					else if(M[i][j] == 0)
						cout<<"+ "<<i<<" "<<j<<endl;
					else
						cout<<"o "<<i<<" "<<j<<endl;
				}
			}
		}
	}

	return 0;
}
