#include <cstdio>

using namespace std;

struct Node{
	long long space;
	long long number;
}S[2],preS[2];

int main(){
	int T;
	long long N,K,tmp;
	scanf("%d",&T);
	for(int i=1;i<=T;++i){
		scanf("%ld %ld",&N,&K);
		preS[0].space = N;
		preS[0].number = 1;
		preS[1].space = 0;
		preS[1].number = 0;
		tmp = 0;
		while(true){
			if (tmp + preS[0].number >= K){
				printf("Case #%d: %lld %lld\n",i,preS[0].space/2,(preS[0].space-1)/2);
				break;
			}
			tmp += preS[0].number;
			if(tmp + preS[1].number >=K){
				printf("Case #%d: %lld %lld\n",i,preS[1].space/2,(preS[1].space-1)/2);
				break;
			}
			tmp += preS[1].number;
			S[0].space = preS[0].space/2;
			S[1].space = S[0].space - 1;
			if( preS[0].space % 2){
				S[0].number = preS[0].number * 2 + preS[1].number;
				S[1].number = preS[1].number;
			}
			else{
				S[0].number = preS[0].number;
				S[1].number = preS[0].number + preS[1].number * 2;
			}
			preS[0].space = S[0].space;
			preS[0].number = S[0].number;
			preS[1].space = S[1].space;
			preS[1].number = S[1].number;
		}
	}
	return 0;
}
