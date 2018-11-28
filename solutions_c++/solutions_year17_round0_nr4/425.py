#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl "\n"

using namespace std;

typedef long long ll;
typedef long double ld;

int n, m;

int lin[102], col[102];
int t[102][102], t1[102][102], tf[102][102];
void build(int n){
	memset(t1, 0, sizeof(t1));
	for (int i = 1; i < n - 1; i++){
		//t1[0][i] = 1;
		//t1[n - 1][i] = 1;
		t1[i][0] = 1;
		t1[i][n - 1] = 1;
	}
}
void elimina(int c, int a, int b){
	if (t1[a][b] & c) return;
	//cout << 1231 << endl;
	if ((c & 1) && b != 0 && b != n - 1){
		if (a == 0 || a == n - 1){
			if (t1[b][a] && t1[n - 1 - b][n - 1 - a]){
				t1[n - 1 - a][n - 1 - b] = 1;
			}
		}
        for (int i = 1; a + i < n && b + i < n; i++){
            t1[a + i][b + i] = 0;
        }
        for (int i = 1; a - i >= 0 && b - i >= 0; i++){
            t1[a - i][b - i] = 0;
        }
        for (int i = 1; a + i < n && b - i >= 0; i++){
            t1[a + i][b - i] = 0;
        }
        for (int i = 1; a - i >= 0 && b + i < n; i++){
            t1[a - i][b + i] = 0;
        }
	}
}
int main(){
	ios::sync_with_stdio(false);
	freopen("din", "r", stdin);
    freopen("dout", "w", stdout);
	int te;
	cin >> te;
	int caso = 1;
	while (te--){
		memset(t, 0, sizeof(t));
		memset(t1, 0, sizeof(t1));
		memset(tf, 0, sizeof(tf));
		memset(lin, 0, sizeof(lin));
		memset(col, 0, sizeof(col));
		cin >> n >> m;

		build(n);
		for (int i = 0; i < m; i++){
			char c;
			int a, b;
			cin >> c >> a >> b;
			a--;
			b--;
			if (c == 'o') c = 3;
			else if (c == 'x') c = 2;
			else c = 1;

			t[a][b] = c;
			col[b] |= (c & 2);
			lin[a] |= (c & 2);
			elimina((int)c, a, b);
		}

		int qtd = 0, mov = 0;
		for (int i = 0; i < n; i++){
			if (lin[i]) continue;
			for (int j = 0; j < n; j++){
				if (lin[i]) break;
				if (col[j]) continue;
				//cout << col[j] << endl;
				//cout << i << " " << j << endl;
				col[j] = 2;
				lin[i] = 2;
				t1[i][j] |= 2;
				//cout << col[j] << endl;
			}
		}
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				tf[i][j] = t1[i][j] | t[i][j];
			}
		}
		bool da = true;
		for (int i = 0; i < n; i++){
			if (tf[i][i] & 1){
				da = false;
				break;
			}
		}
		if (da) tf[0][0] |= 1;

		da = true;
		for (int i = 0; i < n; i++){
			if (tf[i][n - 1 - i] & 1){
				da = false;
				break;
			}
		}

		if (da) tf[0][n - 1] |= 1;

		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				if (tf[i][j] != t[i][j]){
					mov++;
				}
				qtd += (tf[i][j] + 1) / 2;
			}
		}
		cout << "Case #" << caso << ": ";
		cout << qtd << " " << mov << endl;
 		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				if (tf[i][j] != t[i][j]){
					char c;
					if (tf[i][j] == 3) c = 'o';
					if (tf[i][j] == 2) c = 'x';
					if (tf[i][j] == 1) c = '+';
					cout << c << " " << i + 1 << " " << j + 1 << endl;
				}
			}
		}
		/*
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				cout << tf[i][j] << " ";
			}cout << endl;
		}
		*/
		caso++;
	}
	return 0;
}


