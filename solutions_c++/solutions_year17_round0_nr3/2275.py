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

map<long long,long long> dp;
long long N,K;
long long x;

long long go(long long len){
	//cout << len << endl;
	//system("pause");
	map<long long,long long>::iterator it = dp.find(len);
	if(it != dp.end()) return it->second;
	long long sol = 0;
	if( len >= x ) sol = 1 + go((len-1)/2) + go(len/2);
	dp[len] = sol; 
	return sol;
}

int solve(long long len){
	x = len;
	long long cnt = go(N);
	//cout << N << " " << len << " " << cnt << endl;
	return (cnt >= K);
}

int main()
	{
	int T;
	//ifstream fcin("in.txt",ios::in);
	ifstream fcin("C-large.in",ios::in);
	FILE* fout;
	fout = fopen("out.txt","w");
	fcin >> T;
	FOR(tc,0,T)
		{
		int res = 0;
		
		fcin >> N >> K;
		cout << N << " " << K << endl;
		
		long long minlen = 1;
		long long maxlen = N;
		
		while(minlen < maxlen) {
			dp.clear();
			long long midlen = (maxlen+minlen+1)/2;
			//cout << minlen << " " << maxlen << endl;
			//cout << "try " << midlen << endl;
			if( solve(midlen) )
				minlen = midlen;
			else maxlen = midlen -1;
			//cout << minlen << " " << maxlen << endl;
		}
		long long larger = maxlen/2;
		long long smaller = (maxlen-1)/2;
		
		fprintf(fout,"Case #%d: %lld %lld\n",tc+1,larger,smaller);
		}
	fcin.close();
	return 0;
	}
