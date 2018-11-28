#include <bits/stdc++.h>
using namespace std;

const int MAXSIZE = 10000;
struct EMPTY{
	int MAX;
	int MIN;
};

vector<vector<EMPTY> > VALUES(MAXSIZE+1);

bool comparator(EMPTY A, EMPTY B){
	int TOTAL_A = A.MAX + A.MIN;
	int TOTAL_B = B.MAX + B.MIN;
	
	return TOTAL_A > TOTAL_B;
}

void STALL(){
    
    EMPTY Z = {0,0};
    EMPTY O = {1,0};
    
    
	VALUES[1].push_back(Z);
	VALUES[2].push_back(O);
	VALUES[2].push_back(Z);
	
	
	for(int i = 3; i <= MAXSIZE; i++){
		for(int j = 0; j < i; j++)
		    VALUES[i].push_back(Z);
	}
	
	for(int i = 3; i <= MAXSIZE; i++){
		int L = 0;
		int R = 0;
		
		if(i%2 == 0){
			L = (i-1)/2;
			R = i/2;
		}
		else{
			L = (i-1)/2;
			R = (i-1)/2;
		}
		
		
		VALUES[i][0].MAX = R;
		VALUES[i][0].MIN = L;
		
		merge(VALUES[L].begin(),VALUES[L].end(),VALUES[R].begin(),VALUES[R].end(),VALUES[i].begin()+1,comparator);
		
	}
}

vector<EMPTY> G;

void BUILD(int N){
    int L = 0;
	int R = 0;
	
	if(N%2 == 0){
		L = (N-1)/2;
		R = N/2;
	}
	else{
		L = (N-1)/2;
		R = (N-1)/2;
	}
	
	EMPTY T = {R,L};
	G.push_back(T);
	
	if(R <= MAXSIZE)
        G.insert(G.end(),VALUES[R].begin(),VALUES[R].end());
    else
        BUILD(R);
        
    if(L <= MAXSIZE)
        G.insert(G.end(),VALUES[L].begin(),VALUES[L].end());
    else
        BUILD(L);
}

EMPTY GET(int N,int K){
    BUILD(N);
    sort(G.begin(),G.end(),comparator);
    EMPTY ANS = {G[K-1].MAX, G[K-1].MIN};
    G.clear();
    return ANS;
}

int main(){
	STALL();
	int T = 0;
	scanf("%d", &T);
	
	for(int i = 1; i <= T; i++){
		int N = 0;
		int K = 0;
		
		scanf("%d %d", &N, &K);
		
		printf("Case #%d: ", i);
		
		if(N <= MAXSIZE){
			printf("%d %d\n", VALUES[N][K-1].MAX, VALUES[N][K-1].MIN);
		}
		else{
			EMPTY ANS = GET(N,K);
			printf("%d %d\n", ANS.MAX, ANS.MIN);
		}
	}
	
	return 0;
}
