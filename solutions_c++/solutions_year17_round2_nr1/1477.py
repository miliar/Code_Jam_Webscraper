#include<bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define pb push_back
#define mk make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
const int N=1010;
int T, n, D;
int ki[N], Si[N];
double tim[N];
int main(){
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for(int cas=0; cas<T; cas++){
		double sl=0;
		scanf("%d%d", &D, &n);
		for(int i=0; i<n; i++){
			scanf("%d%d", ki+i, Si+i);
			tim[i]=1.0*(D-ki[i])/Si[i];
			sl=max(sl, tim[i]);
		}
		printf("Case #%d: %.7f\n", cas+1, D/sl);
	}
	return 0;
}

