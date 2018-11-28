#include<bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const int N=1010;
const double pi=acos(-1);
struct Node{
	int r, h, id;
	double s1, s2;
}a[N], b[N];
bool cmp1(Node x, Node y){
	return x.s1>y.s1;
}
bool cmp2(Node x, Node y){
	return x.s2>y.s2;
}
int T, n, K;
bool vis[N];
double ans;
int main() {
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for(int cas=0; cas<T; cas++){
		ans=0;
		scanf("%d%d", &n, &K);
		for(int i=0; i<n; i++){
			int r, h;
			scanf("%d%d", &r, &h);
			a[i].r=r;
			a[i].h=h;
			a[i].s1=pi*r*r;
			a[i].s2=pi*r*2*h;
			a[i].id=i;
			b[i]=a[i];
		}
		sort(a, a+n, cmp1);
		sort(b, b+n, cmp2);
		for(int i=0; i<n; i++){
			memset(vis, 0, sizeof(vis));
			vis[a[i].id]=1;
			double t=a[i].s1+a[i].s2;
			for(int j=0, k=1; k<K&&j<n; j++){
				if(vis[b[j].id])continue;
				k++;
				t+=b[j].s2;
			}
			ans=max(ans, t);
		}
		printf("Case #%d: %.7f\n", cas+1, ans);
	}
	return 0;
}
