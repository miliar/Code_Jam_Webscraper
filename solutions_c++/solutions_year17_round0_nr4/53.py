#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
using namespace std;

#define LL long long

char S[200][200], T[200][200];
int A[200][200], B[200][200];
bool mask_c[300], mask_r[300];

const int MaxN = 300;
vector<int> adj[MaxN];
int match[MaxN], vis[MaxN];
int K;

int find(int u) {
	for(int i=0;i<adj[u].size();++i) {
		int v = adj[u][i];
		if(!vis[v]) {
			vis[v] = true;
			if (match[v] < 0 || find(match[v]))  {
				match[v]=u;
				return true;
			}
		}
	}
	return false;
}

void run() {
	int N,M,res=0,add=0;
	cin >> N >> M;
	for(int i=0;i<N;++i)
		for(int j=0;j<N;++j) S[i][j]=T[i][j]='.';
	for(int i=0;i<M;++i) {
		string c;
		int x,y;
		cin >> c >> x >> y;
		S[--x][--y] = c[0];
		if (c[0] == 'o') res += 2;
		else res += 1;
	}
	// check x
	for(int i=0;i<N;++i)
		mask_r[i]=mask_c[i]=true;
	for(int i=0;i<N;++i)
		for(int j=0;j<N;++j) {
			A[i][j] = 0;
			if (S[i][j] == 'o' || S[i][j] == 'x') {
				mask_r[i]=false;
				mask_c[j]=false;
			}
		}
	for(int i=0;i<N;++i)
		if (mask_r[i])
			for(int j=0;j<N;++j)
				if (mask_c[j]) {
					res ++;
					add ++;
					A[i][j] = 1;
					mask_r[i] = false;
					mask_c[j] = false;
					break;
				}
	// check +, diag
	memset(mask_r,0,sizeof(mask_r));
	memset(mask_c,0,sizeof(mask_c));
	for(int i=0;i<N;++i)
		for(int j=0;j<N;++j) {
			B[i][j] = 0;
			if (S[i][j] == 'o' || S[i][j] == '+') {
				mask_r[i+j] = true;
				mask_c[i-j+N] = true;
			}
		}
	int K = N + N;
	for(int i=0;i<K;++i) {
		adj[i].clear();
		match[i] = -1;
	}
	for(int i=0;i<N;++i)
		for(int j=0;j<N;++j) {
			if (S[i][j] == '.' || S[i][j] == 'x')
				if (!mask_r[i+j] && !mask_c[i-j+N]) {
					adj[i+j].push_back(i-j+N);
				}
		}
	for(int i=0;i<K;++i) {
		memset(vis,0,sizeof(vis));
		find(i);
	}
	for(int i=0;i<K;++i) {
		if(match[i] > -1) {
			int a = match[i];  // a = x + y
			int b = i - N;  // b = x - y
			int x = a + b >> 1;
			int y = a - b >> 1;
			B[x][y] ++;
			res ++;
			if (!A[x][y])
				add ++;
		}
	}
	printf("%d %d\n", res, add);
	for(int i=0;i<N;++i)
		for(int j=0;j<N;++j)
			if(A[i][j]) {
				char c;
				if(B[i][j] || S[i][j] != '.') {
					c = 'o';
					B[i][j] = 0;
				} else c = 'x';
				cout << c << " " << i+1 << " " << j+1 << endl;
			}
	for(int i=0;i<N;++i)
		for(int j=0;j<N;++j)
			if(B[i][j]) {
				char c;
				if (S[i][j] != '.')
					c = 'o';
				else
					c = '+';
				cout << c << " " << i+1<<" "<<j+1<<endl;
			}
	
}

int main() {
	freopen("D-large.in","r",stdin);
	freopen("D.out","w",stdout);
	int T;
	cin >>T;
	for (int i=1;i<=T;++i) {
		printf("Case #%d: ", i);
		run();
	}
}
