#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
#include <cmath>


using namespace std;

int T;
int N,P;

const int maxn = 105;

int q[maxn][maxn];
int p[maxn];

int R[maxn];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);
	cin >> T;
	int cas = 0;
	while(T--){
		cas++;
		cin >> N >> P;
		for(int i = 1;i <= N;i++) cin >> R[i];
		for(int i = 1;i <= N;i++){
			for(int j = 1;j <= P;j++){
				cin >> q[i][j];
			}
			sort(q[i] + 1,q[i] + 1 + P);
		}
		for(int i = 1;i <= N;i++){
			p[i] = 1;
		}
		int ans = 0;
		for(int s = 1;s <= 1000000;s++){
			bool flag = true;
			for(int i = 1;i <= N;i++){
				long long d = ceil(0.9 * s * R[i]);
				//cout << d << endl;
				while(p[i] <= P && q[i][p[i]] < d) p[i]++;
				d = ceil(1.1 * s * R[i]);
				long long dd = floor(1.1 * s * R[i]);
				if(q[i][p[i]] > dd || p[i] > P) flag = false;
			}
			if(flag){
				ans++;
				s = s - 1;
				for(int i = 1;i <= N;i++) p[i]++;
			}
			bool f = false;
			for(int i = 1;i <= N;i++) if(p[i] > P) f = true;
			if(f) break;
		}
		printf("Case #%d: ",cas);
		cout << ans << endl;
	}
	return 0;
}
