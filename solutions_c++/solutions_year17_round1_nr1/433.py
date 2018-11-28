#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<stack>
#include<cstdio>
#include<cmath>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> P;
typedef pair<int,P> P1;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define rep(i,x) for(int i=0;i<x;i++)
#define rep1(i,x) for(int i=1;i<=x;i++)
#define rrep(i,x) for(int i=x-1;i>=0;i--)
#define rrep1(i,x) for(int i=x;i>0;i--)
#define sor(v) sort(v.begin(),v.end())
#define rev(s) reverse(s.begin(),s.end())
#define lb(vec,a) lower_bound(vec.begin(),vec.end(),a)
#define ub(vec,a) upper_bound(vec.begin(),vec.end(),a)
#define uniq(vec) vec.erase(unique(vec.begin(),vec.end()),vec.end())
#define mp1(a,b,c) P1(a,P(b,c))

const int INF=1000000000;
const int dir_4[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
const int dir_8[8][2]={{1,0},{1,1},{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1}};

int main(){
	int T;
	scanf("%d",&T);
	rep1(ppp,T){
		printf("Case #%d: ",ppp);
		
		int r,c;
		scanf("%d%d",&r,&c);
		int e = -1;
		char a[26][26];
		rep(i,r){
			scanf("\n");
			rep(j,c){
				scanf("%c",&a[i][j]);
				if(a[i][j] != '?')e = i;
			}
		}
		
		for(int i = e ; i >= 0 ; i --){
			for(int j = 0 ; j+1 < c ; j ++){
				if(a[i][j+1] == '?'){
					a[i][j+1] = a[i][j];
				}
			}
			for(int j = c-1 ; j-1 >= 0 ; j --){
				if(a[i][j-1] == '?'){
					a[i][j-1] = a[i][j];
				}
			}
			if(a[i][0] == '?'){
				for(int j = 0 ; j < c ; j ++){
					a[i][j] = a[i+1][j];
				}
			}
		}
		for(int i = e+1 ; i < r ; i ++){
			for(int j = 0 ; j < c ; j ++){
				a[i][j] = a[i-1][j];
			}
		}
		
		printf("\n");
		for(int i = 0 ; i < r ; i ++){
			for(int j = 0 ; j < c ; j ++){
				printf("%c",a[i][j]);
			}
			printf("\n");
		}
	}
}

