#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define pf push_front
int T, n, r, o, y, g, b, v, rr, yy, bb;
int f(int x) {
	int maxx=-1, res=-1;
	if (r>maxx&&x!=1) res=1, maxx=r;
	if (y>maxx&&x!=2) res=2, maxx=y;
	if (b>maxx&&x!=3) res=3, maxx=b;
	return res;
}
vector<int> sol(int st) {
	vector<int>fail;
	fail.pb(-1);
	r=rr; y=yy; b=bb;
	deque<int>d;
	if (st==1&&r>0) d.pb(1), r--;
	else if (st==2&&y>0) d.pb(2), y--;
	else if (st==3&&b>0) d.pb(3), b--;
	else return fail;
	bool fr=true, ok=true;
	int t;
	while (r>0||y>0||b>0) {
		if (fr) t=f(d.front());
		else t=f(d.back());
		//printf("%d %d %d %d\n", r, y, b, t);
		if (fr)  {
			if (t==1&&r>0) d.pf(1), r--;
			else if (t==2&&y>0) d.pf(2), y--;
			else if (t==3&&b>0) d.pf(3), b--;
			else {
				ok=false;
				break;
			}
		} else {
			if (t==1&&r>0) d.pb(1), r--;
			else if (t==2&&y>0) d.pb(2), y--;
			else if (t==3&&b>0) d.pb(3), b--;
			else {
				ok=false;
				break;
			}
		}
		fr=!fr;
	}
	if (!ok) return fail;
	if (d.front() == d.back()) return fail;
	vector<int>v;
	for (int i=0; i<n; i++) {
		v.pb(d.front());
		d.pop_front();
	}
	return v;
}
void solve(int test) {
	scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
	rr=r; yy=y; bb=b;
	vector<int>ans;
	ans=sol(1);
	if (ans.size()==1) {
		ans=sol(2);
		if (ans.size()==1) {
			ans=sol(3);
		}
	}
	printf("Case #%d: ", test);
	if (ans.size()==1) printf("IMPOSSIBLE\n");
	else {
		for (int i=0; i<ans.size(); i++) {
			if (ans[i]==1) printf("R");
			else if (ans[i]==2) printf("Y");
			else printf("B");
		}
		printf("\n");
	}
}
int main () {
	freopen("B-small.in", "r", stdin);
	freopen("B-small1.out", "w", stdout);
	scanf("%d", &T);
	for (int i=1; i<=T; i++) {
		solve(i);
	}
	return 0;
}
