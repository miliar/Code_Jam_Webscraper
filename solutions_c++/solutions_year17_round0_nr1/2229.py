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

int main()
	{
	int T,N;
	ifstream fcin("A-large.in",ios::in);
	FILE* fout;
	fout = fopen("out.txt","w");
	fcin >> T;
	FOR(tc,0,T)
		{
		int res = 0;
		string s; int K;
		fcin >> s >> K;
		cout << s << " " << K << endl;
		VI a;
		int N = s.size();
		FOR(i,0,N)
			if(s[i]=='+') a.pb(0);
			else a.pb(1);
		VI b(N,0);
		int cnt = 0;
		bool ok = true;
		FOR(i,0,N) {
			if( i >= K ) cnt -= b[i-K];
			if((cnt + a[i]) % 2 == 1) {
				b[i] = 1;
				++cnt;
				++res;
				if(i >N - K) ok = false;
			}
		}
		if( ok == false ) fprintf(fout,"Case #%d: IMPOSSIBLE\n",tc+1);
		else fprintf(fout,"Case #%d: %d\n",tc+1,res);
		}
	fcin.close();
	return 0;
	}
