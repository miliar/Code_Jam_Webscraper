



#include<deque>
#include<queue>
#include<map>
#include<string>
#include<iostream>
#include<set>
#include<cmath>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<functional>
//#define scanf scanf_s
#define fir first
#define sec second
#define mp make_pair
#define mt make_tuple
#define pub push_back
using namespace std;
typedef long long int llint;
const llint one = 1;
const llint big = (one<<30);
const llint mod=1000000007;


int main(void){
	int T;
	auto fi=fopen("GCJansA.txt","w");
	scanf("%d",&T);
	for(int ias=1;ias<=T;ias++){ fprintf(fi,"Case #%d:\n",ias);
	int R,C,i,j;
	vector<string> cake;
	scanf("%d %d",&R,&C);
	cake.resize(R);
	for(i=0;i<R;i++){
		cin>>cake[i];
	}
	for(i=0;i<R;i++){
		for(j=0;j<C;j++){
			if(cake[i][j]=='?'&&j>0){
				cake[i][j]=cake[i][j-1];
			}
		}
	}
	for(i=0;i<R;i++){
		for(j=C-1;j>=0;j--){
			if(cake[i][j]=='?'&&j<C-1){
				cake[i][j]=cake[i][j+1];
			}
		}
	}
	for(j=0;j<C;j++){
		for(i=0;i<R;i++){
			if(cake[i][j]=='?'&&i>0){
				cake[i][j]=cake[i-1][j];
			}
		}
	}
	for(j=0;j<C;j++){
		for(i=R-1;i>=0;i--){
			if(cake[i][j]=='?'&&i<R-1){
				cake[i][j]=cake[i+1][j];
			}
		}
	}
	for(i=0;i<R;i++){
		for(j=0;j<C;j++){
			fprintf(fi,"%c",cake[i][j]);
		}
		fprintf(fi,"\n");
	}
	}
	return 0;
}

