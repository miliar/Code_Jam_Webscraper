#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <iomanip>
#include <fstream>
using namespace std;
int T; int N; int P;
int X[5];
int dp[101][101][101][4];

int solve(int l1, int l2, int l3, int lo){
	if(dp[l1][l2][l3][lo] != -1) return dp[l1][l2][l3][lo];
	if(l1 == 0 && l2 == 0 && l3 == 0) return 0;
	int ans = 999999;
	if(l1 > 0)
		ans = min( ans,solve(l1-1,l2,l3, (lo + 1)%P));
	if(l2 > 0)
		ans = min( ans,solve(l1,l2-1,l3, (lo + 2)%P));
	if(l3 > 0)
		ans = min( ans,solve(l1,l2,l3-1, (lo + 3)%P));
	if(lo > 0)
		ans++;
	return dp[l1][l2][l3][lo] = ans;
}

int main(){
	fstream in;
	fstream out;
	out.open("output.txt",ios::out);
	in.open("input.txt",ios::in);
	in >> T;
	for(int tc = 1; tc <= T; ++tc){
		
		in >> N >> P;
		for(int i = 0; i < 5; ++i)
			X[i] = 0;
			
		for(int i = 0; i < N; ++i){
			int g;
			in >> g;
			X[P - (g % P)]++;
		}
		memset(dp,-1,sizeof(dp));	
		out << setprecision(8) << fixed << "Case #" << tc << ": " << N - solve(X[1],X[2],X[3],0) << endl;

	}
}
	

