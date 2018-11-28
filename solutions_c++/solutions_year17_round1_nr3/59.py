#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <map>
#define LL long long
#define N 101
#define fi(a, b, c) for(int a = (b); a < (c); a++)
#define FI(a, b, c) for(int a = (b); a <= (c); a++)
#define FD(a, b, c) for(int a = (b); a >= (c); a--)
using namespace std;

int t, hd, ad, hk, ak, b, d, ans;
map<int, int> dis;
queue<int> q;

int hash(int hd, int ad, int hk, int ak){
	return ((hd * N + ad) * N + hk) * N + ak;
}

void get(int w, int &hd, int &ad, int &hk, int &ak){
	ak = w % N;
	w /= N;
	hk = w % N;
	w /= N;
	ad = w % N;
	w /= N;
	hd = w % N;
}

void push(int hd, int ad, int hk, int ak, int di){
	if(hd <= 0) return;
	int t = hash(hd, ad, hk, ak);
	if(dis[t]) return;
	q.push(hash(hd, ad, hk, ak));
	dis[q.back()] = di;
}

void solve(int tc){
	scanf("%d %d %d %d %d %d", &hd, &ad, &hk, &ak, &b, &d);
	
	while(q.size()) q.pop();
	q.push(hash(hd, ad, hk, ak));
	dis.clear();
	dis[q.back()] = 1;
	
	ans = -1;
	while(!q.empty()){
		int y = q.front(), di = dis[y];
		q.pop();
		
		int Hd, Ad, Hk, Ak;
		get(y, Hd, Ad, Hk, Ak);
		if(!di) printf("%d %d %d %d %d\n", Hd, Ad, Hk, Ak, di);
		if(Hk <= Ad){
			ans = di;
			break;
		}
		
		push(Hd - Ak, Ad, Hk - Ad, Ak, di + 1);
		
		if(Ad < Hk) push(Hd - Ak, min(Hk, Ad + b), Hk, Ak, di + 1);
		
		push(hd - Ak, Ad, Hk, Ak, di + 1);
		
		if(Ak > 0) push(Hd - max(0, Ak - d), Ad, Hk, max(0, Ak - d), di + 1);
	}
	
	printf("Case #%d: ", tc);
	if(ans < 0) puts("IMPOSSIBLE");
	else printf("%d\n", ans);
}

int main(){
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w+", stdout);
	scanf("%d", &t);
	FI(z, 1, t) solve(z);
}

