#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
typedef pair<int,int> ii;
typedef vector<ii> vii;
int main(){
	int t,r,c,lines[26];
	char cake[26][26],ch;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++){
		scanf("%d %d",&r,&c);
		vii pos;
		for(int j = 0; j < r; j++)
			lines[j] = 0;	// Vazia
		for(int j = 0; j < r; j++){
			scanf("%c",&ch);
			for(int k = 0; k < c; k++){
				scanf("%c",&cake[j][k]);
				if(cake[j][k] != '?'){
					lines[j] = 1;
					pos.push_back(make_pair(j,k));
				}
			}
		}
		for(int j = 0; j < pos.size(); j++){
			int row = pos[j].first;
			int col = pos[j].second;
			for(int k = col-1; k >= 0; k--)
				if(cake[row][k] == '?')
					cake[row][k] = cake[row][col];
		}
		for(int j = 0; j < r; j++){
			for(int k = 0; k < c; k++){
				if(cake[j][k] == '?'){
					if(lines[j] == 0){
						int next;
						next = j-1;
						while(next >= 0 && cake[next][k] == '?')next--;
						if(next >= 0) cake[j][k] = cake[next][k];
						else{
							next = j+1;
							while(next < r && cake[next][k] == '?')next++;
							if(next < r) cake[j][k] = cake[next][k];
							else{
								next = k-1;
								while(next >= 0 && cake[j][next] == '?')next--;
								cake[j][k] = cake[j][next];
							}
						}
					} else {
						int next = k-1;
						while(next >= 0 && cake[j][next] == '?')next--;
						cake[j][k] = cake[j][next];
					}
				}
			}
		}
		printf("Case #%d:\n",i);
		for(int j = 0; j < r; j++){
			for(int k = 0; k < c; k++)
				printf("%c",cake[j][k]);
			printf("\n");
		}
	}
}

