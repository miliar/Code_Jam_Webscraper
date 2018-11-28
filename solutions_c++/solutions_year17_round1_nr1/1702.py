#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int n,m;
char s[27][27];
char ans[27][27];

void flood(int x,int y) {
	ans[x][y] = s[x][y];
	int yst = y, ynd = y;
	for (int j=y+1;j<m;j++) {
		if (s[x][j]=='?' && ans[x][j]=='?') {
			ans[x][j] = s[x][y];
			ynd = j;
		}
		else 
			break;
	}
	for (int j=y-1;j>=0;j--) {
		if (s[x][j]=='?' && ans[x][j]=='?') {
			ans[x][j] = s[x][y];
			yst = j;
		}
		else 
			break;
	}
	//cerr<<x<<","<<y<<" : "<<yst<<","<<ynd<<endl;
	bool flag;
	for (int i=x+1;i<n;i++) {
		flag = 1;
		for (int j=yst;j<=ynd;j++) {
			if (s[i][j]!='?' || ans[i][j]!='?') {
				flag = 0;
				break;
			}
		}
		if (flag) {
			for (int j=yst;j<=ynd;j++) {
				ans[i][j] = s[x][y];
			}
		}
		else break;
	}
	for (int i=x-1;i>=0;i--) {
		flag = 1;
		for (int j=yst;j<=ynd;j++) {
			if (s[i][j]!='?' || ans[i][j]!='?') {
				flag = 0;
				break;
			}
		}
		if (flag) {
			for (int j=yst;j<=ynd;j++) {
				ans[i][j] = s[x][y];
			}
		}
		else break;
	}
}

void solve() {
	scanf("%d%d",&n,&m);
	for (int i=0;i<n;i++) {
		getchar();
		for (int j=0;j<m;j++) {
			s[i][j] = getchar();
			ans[i][j] = s[i][j];
		}
	}
	for (int i=0;i<n;i++) {
		for (int j=0;j<m;j++) {
			if (s[i][j]!='?') {
				flood(i,j);
			}
		}
	}
	printf("\n");
	for (int i=0;i<n;i++) {
		for (int j=0;j<m;j++) {
			printf("%c",ans[i][j]);
		}
		printf("\n");
	}
}

int main() {
	int tt;
	cin>>tt;
	for (int cs=1;cs<=tt;cs++){
		printf("Case #%d: ",cs);
		solve();
	}

	return 0;
}