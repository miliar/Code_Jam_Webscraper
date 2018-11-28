#include <cstdio>
#include <iostream>
#include <cstring>
#include <map>
#include <cstdlib>

using namespace std;

typedef long long LL;

string testfile = "D-large";

const int MAXN = 100+5;

char d[MAXN][MAXN];
char ans[MAXN][MAXN];

bool fixed_px[MAXN*2];
bool fixed_py[MAXN*2];
int lp[MAXN*2];
bool usdp[MAXN*2];

bool fixed_xx[MAXN];
bool fixed_xy[MAXN];
int lx[MAXN];
bool usdx[MAXN];

bool gp[MAXN*2][MAXN*2];

int N,M;

void comb(char &x,char y) {
	if (x=='.') x = y;
	else if (x!=y) x = 'o';
}

bool hungry_p(int x) {
	for (int i = 1; i<=2*N-1; ++i)
		if (!fixed_py[i]) {
			if (!usdp[i] && gp[x][i]) {
				usdp[i] = 1;
				if (lp[i]==-1 || hungry_p(lp[i])) {
					lp[i] = x;
					return true;
				}
			}
		}
	return false;
}

bool hungry_x(int x) {
	for (int i = 1; i<=N; ++i)
		if (!fixed_xy[i]) {
			if (!usdx[i]) {
				usdx[i] = 1;
				if (lx[i]==-1 || hungry_x(lx[i])) {
					lx[i] = x;
					return true;
				}
			}
		}
	return false;
}

void run() {
	cin>>N>>M;

	memset(d,'.',sizeof(d));
	memset(fixed_px,0,sizeof(fixed_px));
	memset(fixed_py,0,sizeof(fixed_py));
	memset(fixed_xx,0,sizeof(fixed_xx));
	memset(fixed_xy,0,sizeof(fixed_xy));
	memset(lp,-1,sizeof(lp));
	memset(lx,-1,sizeof(lx));

	memset(gp,0,sizeof(gp));

	for (int i = 0; i<M; ++i) {
		char ch;
		int x,y;
		cin>>ch>>x>>y;
		d[x][y] = ch;

		if (ch=='o') {
			fixed_xx[x] = 1;
			fixed_xy[y] = 1;
			lx[y] = x;
			fixed_px[x+y-1] = 1;
			fixed_py[x-y+N] = 1;
			lp[x-y+N] = x+y-1;
		}
		else if (ch=='x') {
			fixed_xx[x] = 1;
			fixed_xy[y] = 1;
			lx[y] = x;
		}
		else if (ch=='+') {
			fixed_px[x+y-1] = 1;
			fixed_py[x-y+N] = 1;
			lp[x-y+N] = x+y-1;
		}

	}

	for (int i = 1; i<=N; ++i)
		for (int j = 1; j<=N; ++j) {
			gp[i+j-1][i-j+N] = 1;
		}

	int countp = 0;
	for (int i = 1; i<=2*N-1; ++i) if (!fixed_px[i]) {
		memset(usdp,0,sizeof(usdp));
		if (hungry_p(i)) ++countp;
	}

	int countx = 0;
	for (int i = 1; i<=N; ++i) if (!fixed_xx[i]) {
		memset(usdx,0,sizeof(usdx));
		if (hungry_x(i)) ++countx;
	}

	memset(ans,'.',sizeof(ans));
	for (int i = 1; i<=N; ++i) if (lx[i]!=-1) {
		//cout<<lx[i]<<' ';
		comb(ans[lx[i]][i],'x');
	}
	for (int i = 1; i<=2*N-1; ++i) if (lp[i]!=-1) {
		int x = (lp[i]+i+1-N)/2;
		int y = x-i+N;
		//cout<<lp[i]<<' ';
		comb(ans[x][y],'+');
	}

//	cout<<endl;
//	for (int i = 1; i<=N; ++i) {
//		for (int j = 1; j<=N; ++j) {
//			cout<<ans[i][j];
//		}
//		cout<<endl;
//	}

	int total = 0,diff = 0;
	for (int i = 1; i<=N; ++i) {
		for (int j = 1; j<=N; ++j) {
			if (ans[i][j]=='+') ++total;
			else if (ans[i][j]=='x') ++total;
			else if (ans[i][j]=='o') total += 2;
			if (ans[i][j]!=d[i][j]) ++diff;
		}
	}

	cout<<total<<' '<<diff<<endl;
	for (int i = 1; i<=N; ++i) {
		for (int j = 1; j<=N; ++j) {
			if (ans[i][j]!=d[i][j]) {
				cout<<ans[i][j]<<' '<<i<<' '<<j<<endl;
			}
		}
	}
}

int main() {
	freopen((testfile+".in").c_str(),"r",stdin);
	freopen((testfile+".out").c_str(),"w",stdout);
	int testn;
	cin>>testn;
	for (int loop = 1; loop<=testn; ++loop) {
		cout<<"Case #"<<loop<<": ";

		run();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
