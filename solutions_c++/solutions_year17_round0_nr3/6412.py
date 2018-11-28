// ProblemC.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <tuple>

using namespace std;

tuple<int, int> compute(string bathroom, const int people_number)
{
	// cout << "compute " << bathroom << " " << people_number << endl;

	vector<int> min_v;
	vector<int> max_v;
	for (int i = 1; i < (bathroom.size() - 1); i++) {
		// cout << "i " << i << endl;
		int LS = -1, RS = -1;
		if (bathroom[i] == '.') {
			LS = 0;
			for (int left = i - 1; left >= 0; left--) {
				if (bathroom[left] == 'O')
					break;
				LS++;
			}

			RS = 0;
			for (int right = i + 1; right < bathroom.size(); right++) {
				if (bathroom[right] == 'O')
					break;
				RS++;
			}
		}
		// cout << "LS " << LS << endl;
		// cout << "RS " << RS << endl;
		min_v.push_back(std::min(LS, RS));
		max_v.push_back(std::max(LS, RS));
	}

	int max_min = -1;
	for (int e : min_v)
		max_min = std::max(max_min, e);
	// cout << "max_min " << max_min << endl;

	int max_max = -1;
	for (int i = 0; i < max_v.size(); i++) {
		if (min_v[i] == max_min)
			max_max = std::max(max_max, max_v[i]);
	}
	// cout << "max_max " << max_max << endl;

	if (people_number == 1) {
		return make_tuple(max_max, max_min);
	}

	for (int i = 0; i < max_v.size(); i++) {
		// cout << "i " << i << endl;
		if ((min_v[i] == max_min)
			&& (max_v[i] == max_max)) {
			bathroom[i + 1] = 'O';
			break;
		}
	}

	return compute(bathroom, people_number - 1);
}

int main()
{
	int T;
	cin >> T;
	// cout << "T " << T << endl;

	for (int i = 0; i < T; i++) {
		int N, K;
		cin >> N >> K;
		// cout << "N " << N << endl;
		// cout << "K " << K << endl;

		string bathroom(N + 2, '.');
		bathroom[0] = 'O';
		bathroom[N + 1] = 'O';

		int max, min;
		tie(max, min) = compute(bathroom, K);
		cout << "Case #" << to_string(i + 1) << ": " << max << " " << min << endl;
	}

    return 0;
}

