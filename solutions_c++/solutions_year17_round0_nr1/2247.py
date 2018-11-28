#include <iostream>
#include <cstring>
using namespace std;


int T = 0, t = 0, K = 0;
char S[1005];
int main(){
	freopen("codejam01_in.txt", "r", stdin);
	freopen("codejam01_out.txt", "w", stdout);
	cin>>T;
	while(t++ < T){
		cin>>S>>K;
		int nflip = 0;
		bool flag = 1;
		for(int i = 0; i<strlen(S); i++){
			if(S[i] == '+')
				continue;

			if(strlen(S+i) < K){
				printf("Case #%d: IMPOSSIBLE\n", t);
				flag = 0;
				break;
			}
			nflip++;
			for(int j = 0; j<K; j++){
				if(S[i+j] == '+')
					S[i+j] = '-';
				else if(S[i+j] == '-')
					S[i+j] = '+';
			}
		}
		if(flag)
			printf("Case #%d: %d\n", t, nflip);
	}
	return 0;
}