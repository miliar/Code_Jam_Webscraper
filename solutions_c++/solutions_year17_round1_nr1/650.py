#include<bits/stdc++.h>
using namespace std;
char gcj[51][51];
int visited[26];
int main(){
	int t;
	scanf("%d",&t);
	for(int turn = 1; turn <= t; turn++){
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++) scanf("%s",gcj[i]);
		for(int i=0;i<26;i++) visited[i] = 0;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(gcj[i][j] == '?') continue;
				if(visited[gcj[i][j] - 'A']) continue;
				visited[gcj[i][j]-'A'] = 1;
				int ss = j-1, ee = j+1;
				char now = gcj[i][j];
				while(ee<m && gcj[i][ee]=='?') ee++;
				while(ss>=0 && gcj[i][ss]=='?') ss--;
				ss++;ee--;
				for(int k=ss;k<=ee;k++){
					gcj[i][k] = now;
				}
				int roww = i+1;
				while(roww < n){
					int valid = true;
					for(int k=ss;k<=ee;k++){
						if(gcj[roww][k] != '?'){
							valid = false;
							break;
						}
					}
					if(!valid) break;
					for(int k=ss;k<=ee;k++){
						gcj[roww][k] = now;
					}
					roww++;
				}
				roww = i-1;
				while(roww >= 0){
					int valid = true;
					for(int k=ss;k<=ee;k++){
						if(gcj[roww][k] != '?'){
							valid = false;
							break;
						}
					}
					if(!valid) break;
					for(int k=ss;k<=ee;k++){
						gcj[roww][k] = now;
					}
					roww--;
				}
			}
		}
		printf("Case #%d:\n", turn);
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				printf("%c",gcj[i][j]);
			}
			printf("\n");
		}
	}
}
