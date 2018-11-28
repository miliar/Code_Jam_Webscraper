#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

const int maxn = 25;
char a[maxn][maxn];
bool b[maxn];
int T, n, m;

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin>>T;
	for (int tt = 0; tt < T; tt++) {
		cin>>n>>m;
		int first = -1;
		for (int i = 0; i < n; i++) {
			string st;
			cin>>st;
			char ch = '?';
			for (int j = 0; j < m; j++) 
				if (st[j]!='?' && ch=='?')
					ch = st[j];
			if (ch!='?') {
				for (int j = 0; j < m; j++) {
					if (st[j]!='?')
						ch = st[j];
					a[i][j] = ch;
				}
				b[i] = true;
				if (first==-1)
					first = i;
			}
			else
				b[i] = false;
		}
		for (int i = 0; i < first; i++)
			for (int j = 0; j < m; j++)
				a[i][j] = a[first][j];
		for (int i = first; i < n; i++)
			if (!b[i]) {
				for (int j = 0; j < m; j++)
					a[i][j] = a[i-1][j];
			}
		cout<<"Case #"<<tt+1<<":"<<endl;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++)
				cout<<a[i][j];
			cout<<endl;
		}
	}
	return 0;
}