#include <bits/stdc++.h>
using namespace std;
int main() {
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		char cake[25][26];
		vector<int> pos[25];
		int R,C;
		scanf("%d %d",&R,&C);
		for(int i=0;i<R;i++) {
			scanf("%s",cake[i]);
			for(int j=0;j<C;j++) {
				if(cake[i][j]!='?') pos[i].push_back(j);
			}
			pos[i].push_back(C);
		}
		int idx=0;
		int Llen=0;
		while(idx<R) {
			if(pos[idx].size()==1) {idx++;Llen++;continue;}
			int Rlen=1;
			while(idx+Rlen<R && pos[idx+Rlen].size()==1) Rlen++;
			 for(int i=idx-Llen;i<idx+Rlen;i++) {
			 	int k=1;
			 	for(int j=0;j<C;j++) {
			 		if(j==pos[idx][k]) k++;
			 		cake[i][j]=cake[idx][pos[idx][k-1]];
			 	}
			 }
			 Llen=0;
			 idx+=Rlen;
		}
		printf("Case #%d:\n",t);
		for(int i=0;i<R;i++) {
			printf("%s\n",cake[i]);
		}
	}
}
