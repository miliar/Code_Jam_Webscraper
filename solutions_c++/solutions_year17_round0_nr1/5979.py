#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>
#include<utility>
#define PB push_back
#define MP make_pair
#define _F first
#define _S second

using namespace std;

int main(int argc, char* argv[]){
	int T, K;
	char line[10000];
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		printf("Case #%d: ", i);
		bool flag = true;
		scanf("%s%d", line, &K);
		int len = strlen(line);
		int cnt = 0;
		for(int j = 0; j <= len-K; j++){
			if(line[j] == '+') continue;
			cnt++;
			for(int k = 0; k < K; k++){
				if(line[j+k] == '+')
					line[j+k] = '-';
				else
					line[j+k] = '+';
			}
		}
		for(int j = 0; j < len; j++)
			if(line[j] == '-') flag = false;
		if(flag)
			printf("%d\n", cnt);
		else
			puts("IMPOSSIBLE");
	} 
    return 0;
}
