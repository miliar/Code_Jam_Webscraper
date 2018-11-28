#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

#define pb push_back
#define rc(x) scanf("%c\n",&x)
#define ri(x) scanf("%d\n",&x)
#define rii(x,y) ri(x),ri(y)
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define ms2(obj,val,sz) memset(obj,val,sizeof(obj[0])*sz)
#define FOR(i,f,t) for(int i=f;i<(int)t;i++)
#define FORR(i,f,t) for(int i=f;i>(int)t;i--)

typedef long long ll;
typedef vector<int> vi;

const int MAXN=30;

bool letter[MAXN];
int T,R,C;
char A[MAXN][MAXN];

int main() {
	ri(T);
	FOR(t,1,T+1) {
		rii(R,C);
		ms(letter,false);
		FOR(r,0,R) FOR(c,0,C) rc(A[r][c]);
		FOR(r,0,R) {
			FOR(c,0,C) if(A[r][c]!='?') letter[r]=true;
			if(!letter[r]) continue;
			int idx=0;
			while(idx<C && A[r][idx]=='?') idx++;
			FOR(c,0,idx) A[r][c]=A[r][idx];
			int col=idx+1;
			while(col<C) {
				if(A[r][col]=='?') A[r][col]=A[r][idx];
				else idx=col;
				col++;
			}
		}
		FOR(r,0,R) if(letter[r]) {
			int rr=r-1;
			while(rr>=0 && !letter[rr]) {
				FOR(c,0,C) A[rr][c]=A[r][c];
				letter[rr]=true;
				rr--;
			}
			rr=r+1;
			while(rr<R && !letter[rr]) {
				FOR(c,0,C) A[rr][c]=A[r][c];
				letter[rr]=true;
				rr++;
			}
		}
		printf("Case #%d:\n",t);
		FOR(r,0,R) {
			FOR(c,0,C) printf("%c",A[r][c]);
			printf("\n");
		}
	}
}
