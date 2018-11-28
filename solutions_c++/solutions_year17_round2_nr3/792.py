#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <map>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <set>

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define FORC(it,cont) for(__typeof(cont.begin()) it=(cont).begin(); it!=(cont).end();++(it))
#define VI vector<int>
#define VS vector<string>
#define pb push_back

using namespace std;

int Q,N;
vector<long long> endurance;
VI speed;
vector<vector<long long> > dist;
VI startp;
VI endp;

double dp[110];

double solve(int pos){
	if( dp[pos] != -1 )
		return dp[pos];
	double& sol = dp[pos];
	sol = 1e18; 
	if( pos == N-1) { sol = 0; return sol; }
	long long tmpdist = 0;
	FOR(i,pos+1,N) {
		tmpdist += dist[i-1][i];
		if( tmpdist <= endurance[pos] )
			sol = min(sol, ((double)tmpdist)/speed[pos] + solve(i) );
	}
	//cout << pos << " " << sol << endl;
	return sol;
}

int main()
	{
	int T;
	//ifstream fcin("in.txt",ios::in);
	ifstream fcin("C-small-attempt0.in",ios::in);
	FILE* fout;
	fout = fopen("out.txt","w");
	fcin >> T;
	FOR(tc,0,T)
		{
		double res = 0;
		
		fcin >> N >> Q;
		endurance.resize(N);
		speed.resize(N);
		FOR(i,0,N)
			fcin >> endurance[i] >> speed[i];
		dist.resize(N);
		FOR(i,0,N) dist[i].resize(N);
		FOR(i,0,N) FOR(j,0,N) fcin >> dist[i][j];
		
		startp.resize(Q);
		endp.resize(Q);
		FOR(i,0,Q) fcin >> startp[i] >> endp[i];
		FOR(i,0,110) dp[i] = -1;
		res = solve(0);
		
		fprintf(fout,"Case #%d: %.9lf\n",tc+1,res);
		}
	fcin.close();
	return 0;
	}
