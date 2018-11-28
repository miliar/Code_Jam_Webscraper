#include <bits/stdc++.h>

using namespace std;

#define M_PI 3.14159265358979323846
class Node
{
	public:
		long long r, h;
		bool operator<(const Node& lhs) const {
			return r * h > lhs.r * lhs.h;
		}
		double getH() {
			return 2 * r * M_PI * h;
		}
		double getR() {
			return r * r * M_PI;
		}
};

int n, k;
double calc(vector<Node> &pk, int bi)
{
	vector<Node> v;
	for (int i = 0; i < n; i++) {
		if (i == bi) continue;
		v.push_back(pk[i]);
	}
	sort(v.begin(), v.end());
	double ret = pk[bi].getH() + pk[bi].getR();
	int cnt = 1;
	for (int i = 0; i < v.size() && cnt < k; i++) {
		if (v[i].r > pk[bi].r) continue;
		cnt++;
		ret += v[i].getH();
	}
	return cnt == k ? ret : -1;
}
double solve()
{
	cin >> n >> k;

	vector<Node> pk;
	for (int i = 0; i < n; i++) {
		Node tmp;
		cin >> tmp.r >> tmp.h;
		pk.push_back(tmp);
	}

	double ans = calc(pk, 0);
	for (int i = 1; i < n; i++) {
		ans = max(ans, calc(pk, i));
	}
	return ans;
}

int main()
{
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; cs++) {
		cout << fixed << setprecision(8);
		cout << "Case #" << cs << ": " << solve() << endl;
	}
}
