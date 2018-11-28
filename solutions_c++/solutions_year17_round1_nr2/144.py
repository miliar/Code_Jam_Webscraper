#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 60;

int n, p;
vector<int> volume[MAX_N];
int r[MAX_N];
int vis[MAX_N][MAX_N];

void input() {
	scanf("%d%d", &n, &p);
	for (int i = 0; i < n; i++) {
		volume[i] = vector<int> (p);
	}
	for (int i = 0; i < n; i++) {
		scanf("%d", &r[i]);
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < p; j++) {
			scanf("%d", &volume[i][j]);
		}
	}
	for (int i = 0; i < n; i++) {
		sort(volume[i].begin(), volume[i].end());
	}
	memset(vis, 0, sizeof(vis));
}

int get_num(vector<int> &v, int target, int index) {
	int ret = 0;
	for (int i = 0; i < v.size(); i++) {
		auto a = v[i];
		if (a <= target * 1.1 && a >= target * 0.9 && !vis[index][i]) {
			ret++;
		}
	}
	return ret;
}

bool ok(int times) {
	for (int i = 0; i < n; i++) {
		int temp = r[i] * times;
		if (temp * 0.9 > *max_element(volume[i].begin(), volume[i].end())) {
			return false;
		}
	}
	return true;
}

void mark(int num, int times) {
	for (int i = 0; i < n; i++) {
		int low = r[i] * times * 0.9;
		int high = r[i] * times * 1.1;
		int cnt = num;
		for (int j = 0; j < p && cnt > 0; j++) {
			if (!vis[i][j] && volume[i][j] >= low && volume[i][j] <= high) {
				vis[i][j] = true;
//				cout << "marked: " << volume[i][j] << endl;
				cnt--;
			}
		}
	}
}

int work() {
	int times = 1;
	int ret = 0;
	while (ok(times)) {
//		cout << "times: " << times << endl;
		int temp = p;
		for (int i = 0; i < n; i++) {
			temp = min(temp, get_num(volume[i], r[i] * times, i));
		}
//		cout << "temp: " << temp << endl;
		mark(temp, times);
		ret += temp;
		times++;
	}
	return ret;
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
		printf("%d\n", work());
	}
	return 0;
}
