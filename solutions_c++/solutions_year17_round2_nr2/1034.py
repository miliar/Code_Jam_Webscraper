// 3rd party library - CPLEX is used for solving the integer programming

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <ilcplex\ilocplex.h>

using namespace std;

int N, R, RY, Y, YB, B, RB;

void Work()
{
	scanf("%d%d%d%d%d%d%d", &N, &R, &RY, &Y, &YB, &B, &RB);
	
	// Solve by CPLEX
	IloEnv env;
	try
	{
		IloModel model(env);
		IloIntVarArray r(env, N, 0, 1);
		IloIntVarArray ry(env, N, 0, 1);
		IloIntVarArray y(env, N, 0, 1);
		IloIntVarArray yb(env, N, 0, 1);
		IloIntVarArray b(env, N, 0, 1);
		IloIntVarArray rb(env, N, 0, 1);
		model.add(IloMaximize(env, r[0]));
		for (int i = 0; i < N; i ++)
			model.add(r[i] + ry[i] + y[i] + yb[i] + b[i] + rb[i] == 1);
		IloIntExpr sr(env, 0), sry(env, 0), sy(env, 0), syb(env, 0), sb(env, 0), srb(env, 0);
		for (int i = 0; i < N; i ++)
		{
			sr = sr + r[i];
			sry = sry + ry[i];
			sy = sy + y[i];
			syb = syb + yb[i];
			sb = sb + b[i];
			srb = srb + rb[i];
		}
		model.add(sr == R);
		model.add(sry == RY);
		model.add(sy == Y);
		model.add(syb == YB);
		model.add(sb == B);
		model.add(srb == RB);
		for (int i = 0; i < N; i ++)
		{
			int j = (i + 1) % N;
			model.add(r[i] + r[j] <= 1);
			model.add(r[i] + ry[j] <= 1);
			model.add(r[i] + rb[j] <= 1);
			model.add(y[i] + y[j] <= 1);
			model.add(y[i] + ry[j] <= 1);
			model.add(y[i] + yb[j] <= 1);
			model.add(b[i] + b[j] <= 1);
			model.add(b[i] + yb[j] <= 1);
			model.add(b[i] + rb[j] <= 1);

			model.add(ry[i] + r[j] <= 1);
			model.add(ry[i] + ry[j] <= 1);
			model.add(ry[i] + rb[j] <= 1);
			model.add(ry[i] + y[j] <= 1);
			model.add(ry[i] + ry[j] <= 1);
			model.add(ry[i] + yb[j] <= 1);
			
			model.add(rb[i] + r[j] <= 1);
			model.add(rb[i] + ry[j] <= 1);
			model.add(rb[i] + rb[j] <= 1);
			model.add(rb[i] + b[j] <= 1);
			model.add(rb[i] + yb[j] <= 1);
			model.add(rb[i] + rb[j] <= 1);

			model.add(yb[i] + y[j] <= 1);
			model.add(yb[i] + ry[j] <= 1);
			model.add(yb[i] + yb[j] <= 1);
			model.add(yb[i] + b[j] <= 1);
			model.add(yb[i] + yb[j] <= 1);
			model.add(yb[i] + rb[j] <= 1);
		}

		IloCplex cplex(model);
		cplex.setOut(env.getNullStream());
		cplex.setWarning(env.getNullStream());
		if (cplex.solve() == IloFalse)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			for (int i = 0; i < N; i ++)
			{
				if (cplex.getIntValue(r[i])) printf("R");
				if (cplex.getIntValue(ry[i])) printf("O");
				if (cplex.getIntValue(y[i])) printf("Y");
				if (cplex.getIntValue(yb[i])) printf("G");
				if (cplex.getIntValue(b[i])) printf("B");
				if (cplex.getIntValue(rb[i])) printf("V");
			}
			printf("\n");
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
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
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