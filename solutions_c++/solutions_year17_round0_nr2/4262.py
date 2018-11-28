#include <cstdlib>
#include <iostream>
#include <cstring>
#include <fstream>
#include <algorithm>
using namespace std;
int T;
typedef long long ll;
string x;
ll dp[21][10];
ll nove[18];
ll potd[18];

ll solve(int pos, int lu){
	if(pos < 0) return 0;
	if(dp[pos][lu] != -1) return dp[pos][lu];
	ll ans = -1000000000000000001;
	int curf = x[pos] - '0';
	if( curf >= lu) ans = max(ans, 1ll*curf*potd[pos] + solve(pos-1,curf));
	if(curf-1>= lu) ans = max(ans, 1ll*(curf-1)*potd[pos] + nove[pos]);
	//cout << pos << " " << curf << "(" << lu  << ")" << " ANS: " << ans << endl;
	return dp[pos][lu] = ans;
}

int main(){
	fstream in;
	fstream out;
	out.open("output.txt",ios::out);
	in.open("input.txt",ios::in);
	in >> T;
	ll dec = 1;
	potd[0] = 1;
	for(int i = 1; i <= 18; ++i){
		nove[i] = nove[i-1] + dec*9;
		dec = dec*10;
		potd[i] = dec;
	}
	for(int tc = 1; tc <= T; ++tc){
		memset(dp,-1,sizeof(dp));
		in >> x;
		reverse(x.begin(),x.end());
		out << "Case #" << tc  << ": " << solve(x.length()-1,0) << endl;
		
	}
	

}
