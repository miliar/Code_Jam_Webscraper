#include <bits/stdc++.h>
#define MAX_N 100100
using namespace std;

#define ll long long
#define ull unsigned long long
#define ii pair<int,int>
#define iii pair<ii, int>

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ep emplace_back
#define sz(a) (int) a.size()
#define cl(a) a.clear()

#define vi vector<int>
#define vii vector<ii>

#define LOWBIT(x) ( (x) & -(x) )

#define FOR(x,a,b) for (int x=a;x<=b;x++)
#define FOD(x,a,b) for (int x=a;x>=b;x--)
#define REP(x,a,b) for (int x=a;x<b;x++)
#define RED(x,a,b) for (int x=a;x>b;x--)

const int MAX = 1e5 + 10;
const int MAXN = 1e4 + 10;
const int MOD = 1e9 + 7;
const int inf = 1e9;
const double pi = acos(-1.0);
const double eps = 1e-6;

int dx[] = {0 , -1 , 0 , 1};
int dy[] = {1 , 0 , -1 , 0};

int test;

int main() {
	ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);

    cin >> test; int t = test;

    while (test--) {
        cout << "Case #" << t - test << ": ";
        int N , K;

        cin >> N >> K;

        priority_queue <int> pq;

        pq.push(N);
        K--;

        while (K--) {
            int t = pq.top();
            pq.pop();
            t--;
            pq.push(t / 2);
            pq.push(t - t / 2);
        }

        int t = pq.top();
        t--;
        cout << t - t / 2 << ' ' << t / 2 << endl;
    }

	return 0;
}
