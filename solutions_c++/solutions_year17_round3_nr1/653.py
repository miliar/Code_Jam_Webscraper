#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const int N = 1500;

double a[N],b[N];

double c[N];

int id[N];

bool cmp(int x,int y){
	return c[x] > c[y];
}

int main(){
	int n,T;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin >> T;
	int nc = 0;
	while(T--){
		int n,k;
		cin >> n >> k;
		for (int i = 1;i <= n;i++){
			cin >> a[i] >> b[i];
			c[i] = 2 * acos(-1.0) * a[i] * b[i];
		}
		for (int i = 1;i <= n;i++) id[i] = i;
		sort(id + 1,id + n + 1,cmp);
		double ans = 0;
		for (int i = 1;i <= n;i++){
            int x = id[i];
            double now = a[x] * a[x] * acos(-1.0);
            now += c[x];
            int cnt = k - 1;
            for (int j = 1;j <= n;j++){
                if (!cnt) break;
                if (i == j) continue;
                now += c[id[j]];
                cnt--;
            }
            ans = max(ans,now);
		}
		printf("Case #%d: ",++nc);
        printf("%.9f\n",ans);
	}

}
