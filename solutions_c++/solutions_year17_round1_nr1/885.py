#include<bits/stdc++.h>
#define LIM 33

using namespace std;

vector < int > index[LIM] , cur[LIM] , row;
int r , c;
char s[LIM][LIM];

void solve(int Tc){
	scanf("%d %d",&r,&c);	
	for(int i = 0 ; i < r ; i++)
		scanf("%s",s[i]);
	for(int i = 0 ; i < r ; i++){
		cur[i].clear();
		index[i].clear();
	}
	for(int i = 0 ; i < r ; i++)
		for(int j = 0 ; j < c ; j++){
			if(s[i][j] == '?')	continue;
			index[i].push_back(j);
			cur[i].push_back(s[i][j] - 'A');
		}
	row.clear();
	for(int i = 0 ; i < r ; i++)	if(index[i].size() > 0)	row.push_back(i);
	for(int i = 0 ; i < row.size() ; i++){
		int r1 = (i == 0 ? 0 : row[i - 1] + 1);
		int r2 = (i == row.size() - 1 ? r - 1 : row[i]);
		int cc = row[i];	
		for(int j = 0 ; j < index[cc].size() ; j++){
			int c1 = (j == 0 ? 0 : index[cc][j - 1] + 1);
			int c2 = (j == index[cc].size() - 1 ? c - 1 : index[cc][j]);
			for(int i1 = r1 ; i1 <= r2 ; i1++)
				for(int i2 = c1 ; i2 <= c2 ; i2++)	s[i1][i2] = (cur[cc][j] + 'A');
		}
	}
	printf("Case #%d:\n",Tc);
	for(int i = 0 ; i < r ; i++)	puts(s[i]);
}

int main(){
	freopen("test.inp","r",stdin);
	freopen("test.out","w",stdout);
	int Test;
	scanf("%d",&Test);
	for(int i = 1 ; i <= Test; i++)	solve(i);
}

