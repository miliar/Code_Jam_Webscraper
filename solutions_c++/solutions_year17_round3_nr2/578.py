//#include <bits/stdc++.h>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<cmath>
#include<math.h>
#define MAX 1450

using namespace std;

int Min(int a, int b) {
	if (a > b) return b;
	return a;
}

pair<int, int> D[2][MAX];


int Dy[MAX][2][MAX] = { 0, };
int Path[MAX][2][MAX] = { 0, };

void _main(int TEST)
{
	int ans,N,M,i,j,k;
	scanf("%d%d", &N, &M);

	for (i = 0; i <= 1440; i++) {
		for (j = 0; j <= 720; j++) {
			Dy[i][0][j] = Dy[i][1][j] = 1500;
		}
	}

	int V[MAX] = { 0, };
	for (i = 0; i < N; i++) {
		scanf("%d%d", &D[0][i].first, &D[0][i].second);

		for (j = D[0][i].first; j < D[0][i].second; j++) V[j] = 1;
	}

	for (i = 0; i < M; i++) {
		scanf("%d%d", &D[1][i].first, &D[1][i].second);

		for (j = D[1][i].first; j < D[1][i].second; j++) V[j] = -1;
	}




	for (i = 0; i <= 1440; i++) {
		for (j = 0; j <= 720; j++) {
			Dy[i][0][j] = Dy[i][1][j] = 1500;
		}
	}
	Dy[0][0][0] = 0;
	//	Dy[0][1][0] = 0;

	for (i = 1; i <= 1440; i++) {
		//J
		if (V[i] != 1) {
			
			for (j = 0; j < Min(720, i ); j++) {
				if(i-1-j>=0)Dy[i][0][j + 1] = Min(Dy[i - 1][0][j], Dy[i - 1][1][(i-1) - j] + 1);
				else Dy[i][0][j + 1] = Dy[i - 1][0][j];


			}
		}

		//K
		if (V[i] != -1) {
			for (j = 0; j < Min(720, i); j++) {
				if (i - 1 - j >= 0)Dy[i][1][j + 1] = Min(Dy[i - 1][1][j], Dy[i - 1][0][(i - 1) - j] + 1);
				else Dy[i][1][j + 1] = Dy[i - 1][1][j];

			}
		}
	}
	int Ans0, Ans1;
	Ans0 = Min(Dy[1440][0][720] - 1, Dy[1440][1][720]);
	
	for (i = 0; i <= 1440; i++) {
		for (j = 0; j <= 720; j++) {
			Dy[i][0][j] = Dy[i][1][j] = 1500;
		}
	}
	//Dy[0][0][0] = 0;
	Dy[0][1][0] = 0;

	for (i = 1; i <= 1440; i++) {
		//J
		if (V[i] != 1) {

			for (j = 0; j < Min(720, i); j++) {
				if (i - 1 - j >= 0)Dy[i][0][j + 1] = Min(Dy[i - 1][0][j], Dy[i - 1][1][(i - 1) - j] + 1);
				else Dy[i][0][j + 1] = Dy[i - 1][0][j];


			}
		}

		//K
		if (V[i] != -1) {
			for (j = 0; j < Min(720, i); j++) {
				if (i - 1 - j >= 0)Dy[i][1][j + 1] = Min(Dy[i - 1][1][j], Dy[i - 1][0][(i - 1) - j] + 1);
				else Dy[i][1][j + 1] = Dy[i - 1][1][j];

			}
		}
	}
	Ans1 = Min(Dy[1440][0][720] , Dy[1440][1][720]-1);

	printf("%d\n",Min(Ans0, Ans1)+1);
	return;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TEST;

	scanf("%d", &TEST);
	for (int i = 1; i <= TEST; i++)
	{
		//cerr << i << endl;
		printf("Case #%d: ", i);
		_main(i);
	}
	return 0;
}
