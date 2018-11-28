#include <cstdlib>
#include <iostream>
#include <cstring>
#include <fstream>
#include <iomanip>
using namespace std;
int T;
int N,D;
typedef long long ll;
ll dist[105];
ll cum[105];
ll speed[105];
ll energy[105];
ll mat[105][105];
double dp[105][105];
int u,v;

ll query(int sx, int dx){
	ll sum = 0;
	sum+= cum[dx];
	if(sx > 0) 	sum-= cum[sx-1];
	return sum;
}
double solve(int pos, int cav){
	
	if(pos == N-1) return 0;
	if(dp[pos][cav] < 0) return dp[pos][cav];
	ll km_left = energy[cav] - query(cav,pos-1);
	double time = 1e15;
	if(km_left >= dist[pos]) time = min( time, (1.0*dist[pos])/speed[cav] + solve(pos+1,cav));
	if(cav != pos) time = min(time, solve(pos,pos));
	return dp[pos][cav] = time;
}
int main(){
	fstream in;
	fstream out;
	out.open("output.txt",ios::out);
	in.open("input.txt",ios::in);
	in >> T;
	for(int tc = 1; tc <= T; ++tc){
		cout << tc << endl;
		in >> N >> D;
		for(int i = 0; i < N; ++i)
			in >> energy[i] >> speed[i];
		
		for(int i = 0; i < N; ++i)
			for(int j = 0; j < N; ++j)
				in >> mat[i][j];
		
		for(int i = 0; i < D; ++i)
			in >> u >> v;
			
		for(int i = 0; i < N-1; ++i)
			dist[i] = mat[i][i+1];
			
		cum[0] = dist[0];
		for(int i = 1; i < N-1; ++i)
			cum[i] = cum[i-1] + dist[i];
	
		memset(dp,-1,sizeof(dp));
		
		out << fixed << setprecision(6) << "Case #" << tc << ": " << solve(0,0) << endl;
		
	}
	
}
