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

string g[100];
string g2[100];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	srand(time(NULL));

	int T,C = 1;
	cin>>T;
	while(T--) {
		cout<<"Case #"<<C++<<":";
		cout<<'\n';

		int R,C;
		cin>>R>>C;
		for(int i = 0;i < R;i++)
			cin>>g[i],g2[i] = g[i];
		int lasti = -1;
		for(int i = 0;i < R;i++) {
			int lastj = -1;
			int toi = i;
			for(int k = i + 1;k < R;k++) {
				bool can = true;
				for(int z = 0;z < C;z++) {
					can &= g[k][z] == '?';
				}
				if(!can)
					break;
				toi = k;
			}
			bool f = false;
			for(int j = 0;j < C;j++) {
				if(g[i][j] == '?')
					continue;
				f = true;
				int toj = j;
				for(int k = j + 1;k < C;k++) {
					if(g[i][k] != '?')
						break;
					toj = k;
				}
				for(int i1 = lasti + 1;i1 <= toi;i1++) {
					for(int j1 = lastj + 1;j1 <= toj;j1++) {
						g2[i1][j1] = g[i][j];
					}
				}
				lastj = toj;
			}
			if(f)
				lasti = toi;
		}
		for(int i = 0;i < R;i++) {
			cout<<g2[i]<<'\n';
		}

	}
	return 0;
}
/**/
