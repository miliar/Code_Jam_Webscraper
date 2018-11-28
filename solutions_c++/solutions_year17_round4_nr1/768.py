#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
pair<int, int> pii;

#define F first
#define S second

const int MAXN = 100 + 10;

int n, k, cnt[5];

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int te;	cin >> te;
	for (int w = 1; w <= te; w++){
		cin >> n >> k;
		memset(cnt, 0, sizeof(cnt));
		while (n--){
			int x;	cin >> x;
			cnt[x%k]++;
		}

		int ans = cnt[0];
		if (k == 2)
			ans += cnt[1]+1>>1;
		else if (k == 3){
			int mn = min(cnt[1], cnt[2]);
			ans += mn;
			cnt[1] -= mn;
			cnt[2] -= mn;
			ans += (max(cnt[1], cnt[2])+2)/ 3;
		}
		else{
			ans += cnt[2]>>1;
			cnt[2] &= 1;

			int mn = min(cnt[1], cnt[3]);
			ans += mn;
			cnt[1] -= mn;
			cnt[3] -= mn;

			if (cnt[1]){
				ans += cnt[1]/4;
				cnt[1] %= 4;
				if (max(cnt[2], cnt[1]))
					ans++;
				if (cnt[2] && cnt[1] > 2)
					ans++;
			}
			if (cnt[3]){
				ans += cnt[3]/4;
				cnt[3] %= 4;
				if (max(cnt[2], cnt[3]))
					ans++;
				if (cnt[2] && cnt[3] > 2)
					ans++;
			}
		}

		cout << "Case #" << w << ": " << ans << "\n";
	}
	return 0;
}
