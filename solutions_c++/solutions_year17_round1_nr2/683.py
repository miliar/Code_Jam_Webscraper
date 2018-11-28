#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
using namespace std;

int N, P;
int R[50];
vector<int> Q[50];

int calculateKits();

int main(){
	
	int T;
	scanf("%d", &T);

	for(int i=1;i<=T;i++){
		
		scanf("%d %d", &N, &P);
		for(int i=0;i<N;i++){
			scanf("%d", &R[i]);
			Q[i].clear();
		}

		for(int i=0;i<N;i++){
			for(int j=0;j<P;j++){
				int tmp;
				scanf("%d", &tmp);
				Q[i].push_back(tmp);
			}		
			sort(Q[i].begin(), Q[i].end());
		}

		int num_kits = calculateKits();
		printf("Case #%d: %d\n", i, num_kits);		
	}
}

int calculateKits(){

	int num = 0;
	for(int n = 1;;){

		bool flag = false;
		bool fit = true;
		bool increase = false;
		for(int i=0;i<N;i++){
			
			if(Q[i].size() == 0){
				flag = true;
				break;
			}
			int q = Q[i].front();
				
			double t = (double) q;

			while( t < 0.9*((double) n)*((double) R[i])){
				
				Q[i].erase(Q[i].begin());

				if(Q[i].size() == 0){
                                	flag = true;
                                	break;
                        	}	
				t = (double) Q[i].front();
			}

			if(flag)
				break;
			if(t > 1.1*((double)n)*((double) R[i])){
				increase = true;
				break;
			}

			
				
		}

		if(flag)
			break;

		if(increase){
			n++;
			continue;
		}

			num++;
			for(int i=0;i<N;i++)
				Q[i].erase(Q[i].begin());
		
	}

	return num;
}
