#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

pair<int, int> getMinMax(int target, int amount) {
	int minm = (amount * 100 + target * 110 - 1) / (target * 110);
	int maxm = (amount * 100) / (target * 90);
	return make_pair(minm, maxm);
}
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int n, p;
		cin >> n >> p;
		vector<int> ingridients(n);
		for (int i = 0; i < n; i++)
			cin >> ingridients[i];
		vector<deque<pair<int, int> > > v(n);
		int tmp;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j< p; j++) {
				cin >> tmp;
				pair<int, int> p = getMinMax(ingridients[i], tmp);
				if (p.first <= p.second)
					v[i].push_back(p);
			}
			sort(v[i].begin(), v[i].end());
		}
		int initial = -1;
		bool isEmpty = false;
		for (int i = 0; i < n; i++) {
			if (v[i].size() > 0)
				initial = max(initial, v[i][0].first);
			else
				isEmpty = true;
		}
		bool removed = true;
		
		int cnt = 0;
		while (!isEmpty) {
			if (removed) {
				removed = false;
				for (int i = 0; i < n; i++) {
					while (v[i][0].second < initial) {
						v[i].pop_front();
						if (v[i].size() > 0 && initial < v[i][0].first) {
							initial = v[i][0].first;
							removed = true;
						}
						if (v[i].size() == 0) {
							isEmpty = true;
							break;
						}
					}
				}
			} else {
				cnt++;
				initial = -1;
				removed = true;
				for (int i = 0; i < n; i++) {
					v[i].pop_front();
					if (v[i].size() > 0 && initial < v[i][0].first) {
						initial = v[i][0].first;
					}
					if (v[i].size() == 0) {
						isEmpty = true;
						break;
					}
				}
			}
		}

		if (isEmpty) {
			cout << cnt << endl;
		}
	}
	return 0;
}


