#include<stdio.h>
#include<stdlib.h>

#define Swap(aa,bb) {cc=aa;aa=bb;bb=cc;}
int cc;

int T;
int A[101][1440];
int Order[101];
int N, M;
int Ret, Curr;
int B[1440];

int D[1440][721][2][2];
int C[1440][721][2][2];
int Flag;
int INF = 1000000000;

int Go(int last, int sum0, int c_first, int c_last)
{
	int head, opt;

	if(last+1 < sum0) return INF;
	if(sum0 < 0) return INF;
	if(B[last] != 0 && B[last] != c_last+1) return INF;
	if(last == 0)
	{
		if(c_last != c_first) return INF;
		if(sum0 == 0) // 1
		{
			if(B[0] == 1) return INF;
			if(c_first == 0) return INF;
			return 0;
		}
		else if(sum0 == 1) // 0
		{
			if(B[0] == 2) return INF;
			if(c_first == 1) return INF;
			return 0;
		}
		else return INF;
	}

	if(C[last][sum0][c_first][c_last] != Flag)
	{
		C[last][sum0][c_first][c_last] = Flag;
		opt = INF;
		if(c_last == 0)
		{
			head = Go(last-1, sum0-1, c_first, 0);
			if(head < opt) opt = head;
			head = Go(last-1, sum0-1, c_first, 1) + 1;
			if(head < opt) opt = head;
		}
		else
		{
			head = Go(last-1, sum0, c_first, 0) + 1;
			if(head < opt) opt = head;
			head = Go(last-1, sum0, c_first, 1);
			if(head < opt) opt = head;
		}
		D[last][sum0][c_first][c_last] = opt;
	}
	
	return D[last][sum0][c_first][c_last];
}

int main(void)
{
	int l0, l1, l2;
	int start, end;

	{
		int seed;
		FILE *urandom = fopen("/dev/urandom", "r");
		fread(&seed, sizeof(int), 1, urandom) == 0;
		fclose(urandom);
		if(seed < 0) seed = -seed;
		srand(seed);
	}

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		for(l1 = 0; l1 < 1440; l1++) A[l0][l1] = 0;

		scanf("%d %d", &N, &M);
		for(l1 = 0; l1 < N; l1++)
		{
			scanf("%d %d", &start, &end);
			for(l2 = start; l2 < end; l2++) A[l0][l2] = 1;
		}
		for(l1 = 0; l1 < M; l1++)
		{
			scanf("%d %d", &start, &end);
			for(l2 = start; l2 < end; l2++) A[l0][l2] = 2;
		}
	}

	for(l0 = 1; l0 <= T; l0++) Order[l0] = l0;
	/*
	for(l1 = 2; l1 <= T; l1++)
	{
		l2 = rand() % l1 + 1;
		Swap(Order[l1], Order[l2]);
	}
	*/

	Flag = 0;
	for(l0 = 1; l0 <= T; l0++)
	{
		fprintf(stderr, "%d/%d\n", l0, T);
		Flag++;
		for(l1 = 0; l1 < 1440; l1++) B[l1] = A[Order[l0]][l1];

		Ret = INF;
		Curr = Go(1440-1, 720, 0, 0);
		if(Curr < Ret) Ret = Curr;
		Curr = Go(1440-1, 720, 0, 1) + 1;
		if(Curr < Ret) Ret = Curr;
		Curr = Go(1440-1, 720, 1, 0) + 1;
		if(Curr < Ret) Ret = Curr;
		Curr = Go(1440-1, 720, 1, 1);
		if(Curr < Ret) Ret = Curr;

		printf("Case #%d: %d\n", Order[l0], Ret);
	}

	return 0;
}
