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


typedef vector<int> VI;
typedef vector<VI> VVI;

bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
	for (int j = 0; j < w[i].size(); j++) {
		if (w[i][j] && !seen[j]) {
			seen[j] = true;
			if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
				mr[i] = j;
				mc[j] = i;
				return true;
			}
		}
	}
	return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
	mr = VI(w.size(), -1);
	mc = VI(w[0].size(), -1);

	int ct = 0;
	for (int i = 0; i < w.size(); i++) {
		VI seen(w[0].size());
		if (FindMatch(i, w, mr, mc, seen)) ct++;
	}
	return ct;
}

void fix(VVI &w,VI &mr, VI &mc,int cnt) {
	for(int i = 0;i < cnt;i++) {
		if(mr[i] != -1) {
			for(int j = 0;j < cnt;j++) {
				if(j != mr[i])
					w[i][j] = 0;
			}
		}
		if(mc[i] != -1) {
			for(int j = 0;j < cnt;j++) {
				if(j != mc[i])
					w[j][i] = 0;
			}
		}
	}
}

int g[300][300];
int orgG[300][300];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T,C = 1;
	cin>>T;
	//	{
	//		srand(time(NULL));
	//		T = 100;
	//	}
	while(T--) {
		cout<<"Case #"<<C++<<": ";

		int N,M,r,c;
		string s;
		cin>>N>>M;
		memset(g,0,sizeof g);
		memset(orgG,0,sizeof orgG);
		int resS = 0,resC = 0;
		for(int i = 0;i < M;i++) {
			cin>>s>>r>>c;
			r--,c--;
			if(s[0] == '+')
				g[r][c] = 1;
			if(s[0] == 'x')
				g[r][c] = 2;
			if(s[0] == 'o')
				g[r][c] = 3;
			orgG[r][c] = g[r][c];
		}

		{ // x
			VVI w(N,VI(N,1));
			VI mr(N,-1),mc(N,-1);
			for(int i = 0;i < N;i++) {
				for(int j = 0;j < N;j++) {
					if(g[i][j]&2) {
						mr[i] = j;
						mc[j] = i;
						break;
					}
				}
			}
			for(int i = 0;i < N;i++) {
				if(mr[i] != -1) {
					for(int j = 0;j < N;j++) {
						if(j != mr[i])
							w[i][j] = 0;
					}
				}
				if(mc[i] != -1) {
					for(int j = 0;j < N;j++) {
						if(j != mc[i])
							w[j][i] = 0;
					}
				}
			}
			fix(w,mr,mc,N);
			BipartiteMatching(w,mr,mc);
			for(int i = 0;i < N;i++) {
				if(mr[i] != -1)
					g[i][mr[i]] |= 2;
			}
		}

		{ // +
			int cnt = 2 * N - 1;
			VVI w(cnt,VI(cnt,0));
			VI mr(cnt,-1),mc(cnt,-1);
			for(int i = 0;i < N;i++) {
				for(int j = 0;j < N;j++) {
					if(g[i][j]&1) {
						mr[i+j] = i-j+N-1;
						mc[i-j+N-1] = i+j;
					}
					w[i+j][i-j+N-1] = 1;
				}
			}
			fix(w,mr,mc,cnt);
			BipartiteMatching(w,mr,mc);
			for(int i = 0;i < cnt;i++) {
				if(mr[i] != -1)
					g[(i+mr[i]-N+1)>>1][(i-mr[i]+N-1)>>1] |= 1;
			}
		}


		{ // validate
			for(int i = 0;i < N;i++) {
				for(int j = 0;j < N;j++) {
					assert(g[i][j] >= orgG[i][j]);
				}
			}

			for(int i = 0;i < N;i++) {
				int cntX = 0;
				for(int j = 0;j < N;j++) {
					cntX += (g[i][j] & 2) > 0;
				}
				assert(cntX <= 1);
			}
			
			for(int i = 0;i < N;i++) {
				int cntX = 0;
				for(int j = 0;j < N;j++) {
					cntX += (g[j][i] & 2) > 0; 
				}
				assert(cntX <= 1);
			}

			for(int i = 0;i < 2*N-1;i++) {
				int cntX = 0;
				for(int j = 0;j < min(i+1,N);j++) {
					cntX += g[i-j][j] & 1;
				}
				assert(cntX <= 1);
			}

			for(int i = 0;i < 2*N-1;i++) {
				int cntX = 0;
				for(int j = 0;j < min(i+1,N);j++) {
					cntX += g[i+j-N+1][j] & 1;
				}
				assert(cntX <= 1);
			}
		}

		for(int i = 0;i < N;i++) {
			for(int j = 0;j < N;j++) {
				resC += g[i][j] > 0 && orgG[i][j] != g[i][j];
				resS += g[i][j] > 0;
				resS += g[i][j] > 2;
			}
		}
		cout<<resS<<' '<<resC<<'\n';
		for(int i = 0;i < N;i++) {
			for(int j = 0;j < N;j++) {
				//				cerr<<g[i][j]<<" \n"[j+1 == N];
				if(g[i][j] == orgG[i][j])
					continue;
				if(g[i][j] == 1) {
					cout<<"+ "<<i+1<<' '<<j+1<<'\n';
				}
				if(g[i][j] == 2) {
					cout<<"x "<<i+1<<' '<<j+1<<'\n';
				}
				if(g[i][j] == 3) {
					cout<<"o "<<i+1<<' '<<j+1<<'\n';
				}
			}
		}

		//		cout<<endl;
	}
	return 0;
}
/**/
