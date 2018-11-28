#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
int Case;
int n;
char S[1000];
int K, cnt;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&Case);
	for (int CASE=1; CASE<=Case; CASE++){
		printf("Case #%d: ", CASE);
		scanf("%s",S);
		n = strlen(S);
		scanf("%d", &K);
		cnt = 0;
		for (int i=0; i<=n-K; i++){
			if (S[i]=='-'){
				cnt++;
				for (int j=0; j<K; j++){
					if (S[i+j]=='-')
						S[i+j]='+';
					else S[i+j]='-';
				}
			}
		}
		bool flag = true;
		for (int i=n-K+1; i<n; i++)
			if (S[i]!='+') flag = false;
		if (flag) printf("%d\n", cnt);
			else printf("IMPOSSIBLE\n");
	}
	return 0;
}
