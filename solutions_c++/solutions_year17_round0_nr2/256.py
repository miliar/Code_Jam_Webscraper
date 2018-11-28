#include <bits/stdc++.h>
using namespace std;
/***********************************************/
/* Dear online judge:
 * I've read the problem, and tried to solve it.
 * Even if you don't accept my solution, you should respect my effort.
 * I hope my code compiles and gets accepted.
 *  ___  __     _______    _______      
 * |\  \|\  \  |\  ___ \  |\  ___ \     
 * \ \  \/  /|_\ \   __/| \ \   __/|    
 *  \ \   ___  \\ \  \_|/__\ \  \_|/__  
 *   \ \  \\ \  \\ \  \_|\ \\ \  \_|\ \ 
 *    \ \__\\ \__\\ \_______\\ \_______\
 *     \|__| \|__| \|_______| \|_______|
 */
const long long mod = 1000000007;

long long base10[100];
long long dp[100][10][2];
int mx;

void get(long long N) {
	memset(base10,0,sizeof base10);
	mx = 0;
	for(int i = 0;N > 0;i++,mx++) {
		base10[i] = N%10;
		N /= 10;
		cerr<<base10[i]<<" \n"[N == 0];
	}
}

long long get() {
	for(int i = 0;i < 10;i++) {
		dp[0][i][1] = 9;
		if(i <= base10[0])
			dp[0][i][0] = base10[0];
		else
			dp[0][i][0] = -1;
	}
	long long p = 1ll;
	for(int d = 1;d < mx;d++) {
		p *= 10ll;
		for(long long i = 0;i < 10;i++) {
			for(int f = 0;f < 2;f++) {
				dp[d][i][f] = -1;
				if(f == 1) {
					dp[d][i][f] = 9 * p + dp[d-1][9][1];
				} else {
					if(i <= base10[d] && dp[d-1][base10[d]][f] >= 0) {
						dp[d][i][f] = base10[d] * p + dp[d-1][base10[d]][0];
					} else if(i < base10[d]) {
						dp[d][i][f] = (base10[d]-1) * p + dp[d-1][base10[d]-1][1];
					} else
						dp[d][i][f] = -1;
				}
			}
		}
	}
	return dp[mx-1][0][0];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T,C = 1;
	long long N;
	cin>>T;
	//	{
	//		srand(time(NULL));
	//		T = 100;
	//	}
	while(T--) {
		cout<<"Case #"<<C++<<": ";

		cin>>N;
		get(N);
		cout<<get();

		cout<<'\n';
	}
	return 0;
}
/**/
