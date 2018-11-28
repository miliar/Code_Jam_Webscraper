#include<cstdio>
#include<cstdlib>
#include<unordered_map>
using namespace std;

int main(){
    int T;
    scanf(" %d ", &T);
    for(int t=1; t<=T; ++t){
	int N, K;
	scanf(" %d %d ", &N, &K);
	int ips[10001];
	for(int i=0; i<10001; ++i) ips[i] = 0;
	char p_i[8];
	int ipi;
	scanf("%s", p_i);
	int si = 0;
	while(p_i[si] != '.') ++si;
	for(int j=0; j<4; ++j) p_i[si+j] = p_i[si+j+1];
	p_i[si+4] = '\0';
	int U = atoi(p_i);
	for(int i=0; i<N; ++i){
	    scanf("%s", p_i);
	    for(int j=1; j<5; ++j) p_i[j] = p_i[j+1];
	    p_i[5] = '\0';
	    ipi = atoi(p_i);
	    ++ips[ipi];
	}
	int inds = 0;
	while(ips[inds] == 0) ++inds;
	int indn = inds+1;
	while(indn < 10001 && ips[indn] == 0) ++indn;
	while(U > 0){
	    if(U >= (indn-inds)*ips[inds]){
		U -= (indn-inds)*ips[inds];
		ips[indn] += ips[inds];
		inds = indn;
		++indn;
		while(indn < 10001 && ips[indn] == 0) ++indn;
	    }else{
		break;
	    }
	}
	double res = 1.0;
	double pp;
	if(U > 0){
	    pp = inds/10000.0 + U/10000.0/ips[inds];
	    while(ips[inds] > 0){
		res *= pp;
		--ips[inds];
	    }
	    ++inds;
	}
	while(inds < 10001){
	    if(ips[inds] == 0){
		++inds;
		continue;
	    }
	    pp = inds/10000.0;
	    while(ips[inds] > 0){
		res *= pp;
		--ips[inds];
	    }
	    ++inds;
	}
	printf("Case #%d: %lf\n", t, res);
    }
    return 0;
}
