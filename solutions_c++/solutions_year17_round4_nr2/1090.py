#include<stdio.h>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

#define MAXV 2222
int F[MAXV][MAXV];

struct MF
{
	vector< vector<int> > AL;
	int V, S, T, TF;

	MF(int VV, int SS, int TT) : V(VV), S(SS), T(TT)
	{
		int l1, l2;
		TF = 0; AL.clear(); AL.resize(V);
		for(l1=0;l1<V;l1++) for(l2=0;l2<V;l2++) F[l1][l2] = 0;
	}
	void Add(int t1, int t2, int w)
	{
		if(F[t1][t2] == 0){ AL[t1].push_back(t2); AL[t2].push_back(t1); }
		F[t1][t2] += w;
	}
	int FF()
	{
		int l1, l2, t1, t2;
		vector<int> Check(V);
		vector<int> Back(V, -1);
		queue<int> q;
		q.push(S);
		Check[S] = 0x7fffffff;

		while(!q.empty())
		{
			l1 = q.front();
			if(l1 == T) break;
			q.pop();
			for(l2=0;l2<AL[l1].size();l2++)
				if(F[l1][AL[l1][l2]] && Check[AL[l1][l2]] == 0)
				{
					Check[AL[l1][l2]] = min(F[l1][AL[l1][l2]], Check[l1]);
					Back[AL[l1][l2]] = l1;
					q.push(AL[l1][l2]);
				}
		}
		if(l1 != T) return 0;
		TF += Check[T];
		for(l1=T;l1!=S;l1=Back[l1])
		{
			F[Back[l1]][l1] -= Check[T];
			F[l1][Back[l1]] += Check[T];
		}
		return Check[T];
	}
};

int T;
int N, C, M;
int Index, Buyer;
int Cnt1[1001];
int Cnt2[1001];
int Ret1, Ret2;

int main(void)
{
	int l0, l1, l2;
	int upleft, downleft;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d %d %d", &N, &C, &M);
		for(l1 = 0; l1 <= N; l1++)
		{
			Cnt1[l1] = Cnt2[l1] = 0;
		}
		for(l1 = 0; l1 < M; l1++)
		{
			scanf("%d %d", &Index, &Buyer);
			if(Buyer == 1) Cnt1[Index]++;
			if(Buyer == 2) Cnt2[Index]++;
		}

		MF mf = MF(N+N+2, 0, N+N+1);
		for(l1 = 0; l1 <= N+N+1; l1++)
		{
			mf.Add(l1, 1, 0);
			mf.Add(l1, N+1, 0);
		}

		for(l1 = 1; l1 <= N; l1++)
		{
			if(Cnt1[l1] > 0)
			{
				mf.Add(0, l1, Cnt1[l1]);
//				printf("%d %d %d\n", 0, l1, Cnt1[l1]);
			}
			if(Cnt2[l1] > 0)
			{
				mf.Add(N+l1, N+N+1, Cnt2[l1]);
//				printf("%d %d %d\n", N+l1, N+N+1, Cnt2[l1]);
			}
		}

		for(l1 = 1; l1 <= N; l1++)
		{
			for(l2 = 1; l2 <= N; l2++)
			{
				if(l1 == l2) continue;
				mf.Add(l1, N+l2, M);
			}
		}


//		fprintf(stderr, "Go %d\n", l0);
		while(mf.FF());
		Ret1 = mf.TF;
		Ret2 = 0;
		upleft = downleft = 0;
		for(l1 = 1; l1 <= N; l1++)
		{
			upleft += F[0][l1];
			downleft += F[N+l1][N+N+1];
		}
		if(upleft > 0 && downleft == 0)
		{
			Ret1 += upleft;
		}
		else if(upleft == 0 && downleft > 0)
		{
			Ret1 += downleft;
		}
		else if(upleft > 0 && downleft > 0)
		{
			if(F[0][1] == 0)
			{
				Ret1 += max(upleft, downleft);
				Ret2 += min(upleft, downleft);
			}
			else
			{
				Ret1 += upleft+downleft;
			}
		}
		
		printf("Case #%d: %d %d\n", l0, Ret1, Ret2);
	}

	return 0;
}
