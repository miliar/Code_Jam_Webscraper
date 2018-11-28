#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>
#include <queue>
#include <map>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FORE(i,a,b) for(int i=a;i<=b;i++)
#define SCF(a) scanf("%d",&a)
#define SCFU(a) scanf("%lld",&a)
#define SCF2(a,b) scanf("%d%d",&a,&b)
#define SCF3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define min2(a,b) ((a)<(b))?(a):(b)
#define max2(a,b) ((a)>(b))?(a):(b)
#define MST(a,b) memset(a,b,sizeof(a))
const int INF = 0x3FFFFFFF;
const int N = 2000+5;

typedef long long int LL;

typedef struct{	int id,val;} QDE;
bool operator < (const QDE& a, const QDE& b) {  
	return a.val < b.val;
}
char mat[30][30];
//------------------------------------------------------------
int main(){
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int r,c,T;
	SCF(T);
	FOR(cse,0,T){
		SCF2(r,c);
		FOR(i,0,r)
			scanf("%s", mat[i]);
		FOR(i,0,r)
			FOR(j,0,c)
			if( mat[i][j]!='?' ){
				for(int q=j-1;q>=0;q--)
					if(mat[i][q]=='?')
						mat[i][q] = mat[i][j];
					else break;
				for(int q=j+1;q<c;q++)
					if(mat[i][q]=='?')
						mat[i][q] = mat[i][j];
					else break;
			}
		FOR(i,0,r)
		if( mat[i][0]!='?' ){
			for(int q=i-1;q>=0;q--)
				if(mat[q][0]=='?')
					FOR(j,0,c) mat[q][j] = mat[i][j];
				else break;
			for(int q=i+1;q<r;q++)
				if(mat[q][0]=='?')
					FOR(j,0,c) mat[q][j] = mat[i][j];
				else break;
		}
		printf("Case #%d:\n",cse+1);
		FOR(i,0,r)
			printf("%s\n",mat[i]);
	}
	return 0;
}
/*
3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
*/
