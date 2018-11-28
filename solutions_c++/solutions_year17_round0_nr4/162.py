#include <stdio.h>
#include <vector>
using namespace std;

bool ext(vector<vector<int> > &G, vector<int> &mat, vector<bool> &chk, int x)
{
	if (chk[x]) return false;
	chk[x] = 1;

	for (auto &y : G[x]){
		if (mat[y] == -1 || ext(G,mat,chk,mat[y])){
			mat[y] = x;
			return true;
		}
	}
	return false;
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);

		int N,M; char map[111][111],ans[111][111];

		scanf ("%d %d",&N,&M);
		for (int i=0;i<N;i++) for (int j=0;j<N;j++) map[i][j] = ans[i][j] = '.';
		vector<vector<int> > G[2];
		vector<int> mat[2];
		vector<bool> chkt[2],chkv[2];
		G[0].resize(2*N-1);
		G[1].resize(N);
		mat[0] = vector<int>(2*N-1,-1);
		mat[1] = vector<int>(N,-1);
		chkt[0] = vector<bool>(2*N-1,0);
		chkt[1] = vector<bool>(N,0);
		for (int i=0;i<M;i++){
			char S[5]; int x,y;
			scanf ("%s %d %d",S,&x,&y);
			x--; y--;
			map[x][y] = S[0];
		}

		for (int x=0;x<N;x++) for (int y=0;y<N;y++){
			if (map[x][y] == 'x' || map[x][y] == '.'){
				G[0][x+y].push_back(x+N-1-y);
			}
			else{
				chkt[0][x+y] = 1;
				mat[0][x+N-1-y] = x+y;
			}
			if (map[x][y] == '+' || map[x][y] == '.'){
				G[1][x].push_back(y);
			}
			else{
				chkt[1][x] = 1;
				mat[1][y] = x;
			}
		}

		for (int k=0;k<2;k++){
			for (int i=0;i<G[k].size();i++){
				vector<bool> chk = chkt[k];
				ext(G[k],mat[k],chk,i);
			}
		}

		for (int k=0;k<2;k++){
			int n = G[k].size();
			for (int i=0;i<n;i++) if (mat[k][i] != -1){
				int x,y;
				if (k == 0){
					x = (i + mat[k][i] - (N-1)) / 2;
					y = (mat[k][i] - (i - (N-1))) / 2;
					ans[x][y] = '+';
				}
				else{
					x = mat[k][i];
					y = i;
					if (ans[x][y] == '+') ans[x][y] = 'o';
					else ans[x][y] = 'x';
				}
			}
		}

		int score = 0, add = 0;
		for (int i=0;i<N;i++) for (int j=0;j<N;j++){
			if (ans[i][j] == 'o') score += 2;
			else if (ans[i][j] == '+' || ans[i][j] == 'x') score++;
			if (ans[i][j] != map[i][j]) add++;
		}

		for (int i=0;i<N;i++) for (int j=0;j<N;j++){
			if (ans[i][j] == '.' && map[i][j] != '.'){
				fprintf (stderr,"!?");
			}
			if (ans[i][j] == '+' && (map[i][j] == 'x' || map[i][j] == 'o')){
				fprintf (stderr,"!?");
			}
			if (ans[i][j] == 'x' && (map[i][j] == '+' || map[i][j] == 'o')){
				fprintf (stderr,"!?");
			}
			if (ans[i][j] == 'o' || ans[i][j] == '+'){
				for (int k=-N;k<N;k++) if (k){
					int x = i + k, y = j + k;
					if (0 <= x && x < N && 0 <= y && y < N){
						if (ans[x][y] == 'o' || ans[x][y] == '+'){
							fprintf (stderr,"!?");
						}
					}
					x = i - k, y = j + k;
					if (0 <= x && x < N && 0 <= y && y < N){
						if (ans[x][y] == 'o' || ans[x][y] == '+'){
							fprintf (stderr,"!?");
						}
					}
				}
			}
			if (ans[i][j] == 'o' || ans[i][j] == 'x'){
				for (int k=-N;k<N;k++) if (k){
					int x = i, y = j + k;
					if (0 <= x && x < N && 0 <= y && y < N){
						if (ans[x][y] == 'o' || ans[x][y] == 'x'){
							fprintf (stderr,"!?");
						}
					}
					x = i + k, y = j;
					if (0 <= x && x < N && 0 <= y && y < N){
						if (ans[x][y] == 'o' || ans[x][y] == 'x'){
							fprintf (stderr,"!?");
						}
					}
				}
			}
		}

		printf ("%d %d\n",score,add);
		for (int i=0;i<N;i++) for (int j=0;j<N;j++){
			if (ans[i][j] != map[i][j]) printf ("%c %d %d\n",ans[i][j],i+1,j+1);
		}
	}

	return 0;
}