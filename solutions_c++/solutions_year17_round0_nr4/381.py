#include<bits/stdc++.h>
#define OFF 102
#define LIM 444
using namespace std;

bool row[LIM] , col[LIM] , main_dia[LIM] , sub_dia[LIM] , visited[LIM] , e[LIM][LIM];
int start_figure[LIM][LIM] , end_figure[LIM][LIM] , n , m;
int match[LIM];

int dfsrowcol(int u){
	if(visited[u])	return 0;
	visited[u] = true;
	for(int v = 1 ; v <= n ; v++){
		if(col[v])	continue;
		if(match[v] == 0 || dfsrowcol(match[v]) == 1){
			match[v] = u;
			return 1;
		}
	}
	return 0;
}

int dfsDia(int u){
	if(visited[u])	return 0;
	visited[u] = true;
	for(int v = 1 - n ; v <= n - 1 ; v++){
		if(sub_dia[OFF + v])	continue;
		if(!e[u][OFF + v])	continue;
		if(match[OFF + v] == 0 || dfsDia(match[OFF + v]) == 1){
			match[OFF + v] = u;
			return 1;
		}
	}
	return 0;
}

void show(){
	int ans = 0;
	vector < int > xx , yy;
	vector < char > zz;
	for(int x = 1 ; x <= n ; x++)
		for(int y = 1 ; y <= n ; y++){
			if(end_figure[x][y] == 1 || end_figure[x][y] == 2)	ans++;		
			if(end_figure[x][y] == 3)	ans += 2;
			int t = (end_figure[x][y] ^ start_figure[x][y]);
			if(t > 0){
				xx.push_back(x);
				yy.push_back(y);
				int tmp = end_figure[x][y];
				if(tmp == 1)	zz.push_back('+');
				else if(tmp == 2)	zz.push_back('x');
				else zz.push_back('o');
			}
		}
	printf("%d %d\n",ans,xx.size());
	for(int i = 0 ; i < xx.size() ; i++)	printf("%c %d %d\n",zz[i],xx[i],yy[i]);
}

void solve(int Tc){
	scanf("%d %d",&n,&m);
	memset(row , 0 , sizeof row);
	memset(col , 0 , sizeof col);
	memset(main_dia , 0 , sizeof main_dia);
	memset(sub_dia ,  0 , sizeof sub_dia);
	memset(start_figure , 0 , sizeof start_figure);
	memset(end_figure , 0 , sizeof end_figure);
	memset(e , 0 , sizeof e);
	while(m > 0){
		char t[4];
		int x , y;
		scanf("%s %d %d",t,&x,&y);
		if(t[0] == '+')	start_figure[x][y] |= 1;
		else if(t[0] == 'x') start_figure[x][y] |= 2;
		else start_figure[x][y] |= 3;
		m--;
	}
	for(int r = 1 ; r <= n ; r++)
		for(int c = 1 ; c <= n ; c++){
			end_figure[r][c] = start_figure[r][c];
			if(end_figure[r][c] == 2 || end_figure[r][c] == 3){
				row[r] = true;
				col[c] = true;
			}
			if(end_figure[r][c] == 1 || end_figure[r][c] == 3){
				main_dia[r + c] = true;
				sub_dia[OFF + r - c] = true;
 			}
 			e[r + c][r - c + OFF] = true;
		}
	/*------*/
	memset(match , 0 , sizeof match);
	for(int r = 1 ; r <= n ; r++){
		if(row[r])	continue;
		memset(visited , 0 , sizeof visited);
		int tmp = dfsrowcol(r);
	}
	for(int c = 1 ; c <= n ; c++)
		if(match[c] != 0)	end_figure[match[c]][c] |= 2;
	/*---------*/
	memset(match , 0 , sizeof match);
	for(int md = 2 ; md <= 2*n ; md++){
		if(main_dia[md])	continue;
		memset(visited , 0  , sizeof visited);
		int tmp = dfsDia(md);
	}
	for(int sd = 1 - n ; sd <= n - 1 ; sd++){
		if(match[sd + OFF] == 0)	continue;
		int md = match[sd + OFF];
		int r =  (md + sd)/2;
		int c =  (md - sd)/2;
		end_figure[r][c] |= 1;
	}
	printf("Case #%d: ",Tc);
	show();
}

int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int Tc;
	scanf("%d",&Tc);
	for(int i = 1 ; i <= Tc ; i++)	solve(i);
	
}
