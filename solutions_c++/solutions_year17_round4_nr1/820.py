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

int dp4[101][101][101];
int dp3[101][101];

int bt4(int a,int b,int c) {
	if(a + b + c == 0)
		return 0;
	if(a <= 0 && b <= 0 && c <= 0)
		return 0;
	int & ref = dp4[a][b][c];
	if(ref != -1)
		return ref;
	ref = 0;
	for(int i = 0;i <= 4;i++) {
		for(int j = 0;j <= 4;j++) {
			for(int k = 0;k <= 4;k++) {
				if((i + j * 2 + k * 3)%4 == 0 && i <= a && j <= b && k <= c) {
					ref = max(ref,1 + bt4(a - i,b - j,c - k));
				}
				if((i + j * 2 + k * 3)%4 == 0 && i >= a && j >= b && k >= c) {
					ref = max(ref,1 + bt4(a - i,b - j,c - k));
				}
			}
		}
	}
	return ref;
}

int bt3(int a,int b) {
	if(a + b == 0)
		return 0;
	if(a < 0 && b < 0)
		return 0;
	int & ref = dp3[a][b];
	if(ref != -1)
		return ref;
	ref = 0;
	for(int i = 0;i <= 3;i++) {
		for(int j = 0;j <= 3;j++) {
			if((i + j * 2)%3 == 0 && i <= a && j <= b) {
				ref = max(ref,1 + bt3(a - i,b - j));
			}
			if((i + j * 2)%3 == 0 && i > a && j > b) {
				ref = max(ref,1 + bt3(a - i,b - j));
			}
		}
	}
	return ref;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);


	memset(dp4,-1,sizeof dp4);
	memset(dp3,-1,sizeof dp3);

	int T,C = 1;
	cin>>T;
	while(T--) {

		cout<<"Case #"<<C++<<": ";

		int N,P,x;
		cin>>N>>P;
		vector<int> cnt(P);
		for(int i = 0;i < N;i++) {
			cin>>x;
			cnt[x%P]++;
		}
		if(P == 2) {
			cout<<cnt[0] + ((cnt[1]+1)>>1)<<'\n';
			continue;
		}
		if(P == 3) {
			cout<<cnt[0] + bt3(cnt[1],cnt[2])<<'\n';
			continue;
		}
		cout<<cnt[0] + bt4(cnt[1],cnt[2],cnt[3])<<'\n';
	}

	return 0;
}
