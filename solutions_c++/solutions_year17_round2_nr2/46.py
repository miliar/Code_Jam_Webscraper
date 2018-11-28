#include <bits/stdc++.h>

#define debug(x) cout << #x" = " << x;

#define st first
#define nd second

using namespace std;
using namespace placeholders;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;

const char out[] = "ROYGBV";
const char *fail = "IMPOSSIBLE";

int a[6];
string ans;

void solve3(){
	int val = max(a[0], max(a[2], a[4]));
	if (a[0] + a[2] + a[4] - val < val){
		ans = fail;
		return;
	}

	for (int i = 0; i < 6; i += 2)
		if (a[i] == val){
			ans = string(val, out[i]);
			a[i] = 0;
			break;
		}

	int cnt = 0;
	for (int i = 0; i < 6; i += 2)
		for (int j = 0; j < a[i]; ++j){
			ans.insert(cnt, 1, out[i]);
			if ((cnt += 2) >= ans.size())
				cnt = 0;
		}
}

void solve2(int i, int j){
	if (a[i] != a[j])
		ans = fail;
	else{
		ans.clear();
		for (int k = 0; k < a[i]; ++k)
			ans.push_back(out[i]), ans.push_back(out[j]);
	}
}

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		int n;
		scanf("%d", &n);
		for (int i = 0; i < 6; ++i)
			scanf("%d", a + i);

		bool flag = true;
		for (int i = 0; i < 6; i += 2){
			int j = (i + 3) % 6;

			if (a[i] == a[j] && a[i] + a[j] == n){
				ans.clear();
				for (int k = 0; k < a[i]; ++k)
					ans.push_back(out[i]), ans.push_back(out[j]);
				puts(ans.c_str());
				flag = false;
				break;
			}

			if (!(a[j] == 0 || (a[i] -= a[j]) > 0)){
				puts(fail);
				flag = false;
				break;
			}
		}
		if (!flag){
			continue;
		}

		int type = !!a[0] << 2 | !!a[2] << 1 | !!a[4];
		switch (type){
		case 7:
			solve3();
			break;
		case 3:
			solve2(2, 4);
			break;
		case 5:
			solve2(0, 4);
			break;
		case 6:
			solve2(0, 2);
			break;
		default:
			ans = fail;
			break;
		}
		if (ans != fail){
			for (int i = 0; i < 6; i += 2){
				int j = (i + 3) % 6;
				string t = "";
				for (int k = 0; k < a[j]; ++k)
					t.push_back(out[i]), t.push_back(out[j]);
				if (a[j])
					ans.insert(ans.find(out[i]), t);
			}
		}

		puts(ans.c_str());
	}
	return 0;
}
