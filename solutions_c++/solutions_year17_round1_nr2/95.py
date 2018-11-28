#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <complex>
#include <random>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const int MAX = 1111115;
const int MAXN = 55;
int T, N, P;
ll R[MAXN];
ll Q[MAXN][MAXN];
int idx[MAXN];

int go()
{
    for (int i = 0; i < N; i++)
    {
        sort(Q[i], Q[i] + P);
        idx[i] = 0;
    }

    int ans = 0;
    for (int i = 1; i < MAX; i++)
    {
        while (true)
        {
            bool found = true;
            for (int j = 0; j < N; j++)
            {
                while (idx[j] < P && Q[j][idx[j]] < 0.9*i*R[j])
                    idx[j]++;
                if (idx[j] == P || Q[j][idx[j]] > 1.1*i*R[j])
                {
                    found = false;
                    break;
                }
            }
            if (!found)
                break;

            for (int j = 0; j < N; j++)
                idx[j]++;
            ans++;
        }
    }
    return ans;
}

int main()
{
	ios::sync_with_stdio(0);

    freopen("B.in", "r", stdin);
    freopen("Bout.txt", "w", stdout);

    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> N >> P;
        for (int i = 0; i < N; i++)
            cin >> R[i];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < P; j++)
                cin >> Q[i][j];

        cout << "Case #" << t << ": " << go() << "\n";
    }

	return 0;
}
