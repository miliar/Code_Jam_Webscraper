#include<iostream>
#include<string>
#include<algorithm>
#include<utility>
#include<vector>
using namespace std;


void llenaIzq(vector<string> &G, int k, int l, char c){
	int i = k-1, j= l;
	while(i>=0 && G[i][j]=='?'){
		G[i][j] = c;
		i--;
	}
	i = k;
	while(i>=0 && G[i][l]==c){
		j = l-1;
		while(j>=0 && G[i][j]=='?'){
			G[i][j] = c;
			j--;
		}
		i--;
	}
}


void llenaDerecha(vector<string> &G, int c, int k){
	int l = c-1;
	while(l>=0 && G[k][l]=='?') l--;
	char ch = G[k][l];
	l++;
	while(k>=0 && G[k][l]=='?'){
		for(int j = l;j<c && G[k][j]=='?';j++){
			G[k][j]=ch;
		}
		k--;
	}
}


void llenaAbajo(vector<string> &G, int r, int c){
	for(int i=0;i<c;i++){
		int j;
		for(j=r-1;j>=0 && G[j][i]=='?';j--);
		char ch = G[j][i];
		for( ; j<r;j++)
			G[j][i]=ch;
	}
}


void llena(vector<string> &G, int r, int c){
	bool cambioRenglon = false;
	for(int i=0;i<r;i++){
		cambioRenglon = false;
		for(int j=0;j<c;j++){
			if(G[i][j]!='?'){
				cambioRenglon = true;
				llenaIzq(G,i,j,G[i][j]);
			}
		}
		if(cambioRenglon){
			llenaDerecha(G,c,i);
		}
	}
	llenaAbajo(G,r,c);
}


int main(){
	int T;
	int r, c;
	cin >> T;
	for(int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": " << endl;
		cin >> r >> c;
		vector<string> Grid(r);
		for(int i=0;i<r;i++)
			cin >> Grid[i];
		llena(Grid,r,c);
		for(int i=0;i<r;i++){
			cout << Grid[i] << endl;
		}
	}
	return 0;

}
