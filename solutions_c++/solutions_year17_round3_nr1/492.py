#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <iomanip>
#include <fstream>
#define PI 3.14159265359
using namespace std;
int T; 
int N;
int K;
double dp[1001][1001];
int R[1001];
int H[1001];
int o[1001];
double solve(int n, int k){
	if(k == 0) return 0;
	if(n == N) return -10e20;
	if(dp[n][k] < -2 || dp[n][k] > -0.5) return dp[n][k];
	double ans = 0;
	int h = H[o[n]];
	int r = R[o[n]];
	ans+= max( solve(n+1,k), solve(n+1,k-1) + 1.0*2*h*r);
	return dp[n][k] = ans;
	
}

bool cmp(int x, int y){
	return R[x] > R[y];
}

int main(){
	fstream in;
	fstream out;
	out.open("output.txt",ios::out);
	in.open("input.txt",ios::in);
	in >> T;
	for(int tc = 1; tc <= T; ++tc){
		in >> N >> K;
		double ans = 0;
		memset(dp,-1,sizeof(dp));
		for(int i = 0; i < N; ++i){
			in >> R[i] >> H[i];
			o[i] = i;
		}
		sort(o,o+N,cmp);
		
		for(int i = 0; i < N; ++i){
		//	cout << PI*(1.0*R[o[i]])*(1.0*R[o[i]]) + 2.0*PI*H[o[i]]*R[o[i]] << " " <<  solve(i+1,K-1) <<  " " << o[i] << endl;
			ans = max((1.0*R[o[i]])*(1.0*R[o[i]]) + 2.0*H[o[i]]*R[o[i]] + solve(i+1,K-1), ans);
		}
		out << setprecision(8) << fixed << "Case #" << tc << ": " << ans*PI << endl;
			
		cout << endl;
	}
}
	

