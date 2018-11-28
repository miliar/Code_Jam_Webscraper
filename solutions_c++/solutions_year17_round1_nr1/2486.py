#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define INF INT_MAX/2
#define PI 3.14159265358979323846264338327950
#define reset(a,x) memset(a,x,sizeof(a))

#define ll long long
#define ull unsigned long long
#define ii pair<int,int>
#define vi vector<int> 
#define vii vector<ii>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define all(c) (c).begin,(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define rep(a,b,c)   for(int (a)=(b); (a)<(c); (a)++)
#define repn(a,b,c)  for(int (a)=(b); (a)<=(c); (a)++)
#define repd(a,b,c)  for(int (a)=(b); (a)>=(c); (a)--)

int moves[8][2]={{-1,0},{1,0},{0,1},{0,-1},{1,1},{-1,-1},{-1,1},{1,-1}};
bool issafe(int i,int j){
    return (i>=0 && i<8 && j>=0 && j<8);
}


char grid[25][25];

bool isRowEmpty(int row,int r,int c){
	for(int i=0;i<c;i++){
		if(grid[row][i]!='?')
			return false;
	}
	return true;
}

int main(){
	int t,r,c;
	cin>>t;
	repn(test,1,t){
		cin>>r>>c;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cin>>grid[i][j];
			}
		}

		bool pRowEmpty=true;
		for(int i=0;i<r;i++){
			if(isRowEmpty(i,r,c)){
				if(!pRowEmpty){
					for(int j=0;j<c;j++)
						grid[i][j]=grid[i-1][j];
				}
				continue;
			}
			pRowEmpty=false;
			char pChar=grid[i][0];
			for(int j=1;j<c;j++){
				if(grid[i][j]=='?')
					grid[i][j]=pChar;
				else
					pChar=grid[i][j];
			}

		}

		for(int i=r-1;i>=0;i--){
			if(isRowEmpty(i,r,c)){
				for(int j=0;j<c;j++)
					grid[i][j]=grid[i+1][j];
				continue;
			}
			char pChar=grid[i][c-1];
			for(int j=c-2;j>=0;j--){
				if(grid[i][j]=='?')
					grid[i][j]=pChar;
				else
					pChar=grid[i][j];
			}
		}

		printf("Case #%d: \n",test);
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout<<grid[i][j];
			}
			cout<<endl;
		}
	}

	return 0;
}

