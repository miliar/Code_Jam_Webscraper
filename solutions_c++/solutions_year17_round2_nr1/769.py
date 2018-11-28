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

long long D,N;
VI pos;
VI speed;

int main()
	{
	int T;
	//ifstream fcin("in.txt",ios::in);
	//ifstream fcin("A-small-attempt0.in",ios::in);	
	ifstream fcin("A-large.in",ios::in);	
	FILE* fout;
	fout = fopen("out.txt","w");
	fcin >> T;
	FOR(tc,0,T)
		{
		double res = 0;
		fcin >> D >> N;
		pos.clear();
		speed.clear();
		pos.resize(N); speed.resize(N);
		FOR(i,0,N) fcin >> pos[i] >> speed[i]; 
		
		double time = 0;
		
		FOR(i,0,N) time = max(time,((double)(D-pos[i]))/speed[i]);
		res = D / time;
		
		fprintf(fout,"Case #%d: %lf\n",tc+1,res);
		}
	fcin.close();
	return 0;
	}
