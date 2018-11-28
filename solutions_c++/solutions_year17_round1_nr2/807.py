#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <functional>
#include <math.h> 

using namespace std;

const int maxn = 100;
int low[maxn][maxn], high[maxn][maxn];
int b[maxn], c[maxn];
int T, n, m;
			
int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin>>T;
	for (int tt = 0; tt < T; tt++) {
		cin>>n>>m;
		for (int i = 0; i < n; i++)
			cin>>c[i];
		for (int i = 0; i < n; i++) {
			vector<int> a;
			for (int j = 0; j < m; j++) {
				int k;
				cin>>k;
				a.push_back(k);
			}
			sort(a.begin(), a.end());
			for (int j = 0; j < m; j++) {
				int k = a[j];
				low[i][j] = (int)ceil(k/1.1/c[i]);
				high[i][j] = (int)floor(k/0.9/c[i]);
			}
		}
		int ans = 0;
		for (int i = 0; i < n; i++)
			b[i] = 0;
		bool flag = true;
		while (flag) {
			int k = 0;
			for (int i = 1; i < n; i++) 
				if (high[i][b[i]]<high[k][b[k]])
					k = i;
			int l = 0;
			for (int i = 1; i < n; i++)
				if (low[i][b[i]]>low[l][b[l]])
					l = i;
			if (high[k][b[k]]<low[l][b[l]]) {
				b[k] += 1;
				if (b[k]==m)
					break;
				continue;
			}
			ans += 1;
			for (int i = 0; i < n; i++) {
				b[i] += 1;
				if (b[i]==m) 
					{flag = false; break;}
			}
		}
	
		cout<<"Case #"<<tt+1<<": "<<ans<<endl;
	}
	return 0;
}
