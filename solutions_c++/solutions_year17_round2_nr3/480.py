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

int n;
pii horse[maxn+10];
int m[maxn+10][maxn+10];
double res[maxn+10][maxn+10];
ll energ[maxn+10][maxn+10];
bool obiskano[maxn+10][maxn+10];

void dijk(int start, int cilj){
	FOR(i,maxn+2)FOR(j,maxn+2){res[i][j]=-1;energ[i][j]=-1;obiskano[i][j]=0;}//-1 neobiskano
	res[start][start]=0;
	energ[start][start]=horse[start].fs;
	while(1){
		/*printf("\n\n");
		FOR(i,n){FOR(j,n)printf("%.2lf ",res[i][j]);printf("\n");}*/
		pii mini=mp(0,0);
		FOR(i,n)FOR(j,n){
			if(res[i][j]<0)continue;
			if(obiskano[i][j])continue;
			if(res[mini.fs][mini.sec]<0 || obiskano[mini.fs][mini.sec]){
				mini=mp(i,j);
				continue;
			}
			if(res[mini.fs][mini.sec]>res[i][j]){
				mini=mp(i,j);
				continue;
			}
		}
		if(mini.fs==cilj){
			printf(" %.12lf",res[mini.fs][mini.sec]);
			return;
		}
		obiskano[mini.fs][mini.sec]=1;
		//printf("Mini: %d,%d\n",mini.fs,mini.sec);
		FOR(i,n){//isti konj
			if(m[mini.fs][i]==-1)continue;
			if(m[mini.fs][i]>energ[mini.fs][mini.sec])continue;
			double cas = res[mini.fs][mini.sec]+(double)m[mini.fs][i]/(double)horse[mini.sec].sec;
			if(res[i][mini.sec]==-1 || res[i][mini.sec]>cas){
				res[i][mini.sec]=cas;
				energ[i][mini.sec]=energ[mini.fs][mini.sec]-m[mini.fs][i];
			}
		}
		if(res[mini.fs][mini.fs]==-1 || res[mini.fs][mini.fs]>res[mini.fs][mini.sec]){
			res[mini.fs][mini.fs]=res[mini.fs][mini.sec];
			energ[mini.fs][mini.fs]=horse[mini.fs].fs;
		}
	}
}

void solve(int prim){
	int q;
	scanf("%d%d",&n,&q);
	FOR(i,n)scanf("%d%d",&horse[i].fs,&horse[i].sec);
	FOR(i,n)FOR(j,n)scanf("%d",&m[i][j]);
	printf("Case #%d: ",prim);
	FOR(i,q){
		int a,b;
		scanf("%d%d",&a,&b);
		dijk(a-1,b-1);
	}
	printf("\n");
}

int main(){
	int n;
	scanf("%d",&n);
	FORR(i,1,n+1)solve(i);
	return 0;
}
