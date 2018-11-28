#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

int a[150];

int solve(int n,int m){
	for (int i = 1;i <= n;i++) cin >> a[i];

	if (m == 1) return n;

	if (m == 2){
		int cnt = 0;
		for (int i = 1;i <= n;i++)
			if(a[i] % 2 == 0) cnt++;
        if (cnt == n) return n;
		return cnt + (n - cnt - 1) / 2 + 1;
	}

	if (m == 3){
		int num[3];
		memset(num,0,sizeof(num));
		for (int i = 1;i <= n;i++)
			num[a[i] % 3]++;
		int ans = 0;
		ans += num[0];
		ans += min(num[1],num[2]);
		int v1 = max(num[1],num[2]);
		int v2 = min(num[1],num[2]);
		v1 -= v2;
		if (v1 > 0) ans += (v1 - 1) / 3 + 1;
		return ans;
	}

	if (m == 4){
		int num[4];
		memset(num,0,sizeof(num));
		for (int i = 1;i <= n;i++)
			num[a[i] % 4]++;
		int ans = 0;
		ans += num[0];
		ans += num[2] / 2;
		ans += min(num[1],num[3]);
		int v2 = min(num[1],num[3]);
		int v1 = max(num[1],num[3]);
		v1 -= v2;
		if (num[2] % 2 == 1){
            if (v1 >= 2) ans++,v1 -= 2;
            else{
                if (v1 == 0) return ++ans;
            }
		}
        if (v1 > 0) ans += (v1 - 1) / 4 + 1;
		return ans;
	}
}

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
	int T;
	ios_base::sync_with_stdio(false);
	cin >> T;
	int n,m;
	int nc = 0;
	while(T--){
		cin >> n >> m;
        cout << "Case #" << ++nc << ": ";
		cout << solve(n,m) << endl;
	}
}
