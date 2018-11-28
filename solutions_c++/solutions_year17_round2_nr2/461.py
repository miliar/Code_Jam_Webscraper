#include <iostream>
#include <iomanip>
#include <climits>
#include <stack>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

#define maxn 1000

using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;

char w[maxn+10];

void solve(int prim){
	int n,r,o,y,g,b,v;
	scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
	/*if(o>b+1 && v>y+1 && r>g+1){
		printf("Case #%d: IMPOSSIBLE\n",prim);
		return;
	}
	if(o==b+1 && n!=o+b+1){
		printf("Case #%d: IMPOSSIBLE\n",prim);
		return;
	}
	if(v==y+1 && n!=o+b+1){
		printf("Case #%d: IMPOSSIBLE\n",prim);
		return;
	}
	if(g==r+1 && n!=o+b+1){
		printf("Case #%d: IMPOSSIBLE\n",prim);
		return;
	}
	int cnt=0;
	if(*/
	int cnt=1;
	if(r>=y && r>=b){w[0]='R';r--;}
	else if(y>=r && y>=b){w[0]='Y';y--;}
	else {w[0]='B';b--;}
	while(r>0 || b>0 || y>0){
	//	printf("r:%d b:%d y:%d\n",r,b,y);
		if(w[cnt-1]=='R'){
			if(b+y==0){
				printf("Case #%d: IMPOSSIBLE\n",prim);
				return;
			}
			if(b>y || b==y && w[0]=='B'){
				w[cnt++]='B';
				b--;
			}
			else{
				y--;
				w[cnt++]='Y';
			}
			continue;
		}
		if(w[cnt-1]=='B'){
			if(r+y==0){
				printf("Case #%d: IMPOSSIBLE\n",prim);
				return;
			}
			if(r>y || r==y && w[0]=='R'){
				w[cnt++]='R';
				r--;
			}
			else{
				y--;
				w[cnt++]='Y';
			}
			continue;
		}
		if(w[cnt-1]=='Y'){
			if(r+b==0){
				printf("Case #%d: IMPOSSIBLE\n",prim);
				return;
			}
			if(b>r || b==r&&w[0]=='B'){
				b--;
				w[cnt++]='B';
			}
			else{
				w[cnt++]='R';
				r--;
			}
			continue;
		}
	}
	if(w[0]==w[cnt-1]){
		printf("Case #%d: IMPOSSIBLE\n",prim);
		return;
	}
	w[cnt]='\0';
	printf("Case #%d: %s\n",prim,w);
}

int main(){
	int n;
	scanf("%d",&n);
	FORR(i,1,n+1)solve(i);
	return 0;
}
