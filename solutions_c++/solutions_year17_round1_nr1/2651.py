#include <bits/stdc++.h>
using namespace std;
int u, t=1, r, c, i, j, R[30][2], C[30];
bool vis[27][27];
char board[27][27];
struct huh{int a; char h;};
vector<huh> V;
void dfs(int x, int y, char l){
	if(vis[x][y])	return;
	if(l=='?'||(board[x][y]!='?'&&board[x][y]!=l))	return;
	if(board[x][y]!='?')	vis[x][y]=true;
	board[x][y]=l;
	R[l-'A'][1]=max(R[l-'A'][1], x);
	R[l-'A'][0]=min(R[l-'A'][0], x);
	if(y==j){
		dfs(x+1, y, l);
		dfs(x-1, y, l);
	}
}
void omfg(int y, char l){
	int i, j, flag=true;
	for(j=y+1; j<=c; j++){
		for(i=R[l-'A'][0]; flag&&(i<=R[l-'A'][1]); i++)
			if(board[i][j]!='?')
				flag=false;
		if(!flag)	break;
		for(i=R[l-'A'][0]; i<=R[l-'A'][1]; i++)
			board[i][j]=l, vis[i][j]=true;
	}
	for(flag=true, j=y-1; j>0; j--){
		for(i=R[l-'A'][0]; flag&&(i<=R[l-'A'][1]); i++)
			if(board[i][j]!='?')
				flag=false;
		if(!flag)	break;
		for(i=R[l-'A'][0]; i<=R[l-'A'][1]; i++)
			board[i][j]=l, vis[i][j]=true;
	}
}

int main(){
	for(cin>>u; t<=u; t++){
		cin>>r>>c;
		V.clear();
		for(i=1; i<=r; i++)
			for(j=1; j<=c; j++)
				vis[i][j]=false;
		for(i=0; i<=c+1; i++)
			vis[0][i]=vis[r+1][i]=true;
		for(i=0; i<=r+1; i++)
			vis[i][0]=vis[i][c+1]=true;
		for(i=0; i<30; i++)
			R[i][0]=1e9, R[i][1]=0;
		for(i=1; i<=r; i++)
			cin>>(board[i]+1);
		for(i=1; i<=r; i++)
			for(j=1; j<=c; j++){
				if(board[i][j]=='?'||vis[i][j])	continue;
				dfs(i, j, board[i][j]);
				V.push_back({j, board[i][j]});
			}
		for(auto obj:V){
			omfg(obj.a, obj.h);
		}
		cout<<"Case #"<<t<<":"<<endl;
		for(i=1; i<=r; i++)
			cout<<(board[i]+1)<<endl;
	}
	return 0;
}
