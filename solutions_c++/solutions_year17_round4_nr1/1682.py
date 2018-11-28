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
#define mp make_pair
#define LL long long
#define PII pair<int,int>
#define SZ(x) (int)((x).size())

using namespace std;

int main()
	{
	int T,N,P;
	ifstream fcin("A-small-attempt0.in",ios::in);
	//ifstream fcin("A-large.in",ios::in);
	//ifstream fcin("in.txt",ios::in);
	FILE* fout;
	fout = fopen("out.txt","w");
	fcin >> T;
	FOR(tc,0,T)
		{
		int res = 0;
		fcin >> N >> P;
		VI x(N);
		FOR(i,0,N) fcin >> x[i];
		
		VI y(5);
		FOR(i,0,N)
			y[(x[i]%P)]++;
		
		if( P == 2 ) {
			res = y[0] + (y[1]+1)/2;	
		}
		else if( P == 3 ) {
			int z = min(y[1],y[2]);
			res = y[0] + z;
			y[1] -= z; y[2] -= z;
			res += (y[1] + y[2] + 2 ) /3;
		}
		else {
			res = y[0];
			res += y[1]/2;
			y[1] %= 2;
			int z = min(y[1],y[3]);
			res += z; 
			y[1] -= z;
			y[3] -= z;
			if ( y[1] == 0 ) {
				res += (y[1]+y[3]+3)/4;
			}
			else {
				res+= (y[1]+y[3]+2+3)/4;
			}
		}
		
		fprintf(fout,"Case #%d: %d\n",tc+1,res);
		}
	fcin.close();
	return 0;
	}
