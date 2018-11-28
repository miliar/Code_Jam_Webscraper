#include<iostream>
#include<stdio.h>
#include<string.h>
#include <algorithm>
#define FR(i,a,b) for(i=a;i<b;++i)
#define FRS(i,a,b,s) for(i=a;i<b;i+=s)
#define FRE(i,a,b) for(i=a;i<=b;++i)
#define FRES(i,a,b,s) for(i=a;i<=b;i+=s)
// 0->tt-1		FR(i, 0, tt) printf(" 1");
// 0,2,4->tt-1	FRS(i, 0, tt, 2) printf(" 2");
// 0->tt		FRE(i, 0, tt) printf(" 3");
// 0,2,4->tt	FRES(i, 0, tt, 2) printf(" 4");
using namespace std;

// min distance may not be the path
// as a fast horse can lie in a long path
// [cur, horse on hand, time used?, endurance left?], what about endurance more but time used shorter?
// backward? 

int i, j, n, q,k,x,y,z;
int tt;

long long edge[101][101];
long long s[101];
long long energy[101];
long double t[101][101];
	
	int st, en;
void slow(){
		cin >> st >> en;
		long long left[101]; // horse
		long double t[101];
		FR(x,0,101) left[x] = 0;
		FR(x,0,101) t[x] = -10;
		long double used = 0;
		int cur = st;
		t[st] = 0;
		while(cur != en){
			left[cur] = energy[cur];
			FR(x,1,cur+1) {
				left[x] -= edge[cur][cur+1];
				if(t[x] >-1 && left[x] >=0){
					// remain horse
					t[x] += edge[cur][cur+1] / ((long double) s[x]);
					if(t[cur+1] <-1 || t[x] < t[cur+1]) t[cur+1] = t[x];
				}
			}
			cur++;
		}
		printf(" %.8Lf", t[en]);
}

long long d[101][101];
void fastPre(){
	// find pair wise distance
	FR(x,1,n+1) FR(y,1,n+1) d[x][y] = edge[x][y];
	FR(z,1,n+1) FR(x,1,n+1) FR(y,1,n+1) if(d[x][z] >0 && d[z][y] >0 && (d[x][y] <0 || d[x][z] + d[z][y] < d[x][y])) d[x][y] = d[x][z] + d[z][y];
}

//dijkstra
void fast(){
	cin >> st >> en;
	bool used[102];
	FR(x,1,n+1) used[x] = false;
	long double t[102];
	FR(x,1,n+1) t[x] = -10;
	t[st]=0;
	FR(z,1,n+1){
		int minn = en;
		FR(x,1,n+1) if(!used[x] && t[x] > -1 && (t[minn] < -1 || t[minn] > t[x])) minn = x;
		used[minn] = true;
		FR(x,1,n+1) if(d[minn][x] >0 && energy[minn] >= d[minn][x]) {
			long double ttt = d[minn][x] / ((long double) s[minn]);
			if(t[x] < -1 || t[x] > t[minn] + ttt) t[x] = t[minn] + ttt;
		}
	}
	printf(" %.8Lf", t[en]);
}

void run(){
	cin >> n >> q;
	FR(i,1,n+1) cin >> energy[i] >> s[i];
	FR(i,1,n+1) FR(j,1,n+1) cin >> edge[i][j];
	fastPre();
	FR(i,0,q){
//		slow();
		fast();
	}

}

int main(){
	int T;
	scanf("%d", &T);
	for(tt =1; tt<=T; tt++){
		printf("Case #%d:",tt); // standard
		run();
		printf("\n"); // endline
	}
	return 0;
}
