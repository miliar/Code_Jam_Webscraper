#include<bits/stdc++.h>
using namespace std;
#define SZ(a) ((int)a.size())
typedef pair<int,int> pii;
#define F first
#define S second
/*I DUCK HORSE*/
struct cmp
{
	bool operator () (const pii & x, const pii & y)
	{
		return y.F > x.F || (y.F == x.F && y.S < x.S);
	}
};
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for (int kase=1;kase<=T;++kase) {
		int n,k;
		cin >> n >> k;
		priority_queue<pii, vector<pii>, cmp> pq;
		pq.push({n,0});
		pii x;
		int a,b;
		while (k--) {
			x = pq.top();
			pq.pop();
			a = x.F - 1;
			b = a/2;
			a -= b;
			pq.push({b,x.S});
			pq.push({a,x.S+b+1});
		}
		cout << "Case #" << kase << ": ";
		cout << a << ' ' << b << '\n';
	}
}
