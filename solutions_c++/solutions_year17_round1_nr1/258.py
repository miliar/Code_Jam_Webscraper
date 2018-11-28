#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		int N,M;
		scanf ("%d %d",&N,&M);
		char S[30][30];
		for (int i=0;i<N;i++) scanf ("%s",S[i]);
		for (int i=0;i<N;i++){
			for (int j=1;j<M;j++) if (S[i][j] == '?' && S[i][j-1] != '?'){
				S[i][j] = S[i][j-1];
			}
			for (int j=M-2;j>=0;j--) if (S[i][j] == '?' && S[i][j+1] != '?'){
				S[i][j] = S[i][j+1];
			}
		}

		for (int i=1;i<N;i++){
			if (S[i][0] == '?' && S[i-1][0] != '?'){
				for (int j=0;j<M;j++) S[i][j] = S[i-1][j];
			}
		}
		for (int i=N-2;i>=0;i--){
			if (S[i][0] == '?' && S[i+1][0] != '?'){
				for (int j=0;j<M;j++) S[i][j] = S[i+1][j];
			}
		}

		printf ("Case #%d:\n",Case);
		for (int i=0;i<N;i++) puts(S[i]);
	}

	return 0;
}