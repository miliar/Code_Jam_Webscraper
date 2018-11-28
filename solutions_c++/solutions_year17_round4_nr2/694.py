#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
pair<int, int> pii;

#define F first
#define S second

const int MAXN = 1e3 + 10;

int n, k, m, c[MAXN];
vector<int> vec[MAXN];

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int te;	cin >> te;
	for (int w = 1; w <= te; w++){
		cin >> n >> k >> m;
		for (int i = 0; i < n; i++) vec[i].clear();
		memset(c, 0, sizeof(c));
		while (m--){
			int a, b;	cin >> a >> b, a--, b--;
			vec[a].push_back(b);
			c[b]++;
		}

		int x = 0;
		for (int i = 0; i < k; i++) x = max(x, c[i]);
		
		int cur = 0;
		for (int i = 0; i < n; i++){
			cur += vec[i].size();
			x = max(x, (cur+i)/(i+1));
		}

		int y = 0;
		for (int i = 0; i < n; i++)
			y = max(y, (int)vec[i].size() - x);
		cout << "Case #" << w << ": " << x << " " << y << "\n";
	}
	return 0;
}
