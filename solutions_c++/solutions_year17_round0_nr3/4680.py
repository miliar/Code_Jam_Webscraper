#include <bits/stdc++.h>
/*
TASK: hidden
LANG: C++11
*/
using namespace std;
typedef long long ll;
typedef pair<int, int> pair2;
typedef pair<int, pair<int, int> > pair3;
typedef pair<int, pair<int, pair<int, int> > > pair4;
#define MAXN 10000
//#define INFINITY 1000000000000000L
#define mp make_pair
#define add push_back
#define remove pop

int n, k;
set<pair2> intervals; //first value is length, second value is index of beginning.
int main() {
	//freopen("friendcross.in", "r", stdin);
	//freopen("friendcross.out", "w", stdout);
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL);

	int T;

	cin >> T;
	int counter = 0;

	while (T--) {
		cin >> n >> k;

		intervals.insert(mp(-n, 0));

		for (int i = 1; i < k; i++) {
			//Place the ith individual
			pair2 temp = *(intervals.begin());
			intervals.erase(temp);
			int start = temp.second;
			int end = temp.second - temp.first - 1;
			int mid = (start + end) / 2;

			intervals.insert(mp(-(mid - start), start));
			intervals.insert(mp(-(end - mid), mid + 1));
		}

		//Place the kth individual
		pair2 temp = *(intervals.begin());
		intervals.erase(temp);
		int start = temp.second;
		int end = temp.second - temp.first - 1;
		int mid = (start + end) / 2;

		int l1 = (mid - start);
		int l2 = (end - mid);

		cout << "Case #" << ++counter << ": " << max(l1, l2) << " " << min(l1, l2) << '\n';
		intervals.clear();
	}

}