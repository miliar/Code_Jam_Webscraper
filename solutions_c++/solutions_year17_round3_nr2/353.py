// VSCF.cpp : Defines the entry point for the console application.
//
#include <bits/stdc++.h>
#include "gurobi_c++.h"
using namespace std;
#define int long long
#define M_PI 3.14159265358979323846
typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i)  decltype(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SZ(x) (int)x.size()
#define SIZE(x) SZ(x)
#define ALL(c) c.begin(),c.end()
#define MAXN 1000010
typedef long double LD;
typedef vector<int> VI;

int32_t main() {
	ios_base::sync_with_stdio(0);
	cout << setprecision(9) << fixed;
	int t;
	cin >> t;
	REP(_, t) {
		cerr << "test + " << to_string(_)<<"\n";
		int maxRes = LLONG_MAX;
		int tday = 60 * 24;
		struct interval {
			int l, r, owner;
			bool operator<(const interval & rhs) const {
				return tie(l, r, owner) < tie(rhs.l, rhs.r, rhs.owner);
			}
		};
		int ac, aj;
		cin >> ac >> aj;
		if (!ac && !aj) {
			maxRes = 0;
			cout << "Case #" << _ + 1 << ": " << maxRes << "\n";
			continue;
		}
		vector<interval> inp(ac + aj);
		REP(i, ac) {
			cin >> inp[i].l >> inp[i].r;
			inp[i].owner = 0;
		}
		FOR(i, ac, ac + aj - 1) {
			cin >> inp[i].l >> inp[i].r;
			inp[i].owner = 1;
		}
		sort(ALL(inp));

		GRBEnv env;
		env.set(GRB_DoubleParam_MIPGap, 0);
		GRBModel model(env);
		model.set(GRB_IntAttr_ModelSense, GRB_MINIMIZE);
		model.set(GRB_IntParam_OutputFlag, 0);
		GRBVar ctime = model.addVar(720, 720, 0, GRB_INTEGER, "ctime");
		GRBVar jtime = model.addVar(720, 720, 0, GRB_INTEGER, "jtime");
		GRBVar exchanges = model.addVar(0, 1, 0, GRB_INTEGER, "exchanges");;
		vector<GRBVar> times(tday);
		vector<GRBVar> koks(tday);
		REP(i, tday) {
			times[i] = model.addVar(0, 1, 0, GRB_BINARY, "times_" + to_string(i));
			koks[i] = model.addVar(0, 1, 1, GRB_BINARY, "koks_" + to_string(i));
		}
		model.update();
		GRBLinExpr cexpr, jexpr;
		REP(i, tday) {
			cexpr += times[i];
		}
		model.addConstr(ctime == cexpr);
		model.addConstr(jtime == tday - ctime);
		for (interval i : inp) {
			FOR(j, i.l, i.r - 1) {
				model.addConstr(times[j] == i.owner);
			}
		}
		REP(i, tday) {
			GRBVar t1 = times[i];
			GRBVar t2 = times[(i + 1) % tday];
			model.addConstr(koks[i] <= t1 + t2);
			model.addConstr(koks[i] >= t1 - t2);
			model.addConstr(koks[i] >= t2 - t1);
			model.addConstr(koks[i] <= 2 - t2 - t1);
		}
		model.optimize();
		maxRes = (int)model.get(GRB_DoubleAttr_ObjVal);
		/*vector<GRBVar> vars1(ac + aj);
		vector<GRBVar> vars2(ac + aj);
		vector<GRBVar> varsb(ac + aj);
		REP(i, ac + aj){
			int l1 = inp[i].l,
				r1 = inp[i].r,
				l2 = inp[i + 1].l,
				r2 = inp[i + 1].r,
				own1 = inp[i].owner,
				own2 = inp[i + 1].owner;
			vars1[i] = model.addVar(0, GRB_INFINITY, 0, GRB_INTEGER, "vars1_" + to_string(i));
			vars2[i] = model.addVar(0, GRB_INFINITY, 0, GRB_INTEGER, "vars2_" + to_string(i));
			vars2[i] = model.addVar(0, 1, 0, GRB_BINARY, "varsb_" + to_string(i));
		}
		model.update();
		GRBLinExpr exchangeExpr;
		GRBLinExpr cexpr;
		GRBLinExpr jexpr;
		REP(i, ac + aj - 1) {
			int l1 = inp[i].l,
				r1 = inp[i].r,
				l2 = inp[i + 1].l,
				r2 = inp[i + 1].r,
				own1 = inp[i].owner,
				own2 = inp[i + 1].owner;
			jexpr += own1 * (r1 - l1) + own2 * (r2 - l2);
			cexpr += (1 - own1) * (r1 - l1) + (1 - own2) * (r2 - l2);
			if (own1 == own2) {

			}
		}
		model.update();
		model.optimize();*/
		end:
		cout << "Case #" << _ + 1 << ": " << maxRes << "\n";
	}
	return 0;
}
