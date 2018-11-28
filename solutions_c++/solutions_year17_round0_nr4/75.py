// 3rd party library - CPLEX is used for solving the integer programming

#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <ilcplex\ilocplex.h>

using namespace std;

int N, nOccupied;
char Buf[10];
char Map[105][105];

void Work()
{
	scanf("%d%d", &N, &nOccupied);
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < N; j ++)
			Map[i][j] = '.';
	for (int i = 0; i < nOccupied; i ++)
	{
		int x, y;
		scanf("%s%d%d", Buf, &x, &y);
		Map[x - 1][y - 1] = Buf[0];
	}
	// Solve by CPLEX
	IloEnv env;
	try
	{
		IloModel model(env);
		IloIntVarArray spc(env, N * N, 0, 1);
		IloIntVarArray plus(env, N * N, 0, 1);
		IloIntVarArray x(env, N * N, 0, 1);
		IloIntVarArray o(env, N * N, 0, 1);
		IloIntVar obj(env, nOccupied, N * N + N);
		model.add(IloMaximize(env, obj));
		model.add(obj == IloSum(plus) + IloSum(x) + IloSum(o) * 2);
		for (int i = 0; i < N; i ++)
			for (int j = 0; j < N; j ++)
			{
				int id = i * N + j;
				model.add(spc[id] + plus[id] + x[id] + o[id] == 1);
				if (Map[i][j] == 'o')
				{
					model.add(spc[id] == 0);
					model.add(plus[id] == 0);
					model.add(x[id] == 0);
					model.add(o[id] == 1);
				}
				if (Map[i][j] == 'x')
				{
					model.add(spc[id] == 0);
					model.add(plus[id] == 0);
				}
				if (Map[i][j] == '+')
				{
					model.add(spc[id] == 0);
					model.add(x[id] == 0);
				}
			}
		for (int i = 0; i < N; i ++)
		{
			IloIntExpr tmp(env, 0);
			for (int j = 0; j < N; j ++)
			{
				int id = i * N + j;
				tmp = tmp + x[id] + o[id];
			}
			model.add(tmp <= 1);
		}
		for (int i = 0; i < N; i ++)
		{
			IloIntExpr tmp(env, 0);
			for (int j = 0; j < N; j ++)
			{
				int id = j * N + i;
				tmp = tmp + x[id] + o[id];
			}
			model.add(tmp <= 1);
		}

		for (int tot = 0; tot < N + N - 1; tot ++)
		{
			IloIntExpr tmp(env, 0);
			for (int i = 0; i < N; i ++)
			{
				int j = tot - i;
				if (j >= 0 && j < N)
				{
					int id = i * N + j;
					tmp = tmp + plus[id] + o[id];
				}
			}
			model.add(tmp <= 1);
		}
		for (int tot = 0; tot < N + N - 1; tot ++)
		{
			IloIntExpr tmp(env, 0);
			for (int i = 0; i < N; i ++)
			{
				int j = tot - i;
				if (j >= 0 && j < N)
				{
					int id = i * N + (N - 1 - j);
					tmp = tmp + plus[id] + o[id];
				}
			}
			model.add(tmp <= 1);
		}

		IloCplex cplex(model);
		cplex.setOut(env.getNullStream());
		cplex.setWarning(env.getNullStream());
		cplex.solve();
		int OBJ = cplex.getIntValue(obj);
		//OBJ = cplex.getIntValue(plus[0]);
		int cnt = 0;
		for (int i = 0; i < N; i ++)
		{
			for (int j = 0; j < N; j ++)
			{
				int id = i * N + j;
				char g = cplex.getIntValue(plus[id]) * '+' + cplex.getIntValue(x[id]) * 'x' + cplex.getIntValue(o[id]) * 'o' + cplex.getIntValue(spc[id]) * '.';
				cnt += (g != Map[i][j]);
			}
		}
		printf("%d %d\n", OBJ, cnt);
		for (int i = 0; i < N; i ++)
		{
			for (int j = 0; j < N; j ++)
			{
				int id = i * N + j;
				char g = cplex.getIntValue(plus[id]) * '+' + cplex.getIntValue(x[id]) * 'x' + cplex.getIntValue(o[id]) * 'o' + cplex.getIntValue(spc[id]) * '.';
				if (g != Map[i][j])
				{
					printf("%c %d %d\n", g, i + 1, j + 1);
				}
			}
		}
		env.end();
	}
	catch (IloException& ex)
	{
		cerr << "Error: " << ex << endl;
		env.end();
	}
	catch (...)
	{
		cerr << "Error" << endl;
		env.end();
	}
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: ", Case);
		fprintf(stderr, "Case #%d: \n", Case);
		Work();
		fflush(stdout);
	}
	return 0;
}