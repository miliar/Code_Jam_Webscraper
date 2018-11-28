#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

#ifdef ROOM_311
__attribute__((destructor)) void fini_main()
{
	fprintf(stderr, "Execution time = %0.0lf ms\n", clock() * 1000.0 / CLOCKS_PER_SEC);
}
#endif

#define MY_RAND 1
#if MY_RAND
uint64_t rnd_data = 0xDEADBEEFDULL;
inline void my_srand(int seed) { rnd_data = ((uint64_t)seed << 16) | 0x330E; }
inline int my_rand() { rnd_data = rnd_data * 0x5DEECE66DULL + 0xB; return (rnd_data >> 17) & 0x7FFFFFFF; }
#define rand my_rand
#define srand my_srand
template <typename T> void my_random_shuffle(T b, T e) { for(ssize_t i = 1; i < (e - b); i++) { swap(b[i], b[rand() % (i + 1)]); } }
#define random_shuffle my_random_shuffle
#endif

template <class _T> inline _T sqr(const _T &x) { return x * x; }

// Types
typedef long double ld;
typedef long long i64;
typedef __int128 i128;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < int > VI;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-9;

int qq;
int n, m, k;
int s[1024];
int h[1024];
int a[1024][2];

inline void upd(int &a, int b)
{
	if (a < b) a = b;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d: ", ii+1);
		fprintf(stderr, "Case #%d:\n", ii+1);
		
		clr(s);
		clr(h);
		scanf("%d%d%d", &n, &k, &m);
		forn(i, m)
		{
			int x, y;
			scanf("%d%d", &x, &y);
			x--;
			y--;
			a[i][0] = x;
			a[i][1] = y;
			s[x]++;
			h[y]++;
		}
		int ans = 0;
		forn(i, k)
		{
			upd(ans, h[i]);
		}
		int sum = 0;
		For(j, 1, n)
		{
			sum += s[j - 1];
			upd(ans, (sum + j - 1) / j);
		}
		int cnt = 0;
		forn(i, n)
		{
			if (s[i] > ans)
			{
				cnt += s[i] - ans;
			}
		}
		printf("%d %d\n", ans, cnt);
		
		fflush(stdout);
	}

	return 0;
}
