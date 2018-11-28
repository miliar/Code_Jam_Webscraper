#include <bits/stdc++.h>

using namespace std;
#define MAX 100000
#define T (24*60+2)

int f[T], m[T];
int dres[T][720][2][2];


int recur_solve(int t, int c, int turn, int end)
{
	if (c < 0) return MAX;
	if (turn == 1)
		{
			if (!f[t]) return MAX;
		}
	else
		{
			if (!m[t]) return MAX;
		}
		
	if (t == 0 && c == 0) 
		return turn != end ? 1 : 0;
	int &res = dres[t][c][turn][end];
	
	if (res) return res;
	res = MAX;
	int tmp1 = recur_solve(t - 1, c - 1, turn, end);
	int tmp2 = recur_solve(t - 1, t - c -1, 1 - turn, end) + 1;
	res = min(tmp1, tmp2);
	return res;
}

int main(int argc, char *argv[])
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    //FILE *f = fopen("/home/quanganh/projects/TestQt/build-TestQt-Desktop-Debug/input.txt", "r");

    int num_test;
    //fscanf(f, "%d", &num_test);
    scanf("%d", &num_test);

    for (int test = 0; test < num_test; test++)
    {
    	memset(f, 1, T * sizeof(int));
    	memset(m, 1, T * sizeof(int));
    	memset(dres, 0, sizeof dres);
        int AC, AJ;
        scanf("%d %d", &AC, &AJ);
        
        for (int i = 0; i < AC; i++)
        {
        	int start, end;
        	scanf("%d %d", &start, &end);
        	memset(f + start, 0, (end - start) * sizeof(int));
		}
		
		for (int i = 0; i < AJ; i++)
        {
        	int start, end;
        	scanf("%d %d", &start, &end);
        	memset(m + start, 0, (end - start) * sizeof(int));
		}
		
		int tmp1 = recur_solve(1440, 720, 0, 0);
		int tmp2 = recur_solve(1440, 720, 1, 1);
		int res = min(tmp1, tmp2);

        printf("Case #%d: %d\n", test + 1, res);
    }

    return 0;
}

