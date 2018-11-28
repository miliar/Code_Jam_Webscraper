#include <iostream>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

int getl(int a, int b){
	b *= 1.1;
	int tt = a / b;
	int ttt = tt * b;
	if (ttt < a) return tt + 1;
	else return tt;
}

int geth(int a, int b){
	b *= 0.9;
	return a / b;
}

int main(){
	int T;
	cin >> T;
	for (int K = 1; K <= T; K++){
		int a, b;
		cin >> a >> b;
		int q[60], p[60][60];
		for (int i = 0; i < a; i++){
			cin >> q[i];
			q[i] *= 10;
		}
		for (int i = 0; i < a; i++){
			for (int j = 0; j < b; j++){
				cin >> p[i][j];
				p[i][j] *= 10;
			}
			sort(p[i], p[i] + b);
		}
		int ans = 0;
		queue<int> l[60], h[60];
		for (int i = 0; i < a; i++){
			for (int j = 0; j < b; j++){
				int lt = getl(p[i][j], q[i]);
				int ht = geth(p[i][j], q[i]);
				if (lt <= ht){
					l[i].push(lt);
					h[i].push(ht);
				}
			}
		}
		bool f = true;
		while (f){
			int lt = -1, ht = 99999999;
			for (int i = 0; i < a; i++){
				if (l[i].empty()){
					f = false;
					break;
				}
				while (!l[i].empty() && h[i].front() < lt){
					l[i].pop();
					h[i].pop();
				}
				lt = max(lt, l[i].front());
				ht = min(ht, h[i].front());
				if (lt > ht) break;
			}
			if (!f) break;
			if (lt <= ht){
				ans++;
				for (int i = 0; i < a; i++){
					l[i].pop();
					h[i].pop();
				}
			} else {
				l[0].pop();
				h[0].pop();
			}
		}
		cout << "Case #" << K << ": ";
		cout << ans << endl;
	}
	
	return 0;
}
