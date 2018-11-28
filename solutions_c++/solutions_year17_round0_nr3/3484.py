#include <bits/stdc++.h>

using namespace std;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef unsigned long long int ulli;
typedef pair<ulli, ulli > ullii;

ullii even(ulli n) {
	return ullii((n / 2 - 1), (n / 2));
}

ullii odd(ulli n) {
	return ullii((n / 2), (n / 2));
}

bool cmp(ullii a, ullii b) {
	return (a.first < b.first);
}

int main()
{
	ulli n, k, L, R, c, aux;
	bool foundFirst, foundSecond;
	vector<ullii > count;
	ullii temp, current;
	int T, currT = 1;
	cin >> T;
	while(T--) {
		cin >> n >> k;
		if(n == k) {
			L = 0; R = 0;
		} else {
			c = 0;
			count.push_back(ullii(n, 1));

			while(c < k) {
				current = count[count.size() - 1];
				foundFirst = false; foundSecond = false;
				//cout << current.first << " " << current.second << endl;
				count.pop_back();
				if(current.first % 2 == 0) {
					temp = even(current.first);
					L = temp.second; R = temp.first;
					for (int i = 0; i < (int)count.size(); ++i)
					{
						if(!foundFirst && temp.first == count[i].first) {
							count[i].second += current.second;
							foundFirst = true;
						}
						if(!foundSecond && temp.second == count[i].first) {
							count[i].second += current.second;
							foundSecond = true;
						}
					}
					if(!foundSecond) count.push_back(ullii(temp.second, current.second));
					if(!foundFirst) count.push_back(ullii(temp.first, current.second));
				} else {
					aux = current.first / 2;
					L = aux; R = aux;
					for (int i = 0; i < (int)count.size(); ++i)
					{
						if(aux == count[i].first) {
							count[i].second += current.second * 2;
							foundFirst = true;
							break;
						}
					}
					if(!foundFirst) count.push_back(ullii(aux, current.second * 2));
				}
				c += current.second;
				sort(count.begin(), count.end(), cmp);
			}

			count.clear();
		}

		cout << "Case #" << currT << ": " << L << " " << R << endl;
		currT++;
	}
	return 0;
}