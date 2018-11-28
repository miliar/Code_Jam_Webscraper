#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define s second
#define f first
#define mp make_pair

using namespace std;
const int maxn = 1e6+123;
const int mod = 1e9+7;


string s;
int k,vmx,vmn,n;

int main() {
 //	freopen("in","r",stdin);
// 	freopen("out","w",stdout);
 	int tt;
 	cin >> tt;
 	for (int ii = 1, sz; ii <= tt; ii++) {
 		printf("Case #%d: ",ii);
 		cin >> n >> k;
 		set <pair <int, pair <int, int> > > q;

 		int l, r, len, tm;
 		q.insert(mp(-n, mp(1,n)));
 		for (int i = 1; i <= k; i++) {
 			pair <int, int> v = (*q.begin()).s;
 			q.erase(q.begin());
 			l = v.f, r = v.s;
 			len = r - l + 1;
 			tm = (l+r) >> 1;
 			vmx = r - tm;
 			vmn = tm - l;
 			if (l<r) {
 				q.insert(mp(-(tm-l), mp(l, tm-1)));
 				q.insert(mp(-(r-tm), mp(tm+1,r)));
 			}
 		}
 		printf("%d %d\n", vmx, vmn);
 	}
 	return 0;
}