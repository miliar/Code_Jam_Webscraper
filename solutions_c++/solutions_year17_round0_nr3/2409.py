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
const int N=30;
char s[N];
int main() {
#ifndef ONLINE_JUDGE
	//freopen("in.txt","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("1003.out","w",stdout);
#endif
	int _;scanf("%d",&_);
	for(int cas=1;cas<=_;cas++){
		printf("Case #%d: ",cas);
		LL n,m;
		cin>>n>>m;
		LL ans1,ans2;
		LL ct=1,sum=0,x=0,y=n;
		
		for(int i=1;;i++){
			sum+=ct;
			if(sum>=m){
				sum-=ct;
				LL sb=m-sum;
				if(sb<=x){
					y++;
				}
				
				if(y%2) 
					cout<<y/2<<" "<<y/2<<endl;
				else
					cout<<y/2<<" "<<y/2-1<<endl;
				break;
			}
			n=n-ct;	
			y=n/(ct*2);//长度为y和y+1 
			x=n%(ct*2);//y+1的 个数 
			
			ct=ct*2;
		}
		
		
	}
	return 0;
}









