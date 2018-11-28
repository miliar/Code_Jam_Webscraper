#include<cstdio>
#include<cstring>
using namespace std;

int main(){
    int T;
    scanf(" %d ", &T);
    for(int t=1; t<=T; ++t){
	char N[20];
	scanf("%s", N);
	int ill = 1;
	int l = strlen(N);
	while(ill < l){
	    if(N[ill] < N[ill-1]) break;
	    ++ill;
	}
	if(ill < l){
	    --ill;
	    while(ill > 0){
		if(N[ill]-1 >= N[ill-1]) break;
		--ill;
	    }
	    N[ill] -= 1;
	    ++ill;
	    while(ill < l){
		N[ill] = '9';
		++ill;
	    }
	}
	int ind = 0;
	while(N[ind] == '0') ++ind;
	printf("Case #%d: %s\n", t, N+ind);
    }
    return 0;
}
