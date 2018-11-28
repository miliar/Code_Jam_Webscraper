#include <iostream>


using namespace std;


void solve()
{
    string cakes;
    int K;
    int N;

    cin >> cakes >> K;
    N = cakes.length();

    int cnt = 0;
    for (int i = 0; i < N-K+1; ++i) {
        if (cakes[i] == '+') continue;
        ++cnt;
        for (int j = 0; j < K; ++j) {
            if (cakes[i+j] == '-') cakes[i+j] = '+';
            else cakes[i+j] = '-';
        }
    }
    for (int i = 0; i < N; ++i) {
        if (cakes[i] == '-') { 
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << cnt << endl;
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