#include <bits/stdc++.h>
using namespace std;

int hd, ad, hk, ak, bb, dd;

void input() {
	scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &bb, &dd);
}

int cal(int inc, int dec) {
	int ret = 0;
	int temp_lose = ak;
	int current_life = hd;
	int attack = ad;
	int knight = hk;
	int cnt = 500;
	while (knight > 0 && cnt--) {
		ret++;
		if (dec > 0 && current_life - (temp_lose - dd) > 0) {
			dec--;
			temp_lose -= dd;
			current_life -= temp_lose;
			continue;
		}
		if (inc > 0 && current_life - temp_lose > 0) {
			inc--;
			attack += bb;
			current_life -= temp_lose;
			continue;
		}
		if (current_life - temp_lose <= 0 && knight - attack > 0) {
			current_life = hd;
			current_life -= temp_lose;
			continue;
		}
		knight -= attack;
		current_life -= temp_lose;
	}
	return ret;
}

int work() {
	int max_inc = 0;
	if (bb > 0) {
		max_inc = (hk - ad + bb - 1) / bb;
	}
	int max_dec = 0;
	if (dd > 0) {
		max_dec = (ak + dd - 1) / dd;
	}
	int ans = 500;
	for (int i = 0; i <= max_inc; i++) {
		for (int j = 0; j <= max_dec; j++) {
			ans = min(ans, cal(i, j));
		}
	}
	return ans;
}

int main()
{
	int t;
	scanf("%d", &t);
	int case_num = 0;
	while (t--)
	{
		case_num++;
		printf("Case #%d: ", case_num);
		input();
		//if (hd <= 2 * (ak - dd) && ad + bb < hk) {
		//	puts("IMPOSSIBLE");
		//	continue;
		//}
		int ans = work();
		if (ans == 500) {
			puts("IMPOSSIBLE");
		}else {
			printf("%d\n", ans);
		}
	}
	return 0;
}
