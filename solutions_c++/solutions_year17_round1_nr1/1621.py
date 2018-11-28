#include <bits/stdc++.h>
using namespace std;
int main(){
	freopen("stdin.txt","r",stdin);
	freopen("stdout.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int u=1;u<=t;u++){
		int r,c;
		scanf("%d %d",&r,&c);
		scanf("\n");
		char s[r+1][c+1];
		bool done[r];
		int idx=-1;
		bool marked = false;
		for(int i=0;i<r;i++){
			done[i] = 0;
			for(int j=0;j<c;j++){
				scanf("%c",&s[i][j]);
				if(s[i][j]!='?' && marked==false){
					idx = i;
					marked = true;
				}
			}
			scanf("\n");
		}
		char curr;
		if(s[idx][0]=='?'){
			for(int i=0;i<c;i++){
				if(s[idx][i]!='?'){
					curr = s[idx][i];
					break;
				}
			}
			for(int i=0;i<c;i++){
				if(s[idx][i]=='?'){
					s[idx][i] = curr;
				}
				else{
					curr = s[idx][i];
				}
			}
		}
		else{
			curr = s[idx][0];
			for(int i=1;i<c;i++){
				if(s[idx][i]=='?'){
					s[idx][i] = curr;
				}
				else{
					curr = s[idx][i];
				}
			}
		}
		done[idx] = true;

		for(int k=idx-1;k>=0;k--){
			int qc = 0;
			for(int i=0;i<c;i++){
				if(s[k][i]=='?'){
					qc++;
				}
			}
			if(qc==c){
				for(int i=0;i<c;i++){
					s[k][i] = s[k+1][i];
				}
				continue;
			}
			if(s[k][0]=='?'){
				for(int i=0;i<c;i++){
					if(s[k][i]!='?'){
						curr = s[k][i];
						break;
					}
				}
				for(int i=0;i<c;i++){
					if(s[k][i]=='?'){
						s[k][i] = curr;
					}
					else{
						curr = s[k][i];
					}
				}
			}
			else{
				curr = s[k][0];
				for(int i=1;i<c;i++){
					if(s[k][i]=='?'){
						s[k][i] = curr;
					}
					else{
						curr = s[k][i];
					}
				}
			}
			done[k] = true;
		}
		for(int k=idx+1;k<r;k++){
			int qc = 0;
			for(int i=0;i<c;i++){
				if(s[k][i]=='?'){
					qc++;
				}
			}
			if(qc==c){
				for(int i=0;i<c;i++){
					s[k][i] = s[k-1][i];
				}
				continue;
			}
			if(s[k][0]=='?'){
				for(int i=0;i<c;i++){
					if(s[k][i]!='?'){
						curr = s[k][i];
						break;
					}
				}
				for(int i=0;i<c;i++){
					if(s[k][i]=='?'){
						s[k][i] = curr;
					}
					else{
						curr = s[k][i];
					}
				}
			}
			else{
				curr = s[k][0];
				for(int i=1;i<c;i++){
					if(s[k][i]=='?'){
						s[k][i] = curr;
					}
					else{
						curr = s[k][i];
					}
				}
			}
			done[k] = true;
		}
		printf("Case #%d:\n",u);
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				printf("%c",s[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}