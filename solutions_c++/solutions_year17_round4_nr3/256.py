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
		char a[52][52];
		rep(i,52)rep(j,52)a[i][j] = '#';
		scanf("%d%d",&r,&c);
		rep1(i,r){
			scanf("\n");
			rep1(j,c){
				scanf("%c",&a[i][j]);
			}
		}
		
		int x[52][52],y[52][52];
		int X = 0,Y = 0;
		rep1(i,r)rep1(j,c){
			if(a[i][j] == '#')continue;
			if(a[i][j-1] == '#')X ++;
			x[i][j] = X;
		}
		rep1(j,c)rep1(i,r){
			if(a[i][j] == '#')continue;
			if(a[i-1][j] == '#')Y ++;
			y[i][j] = Y;
		}
		
		int cnt_X[260] = {},cnt_Y[260] = {};
		rep1(i,r)rep1(j,c){
			if(a[i][j] == '#')continue;
			if(a[i][j] != '.'){
				cnt_X[x[i][j]] ++;
				cnt_Y[y[i][j]] ++;
			}
		}
		
		char ans[52][52];
		rep1(i,r)rep1(j,c){
			if(a[i][j] == '#' || a[i][j] == '.')ans[i][j] = a[i][j];
			else ans[i][j] = '?';
		}
		
		char ans_X[260],ans_Y[260];
		rep(i,260){
			ans_X[i] = '?';
			ans_Y[i] = '?';
		}
		
		rep1(i,X){
			if(cnt_X[i] != 1)ans_X[i] = '|';
		}
		rep1(i,Y){
			if(cnt_Y[i] != 1)ans_Y[i] = '-';
		}
		
		bool update = true;
		bool hoge = true;
		bool ret = true;
		while(update){
			update = false;
			rep1(i,r){
				rep1(j,c){
					if(ans_X[x[i][j]] != '?'){
						if(ans_Y[y[i][j]] == '?'){
							ans_Y[y[i][j]] = ans_X[x[i][j]];
							update = true;
						}
						else if(ans_Y[y[i][j]] != ans_X[x[i][j]]){
							ret = false;
							break;
						}
					}
					if(ans_Y[y[i][j]] != '?'){
						if(ans_X[x[i][j]] == '?'){
							ans_X[x[i][j]] = ans_Y[y[i][j]];
							update = true;
						}
					}
					/*if(ans_X[x[i][j]] == '|'){
						if(ans_Y[y[i][j]] == '-'){
							ret = false;
							break;
						}
						if(ans_Y[y[i][j]] == '?'){
							ans_Y[y[i][j]] = '|';
							update = true;
						}
					}
					if(ans_Y[y[i][j]] == '-'){
						if(ans_X[x[i][j]] == '?'){
							ans_X[x[i][j]] = '-';
							update = true;
						}
					}*/
				}
			}
			if(!update){
				update = hoge;
				hoge = false;
			}
		}
		
		rep1(i,r)rep1(j,c){
			if(ans[i][j] != '?')continue;
			ans[i][j] = ans_X[x[i][j]];
			if(ans[i][j] == '?')ans[i][j] = '-';
		}
		
		if(ret){
			puts("POSSIBLE");
			rep1(i,r){
				rep1(j,c){
					printf("%c",ans[i][j]);
				}
				printf("\n");
			}
		}
		else puts("IMPOSSIBLE");
	}
}

