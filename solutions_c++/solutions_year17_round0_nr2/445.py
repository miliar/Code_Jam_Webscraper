#include <iostream>


using namespace std;
typedef long long ll;

void solve()
{
    string K;
    cin >> K;
    int N = K.length();
    int to_check = 0;
    for (int i = 0; i < N-1; ++i) {
        if (K[i] < K[i+1]) {
            for(int j = to_check; j <= i; ++j) cout << K[i];
            to_check = i+1;
            continue;
        }
        if (K[i] > K[i+1]) {
            if (to_check == 0 && K[0] == '1') {

            }
            else {
                cout << (char)(K[to_check]-1);
            }
            for(int j = to_check+1; j < N; ++j) {
                cout << 9;
            }
            cout << endl;
            return;
        }
    }
    for(int i = to_check; i < N; ++i) cout << K[i];
    cout << endl;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
}