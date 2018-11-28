#include<cstdio>
#include<cstring>
using namespace std;

int main(){
    int T;
    scanf(" %d ", &T);
    for(int t=1; t<=T; ++t){
	char line[1001];
	int K;
	scanf("%s", line);
	scanf(" %d ", &K);
	int l = strlen(line);
	int res = 0;
	for(int i=0; i<l-K+1; ++i){
	    if(line[i] == '-'){
		++res;
		for(int j=0; j<K; ++j){
		    if(line[i+j] == '-') line[i+j] = '+';
		    else line[i+j] = '-';
		}
	    }
	}
	bool valid = true;
	for(int i=0; i<l; ++i){
	    if(line[i] == '-') valid = false;
	}
	if(valid) printf("Case #%d: %d\n", t, res);
	else printf("Case #%d: IMPOSSIBLE\n", t);
    }
    return 0;
}
