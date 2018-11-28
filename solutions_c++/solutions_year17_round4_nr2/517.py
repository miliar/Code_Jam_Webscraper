#include <bits/stdc++.h>
#define AddEdge(x, y, c, v) num[tail[x] = next[tail[x]] = ++ tot] = y; cap[tot] = c; val[tot] = v;
#define N 2222222
int n, c, m, tot;
int num[N],next[N],tail[N],cap[N],val[N],man[N],seat[N],d[2222],fa[2222],ifa[2222];

void clear(){
	tot = n = c = m = 0;
	memset(num, 0, sizeof num);
	memset(next, 0, sizeof num);
	memset(tail, 0, sizeof num);
	memset(cap, 0, sizeof num);
	memset(val, 0, sizeof num);
	memset(man, 0, sizeof num);
	memset(seat, 0, sizeof num);
}

int Max(int a, int b){
	return a > b ? a : b;
}
int calc_man(){
	int max = 0, tot = 0;
	for (int i = 1; i <= c; i ++ ){
		tot += man[i];
		if (man[i] > max) max = man[i];
	}
	tot = tot ? (tot - 1) / n + 1 : 0;
	return max > tot ? max : tot;
}
int calc_seat(){
	int res = 0, tot = 0;
	for (int i = 1; i <= n; i ++ ){
		tot += seat[i];
		if ((tot - 1) / i + 1 > res) res = (tot - 1) / i + 1;
	}
	return res;
}
int spfa(){
	memset(d, 63, sizeof d);
	memset(fa, 0, sizeof fa);
	memset(ifa, 0, sizeof ifa);
	d[n + n + 1] = 0;
	std::vector<int> l;
	l.push_back(n + n + 1);
	for (int t = 0; t < l.size(); t ++ ){
		int now = l[t];
		//printf("l: %d %d\n", now, d[now]);
		for (int i = next[now]; i; i = next[i])
			if (cap[i] && d[now] + val[i] < d[num[i]]){
				fa[num[i]] = now;
				ifa[num[i]] = i;
				d[num[i]] = d[now] + val[i];
				l.push_back(num[i]);
			}
	}
	if (fa[n + n + 2]){
		for (int i = n + n + 2; fa[i]; i = fa[i]){
			int j = ifa[i];
			cap[j] -- ;
			cap[j ^ 1] ++ ;
		}
	}
	return d[n + n + 2];
}

void Main(){
	clear();
	scanf("%d%d%d", &n, &c, &m);
	for (int i = 0; i < m; i ++ ){
		int t1, t2;
		scanf("%d%d", &t1, &t2);
		seat[t1] ++ ;
		man[t2] ++ ;
	}
	int turn = Max(calc_man(), calc_seat());
	/*for (int i = 1; i <= n + n + 2; i ++ )
		tail[i] = i;
	tot = n + n + 3;
	for (int i = 1; i <= n; i ++ )
		for (int j = 1; j <= n; j ++ ){
			if (i == j){
				AddEdge(i, j + n, 99999, 0);
				AddEdge(j + n, i, 0, 0);
			}
			else if (i < j){
				AddEdge(i, j + n, 99999, 1);
				AddEdge(j + n, i, 0, - 1);
			}
		}*/
	/*for (int i = 1; i <= n; i ++ ){
		AddEdge(i, i + n, 99999, 0);
		AddEdge(i + n, i, 0, 0);
		if (i != n){
			AddEdge(i, i + 1, 99999, 1);
			AddEdge(i + 1, i, 0, - 1);
		}
	}*/
	/*for (int i = 1; i <= n; i ++ ){
		AddEdge(n + n + 1, i, turn, 0);
		AddEdge(i, n + n + 1, 0, 0);
		AddEdge(i + n, n + n + 2, seat[i], 0);
		AddEdge(n + n + 2, i + n, 0, 0);
	}
	int minchange = 0;
	for (; ; ){
		int spfares = spfa();
		if (spfares > 9999) break;
		minchange += spfares;
	}*/
	int minchange = 0;
	for (int i = 1; i <= n; i ++ )
		if (seat[i] > turn) minchange += seat[i] - turn;
	printf("%d %d\n", turn, minchange);
	fflush(stdout);
}
int main(){
	freopen("t.in","r",stdin);
	freopen("t.out","w",stdout);
	//int cc = clock();
	int _;
	scanf("%d", &_);
	for (int i = 1; i <= _; i ++ ){
		printf("Case #%d: ", i);
		Main();
		//printf("%d\n", clock() - cc);
	}
}
