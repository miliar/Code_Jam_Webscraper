#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <utility>
#include <complex>
#include <functional>
#include <bitset>
#include <time.h>
#include <assert.h>
#define ff first
#define ss second
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
template <class T> inline void umin(T &a,T b){a=min(a,b);}
template <class T> inline void umax(T &a,T b){a=max(a,b);}
const int INF=0x3f3f3f3f;
LL mod=1e9+7;
const int N=55;

struct Node{
	int x,h1,h2,a,b,f;
};
int main() {
#ifndef ONLINE_JUDGE
	//freopen("in.txt","r",stdin);
	freopen("C-small-attempt2.in","r",stdin);
	
	freopen("out1003.txt","w",stdout);
#endif
	int _;scanf("%d",&_);
	for(int cas=1;cas<=_;cas++){
		printf("Case #%d: ",cas);
		int h1,a,h2,b,c,d;
		cin>>h1>>a>>h2>>b>>c>>d;
		
		queue<Node> q;
		q.push({0,h1,h2,a,b,0});
		int ok=0;
		while(!q.empty()){
			int x=q.front().x;
			int t1=q.front().h1;
			int t2=q.front().h2;
			int g1=q.front().a;
			int g2=q.front().b;
			int f=q.front().f;
			q.pop(); 
			if(x>1000||t1<=0)break;
			if(t2<=0){
				ok=1;
				printf("%d\n",x);
				break;
			}
			if(t2-g1<=0){
				ok=1;
				printf("%d\n",x+1);
				break;
			}
			if(t1-g2<=0){
				if(h1-g2-g2<=0);
				else
				q.push({x+1,h1-g2,t2,g1,g2,f});
			}else{
				if(f==0){
					if(c!=0)
					q.push({x+1,t1-g2,t2,g1+c,g2,0});
					if(d!=0)
					q.push({x+1,t1-g2,t2,g1,max(0,g2-d),0});
				}
				q.push({x+1,t1-g2,t2-g1,g1,g2,1});
			}
			
		}
		if(ok==0)puts("IMPOSSIBLE");
	
	}
	return 0;
}









