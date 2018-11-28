#pragma comment(linker, "/STACK:36777216")

#include <bits/stdc++.h>
#include <pthread.h>
#include <ext/rope>

#define L(a) (int)((a).size())
#define sqr(x) ((x) * 1ll * (x))
#define vi vector<int>
#define mp make_pair
#define pub push_back
#define pob pop_back
#define ii pair<int, int>
#define vii vector <ii>
#define all(s) (s).begin(),(s).end()
#define fore(i, l ,r) for(int i = (int)l; i < (int)r; i++)
#define TRACE(x) cerr << #x << " : " << x << endl
#define _ << " - " << 

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;


const ld EPS = 1e-9;
const ld PI = acos((ld)-1);
const int MOD = (int)1e9 + 7;
const int INF32 = (int)1e9;
const int INF64 = (ll)1e19;

using namespace std;
using namespace __gnu_cxx;

int main()
{
	int t;
	cin >> t;
	fore(tc, 1, t + 1)
	{
		int n, k;
		cin >> n >> k;
		priority_queue <int> pq;
		pq.push(n);
		fore(i, 0, k - 1)
		{
			int head = pq.top();
			pq.pop();
			int mid = head >> 1;
			pq.push(mid);
			pq.push(head - mid - 1);
		}
		cout << "Case #" << tc << ": ";
		int res = pq.top();
		int mid = res >> 1;
		cout << mid << " " << res - mid - 1 << endl;
	}
}