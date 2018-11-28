#include <cstdlib>
#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
int T;
int dp[722][722][2][2]; // iniziale, finale, starting, who
int C,J;
int minu[1500];  // 0 cameron, // 1 james, // -1 free

int solve(int c, int j, int start, int w){
	int pos = c+j;
	if(pos == 1440) return start != w;
	if(dp[c][j][start][w] != -1) return dp[c][j][start][w];
	int ans = 1500;
	if(minu[pos] != 0 && c < 720){ // lo voglio assegnare a cameron
		if(w != 0)
			ans = min( ans,  solve(c+1,j,start,0) + 1);
		else ans = min( ans,  solve(c+1,j,start,0));
	}
	
	if(minu[pos] != 1 && j < 720){ // lo voglio assegnare a james
		if(w != 1)
			ans = min( ans, solve(c,j+1,start,1) + 1);
		else ans = min( ans, solve(c,j+1,start,1));
	}
	return dp[c][j][start][w]  = ans;
	
}
int main(){
	fstream in;
	fstream out;
	out.open("output.txt",ios::out);
	in.open("input.txt",ios::in);
	in >> T;
	for(int tc = 1; tc <= T; ++tc){
		in >> C >> J;
		memset(dp,-1,sizeof(dp));
		memset(minu,-1,sizeof(minu));
		int l,r;
		for(int i = 0; i < C; ++i){
			in >> l >> r;
			for(int j = l; j < r; ++j)
				minu[j] = 0;
		}
		for(int i = 0; i < J; ++i){
			in >> l >> r;
			for(int j = l; j < r; ++j)
				minu[j] = 1;
		}
		int ans = 1500;
		if(minu[0] != 0) // lo assegno a cameron
			ans = min(ans, solve(1,0,0,0));
			
		//cout << ans << endl;
		if(minu[0] != 1) // lo assegno a james
			ans = min(ans, solve(0,1,1,1));
		out << "Case #" << tc << ": " << ans << endl;
		
		
	}
}
