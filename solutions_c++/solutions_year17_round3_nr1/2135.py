#include <iostream>
#include <string>
#include <vector>
#include <memory.h>
#include <algorithm>
#include <cmath>
typedef long long LL;
typedef double D;
using namespace std;

struct node
{
	int R, H;
};

node arr[1000];

D DP[1001][1001][2];
const D pi = acos(-1.0);

D biggest[1001][1001];
int N;

D dp(int maxnum, int cnt, bool used)
{
	if (DP[maxnum][cnt][used] != -1)
		return DP[maxnum][cnt][used];
	if (N - maxnum > cnt)
	{
		DP[maxnum][cnt][used] = dp(maxnum + 1, cnt, used);
//		used[maxnum] = 0;
	}
	D val;
	if (used)
	{
		val = dp(maxnum + 1, cnt - 1, used) + 2.0 * pi * arr[maxnum].R * arr[maxnum].H;
	}
	else
		val = val = dp(maxnum + 1, cnt - 1, 1) + 2.0 * pi * arr[maxnum].R * arr[maxnum].H + pi * arr[maxnum].R * arr[maxnum].R;
	if (val > DP[maxnum][cnt][used])
	{
		DP[maxnum][cnt][used] = val;
//		biggest[maxnum][cnt] = arr[maxnum].R;
//		used[maxnum] = 1;
	}
	return DP[maxnum][cnt][used];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	cout.precision(20);
	for (int t = 0; t < T; ++t)
	{
		int K;
		cin >> N >> K;
		for (int i = 0; i < N; ++i)
			cin >> arr[i].R >> arr[i].H;
		
		sort(arr, arr + N, [](node a, node b) {return a.R >= b.R;});
		
		for (int i = 0; i < 1001; ++i)
		{
			DP[i][0][0] = 0;
			DP[i][0][1] = 0;
			for (int j = 1; j < 1001; ++j)
				DP[i][j][0] = DP[i][j][1] = -1;
		}
//		memset(biggest, 0, sizeof(biggest));
//		memset(used, 0, sizeof(used));
		
//		int cnt = 0;
//		D R = 0, res = dp(0, K, 0);
//		for (int i = N - 1; i >= 0; --i)
//		{
//			if (used[i])
//			{
//				if (K - cnt == 1)
//				{
//					R = biggest[i][K];
//				}
//				cnt++;
//			}
//		}
		
		cout << fixed << "Case #" << t + 1 << ": " << dp(0, K, 0) << '\n';
	}

	
	fclose(stdin);
	fclose (stdout);
	
	return 0;
}

//#include <iostream>
//#include <string>
//#include <vector>
//#include <memory.h>
//#include <algorithm>
//#include <cmath>
//typedef long long LL;
//typedef double D;
//using namespace std;
//
//struct node
//{
//	int R, H;
//};
//
//node arr[1000];
//
//const int n = 1000001;
//
//D DP[n];//DP[i] - max surf of stack with smallest radius i
//
//D Q[n << 1];
//
//void add(int pos, D x)
//{
//	pos += n;
//	while (pos)
//	{
//		Q[pos] += x;
//		pos >>= 1;
//	}
//}
//
//D MAX(int L, int R)
//{
//	D res = 0;
//	for (L += n, R += n; L < R; L >>= 1, R >>= 1)
//	{
//		if (L & 1)
//			res = max(res, Q[L++]);
//		if (R & 1)
//			res = max(res, Q[--R]);
//	}
//	return res;
//}
//const D pi = acos(-1.0);
//int main()
//{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
//	
//	int T;
//	cin >> T;
//	cout.precision(20);
//	for (int t = 0; t < T; ++t)
//	{
//		int N, K;
//		cin >> N >> K;
//		for (int i = 0; i < N; ++i)
//			cin >> arr[i].R >> arr[i].H;
//		
//		sort(arr, arr + N, [](node a, node b) {return a.R >= b.R;});
//		
////		memcpy(Q + N, DP, sizeof(DP));
////		for (int i = N - 1; i > 0; --i)
////			Q[i] = Q[i << 1] + Q[i << 1 ^ 1];
//		
//		memset(Q, 0, sizeof(Q));
//		
//		for (int i = 0; i < N; ++i)
//		{
//			D val = MAX(arr[i].R, 1000001) + 2.0 * pi * arr[i].R * arr[i].H;
//			if (val > DP[arr[i].R])
//			{
//				add(arr[i].R, val - DP[arr[i].R]);
//				DP[arr[i].R] = val;
//			}
//		}
//		
//		cout << fixed << "Case #" << t + 1 << ": " << MAX(1, 1000001) << '\n';
//	}
//	
//	fclose(stdin);
//	fclose (stdout);
//	
//	return 0;
//}

//vector<int> G[1001];
//
//int W[1001][1001], MIN[1001], minv[1001];
//
//bool connected[1001][1001];
//bool used[1001];
//
//int main()
//{
////	ios_base::sync_with_stdio(0);
//	int n, m, a, b, res = 0;
//	cin >> n >> m;
//	memset(MIN, 1, sizeof(MIN));
//	for (int i = 0; i < m; ++i)
//	{
//		cin >> a >> b;
//		G[a].push_back(b);
//		G[b].push_back(a);
//		cin >> W[a][b];
//		W[b][a] = W[a][b];
//	}
//	used[1] = 1;
//	for (int i = 1; i < n; ++i)
//	{
//		int v = -1, e = 1;
//		for (int j = 1; j <= n; ++j)
//			if (!used[j] && (v == -1 || MIN[j] < MIN[v]))
//			{
//				v = j;
//				e = minv[j];
//			}
//		
//		used[v] = connected[v][e] = 1;
//		res = min(res, MIN[v]);
//		for (int to : G[v])
//			if (!used[to] && W[v][to] < MIN[to])
//			{
//				MIN[to] = W[v][to];
//				minv[to] = v;
//			}
//	}
//	cout << res << '\n';
//	cout << n - 1 << '\n';
//	
//}

//struct node
//{
//	int val;
//	char c;
//};
//
//char arr[1000];
//node cnt[6];//R, O, Y, G, B, V.
////			 0, 1, 2, 3, 4, 5.
//int n;
//
//string res;
//
//bool match(char a, char b)
//{
//	switch (a)
//	{
//		case 'R':
//			return b == 'G' || b == 'Y' || b == 'B';
//		case 'Y':
//			return b == 'V' || b == 'R' || b == 'B';
//		case 'B':
//			return b == 'O' || b == 'R' || b == 'Y';
//		case 'G':
//			return b == 'R';
//		case 'O':
//			return b == 'B';
//		case 'V':
//			return b == 'Y';
//	}
//	return 0;
//}
//
//string sub(string s, int l, int r)
//{
//	string res = "";
//	for(int i = l; i < r; ++i)
//		res += s[i];
//	return res;
//}
//
//bool check(string s)
//{
//	for (int i = 1; i < s.length(); ++i)
//		if (!match(s[i - 1], s[i]))
//			return 0;
//	return match(s[0], s[s.length() - 1]);
//}
//
//
//int main()
//{
//		freopen("input.txt", "r", stdin);
//		freopen("output.txt", "w", stdout);
//	
//	int T;
//	cin >> T;
//	for (int t = 0; t < T; ++t)
//	{
//		cin >> n;
//		for (int i = 0; i < 6; ++i)
//			cin >> cnt[i].val;
//		
//		cout << "Case #" << t + 1 << ": ";
//		//R, O, Y, G, B, V.
//		//0, 1, 2, 3, 4, 5.
//		cnt[0].c = 'R'; cnt[1].c = 'O'; cnt[2].c = 'Y'; cnt[3].c = 'G'; cnt[4].c = 'B'; cnt[5].c = 'V';
//		
//		string res;
//		
//		sort(cnt, cnt + 6, [](node a, node b){return a.val >= b.val;});
//		
//		for (int i = 0; i < cnt[0].val; ++i)
//			res += cnt[0].c;
//		
//		int i = 0;
//		
//		for (; i < cnt[1].val; ++i)
//			res = sub(res, 0, i * 2) + cnt[1].c + sub(res, i * 2, (int)res.length());
//		
//		int j = 0;
//		
//		for (; (i + j) * 2 < res.length() && j < cnt[2].val; ++j)
//			res = sub(res, 0, i * 2) + cnt[2].c + sub(res, i * 2, (int)res.length());
//		
//		if (j < cnt[2].val)
//			for (int k = 0; (j + k) < cnt[2].val; ++k)
//				res = sub(res, 0, k * 2) + cnt[2].c + sub(res, k * 2, (int)res.length());
//		
//		if (check(res))
//			cout << res << '\n';
//		else
//			cout << "IMPOSSIBLE\n";
//	}
//	
//		fclose(stdin);
//		fclose (stdout);
//	
//	return 0;
//}


//#include <iostream>
//#include <string>
//#include <vector>
//#include <memory.h>
//#include <algorithm>
//#include <cmath>
//typedef long long LL;
//typedef double D;
//using namespace std;
//
//char arr[1000];
//int cnt[6];//R, O, Y, G, B, V.
////			 0, 1, 2, 3, 4, 5.
//int n;
//
//string res;
//
//bool match(char a, char b)
//{
//	switch (a)
//	{
//		case 'R':
//			return b == 'G' || b == 'Y' || b == 'B';
//		case 'Y':
//			return b == 'V' || b == 'R' || b == 'B';
//		case 'B':
//			return b == 'O' || b == 'R' || b == 'Y';
//		case 'G':
//			return b == 'R';
//		case 'O':
//			return b == 'B';
//		case 'V':
//			return b == 'Y';
//	}
//	return 0;
//}
//
//bool f(int pos)
//{
//	if (pos == n)
//	{
//		if (match(arr[0], arr[n - 1]))
//		{
//			res = "";
//			for (int i = 0; i < n; ++i)
//				res += arr[i];
//			return 1;
//		}
//		return 0;
//	}
//	switch (arr[pos - 1])
//	{
//  			case 'R':
//		{
//			if (cnt[3])
//			{
//				cnt[3]--;
//				arr[pos] = 'G';
//				if (f(pos + 1))
//					return 1;
//				cnt[3]++;
//			}
//			if (cnt[2])
//			{
//				cnt[2]--;
//				arr[pos] = 'Y';
//				if (f(pos + 1))
//					return 1;
//				cnt[2]++;
//			}
//			if (cnt[4])
//			{
//				cnt[4]--;
//				arr[pos] = 'B';
//				if (f(pos + 1))
//					return 1;
//				cnt[4]++;
//			}
//			break;
//		}
//			
//			case 'Y':
//		{
//			if (cnt[5])
//			{
//				cnt[5]--;
//				arr[pos] = 'V';
//				if (f(pos + 1))
//					return 1;
//				cnt[5]++;
//			}
//			if (cnt[0])
//			{
//				cnt[0]--;
//				arr[pos] = 'R';
//				if (f(pos + 1))
//					return 1;
//				cnt[0]++;
//			}
//			if (cnt[4])
//			{
//				cnt[4]--;
//				arr[pos] = 'B';
//				if (f(pos + 1))
//					return 1;
//				cnt[4]++;
//			}
//			break;
//		}
//			
//			case 'B':
//		{
//			if (cnt[1])
//			{
//				cnt[1]--;
//				arr[pos] = 'O';
//				if (f(pos + 1))
//					return 1;
//				cnt[1]++;
//			}
//			
//			if (cnt[0])
//			{
//				cnt[0]--;
//				arr[pos] = 'R';
//				if (f(pos + 1))
//					return 1;
//				cnt[0]++;
//			}
//			
//			if (cnt[2])
//			{
//				cnt[2]--;
//				arr[pos] = 'Y';
//				if (f(pos + 1))
//					return 1;
//				cnt[2]++;
//			}
//			break;
//		}
//			
//			case 'G':
//		{
//			if (cnt[0])
//			{
//				cnt[0]--;
//				arr[pos] = 'R';
//				if (f(pos + 1))
//					return 1;
//				cnt[0]++;
//			}
//			break;
//		}
//			
//			case 'O':
//		{
//			if (cnt[4])
//			{
//				cnt[4]--;
//				arr[pos] = 'B';
//				if (f(pos + 1))
//					return 1;
//				cnt[4]++;
//			}
//			break;
//		}
//			
//			case 'V':
//		{
//			if (cnt[2])
//			{
//				cnt[2]--;
//				arr[pos] = 'Y';
//				if (f(pos + 1))
//					return 1;
//				cnt[2]++;
//			}
//			break;
//		}
//			
//	}
//	return 0;
//}
//
//int main()
//{
////	freopen("input.txt", "r", stdin);
////	freopen("output.txt", "w", stdout);
//	
//	int T;
//	cin >> T;
//	for (int t = 0; t < T; ++t)
//	{
//		cin >> n;
//		for (int i = 0; i < 6; ++i)
//			cin >> cnt[i];
//		
//		cout << "Case #" << t + 1 << ": ";
//		//R, O, Y, G, B, V.
//		//0, 1, 2, 3, 4, 5.
//		if (cnt[0])
//		{
//			arr[0] = 'R';
//			cnt[0]--;
//			if (f(1))
//			{
//				cout << res << '\n';
//				continue;
//			}
//			cnt[0]++;
//		}
//		
//		if (cnt[3])
//		{
//			arr[0] = 'G';
//			cnt[3]--;
//			if (f(1))
//			{
//				cout << res << '\n';
//				continue;
//			}
//			cnt[3]++;
//		}
//		
//		if (cnt[4])
//		{
//			arr[0] = 'B';
//			cnt[4]--;
//			if (f(1))
//			{
//				cout << res << '\n';
//				continue;
//			}
//			cnt[4]++;
//		}
//		
//		if (cnt[2])
//		{
//			arr[0] = 'Y';
//			cnt[2]--;
//			if (f(1))
//			{
//				cout << res << '\n';
//				continue;
//			}
//			cnt[2]++;
//		}
//		
//		if (cnt[1])
//		{
//			arr[0] = 'O';
//			cnt[1]--;
//			if (f(1))
//			{
//				cout << res << '\n';
//				continue;
//			}
//			cnt[1]++;
//		}
//		if (cnt[5])
//		{
//			arr[0] = 'V';
//			cnt[5]--;
//			if (f(1))
//			{
//				cout << res << '\n';
//				continue;
//			}
//			cnt[5]++;
//		}
//			
//		cout << "IMPOSSIBLE\n";
//	}
//	
////	fclose(stdin);
////	fclose (stdout);
//	
//	return 0;
//}

//vector<LL> primes;
//LL factorA[200], factorB[200], nxt[200];//A - B
//
//bool prime(int n)
//{
//	if (n == 2)
//		return 1;
//	if (!(n & 1) || !(n - 1))
//		return 0;
//	for (int i = 3; i * i <= n; i += 2)
//		if (!(n % i))
//			return 0;
//	return 1;
//}
//
//void convert(int n)
//{
//	for (int i = 0; n > 1 && i < primes.size(); ++i)
//		while(!(n % primes[i]))
//		{
//			nxt[i]++;
//			n /= primes[i];
//		}
//}
//
//void add(LL * b)//k nxt - b
//{
//	for (int i = 0; i < primes.size(); ++i)
//		nxt[i] += b[i];
//}
//
//const int MOD = 1e9 + 7;
//
//int cnt()
//{
//	int res = 1;
//	for (int i = 0; i < primes.size(); ++i)
//		res = ((LL)res * (nxt[i] + 1)) % MOD;
//	return res;
//}
////71348251
//int main()
//{
//	int n, p = 0;
//	cin >> n;
//	for (int i = 1; i * i <= 1000000; ++i)
//		if (prime(i))
//			primes.push_back(i);
//	
//	for (int i = 2; i <= n; ++i)
//	{
//		if (i >= 1000 && prime(i))
//		{
//			p++;
//			continue;
//		}
//		memset(nxt, 0, sizeof(primes));
//		add(factorA);
//		add(factorB);
//		convert(i);
//		memcpy(factorA, factorB, sizeof(primes));
//		memcpy(factorB, nxt, sizeof(primes));
//	}
//	
//	int res = cnt();
//	while (p)
//	{
//		res = ((LL)res * 2) % MOD;
//		p--;
//	}
//	
//	cout << res << '\n';
//}

//struct cord
//{
//	D x, y;
//};
//
//D dist(cord A, cord B)
//{
//	return sqrt((A.x - B.x) * (A.x - B.x) + (A.y - B.y) * (A.y - B.y));
//}
//
//int main()
//{
//	ios_base::sync_with_stdio(0);
//	
//	int T;
//	cin >> T;
//	for (int t = 0; t < T; ++t)
//	{
//		cord A, B, O = {0, 0};
//		D R;
//		cin >> R;
//		cin >> A.x >> A.y >> B.x >> B.y;
//		
//		if (dist(O, A) > R || dist(O, B) > R || dist(O, A) < R / sqrt(2) || dist(O, B) < R / sqrt(2))
//		{
//			cout << "NO" << '\n';
//			continue;
//		}
//		
//		
//	}
//	
//	cout << '\n';
//}

//#include <iostream>
//#include <string>
//#include <vector>
//#include <memory.h>
//#include <algorithm>
//typedef long long LL;
//typedef double D;
//using namespace std;
//
//vector<int> v;
//int cnt[2000001];
//
//bool simple(int n)
//{
//	if (n == 2)
//		return 1;
//	for (int i = 3; i * i <= n; i += 2)
//		if (!(n % i))
//			return 0;
//	return 1;
//}
//
//void f(int n)
//{
//	if (simple(n))
//		cnt[n]++;
//	else
//		for (int i = 2; i * i <= n; i++)
//		{
//			if (!(n % i))
//				cnt[i]++;
//		}
//}
//
//int main()
//{
//	ios_base::sync_with_stdio(0);
//	int n, t;
//	cin >> n;
//	for (int i = 0; i < n; ++i)
//	{
//		cin >> t;
//		v.push_back(t);
//	}
//	sort(v.begin(), v.end());
//	f(v.front());
//	
//	for (int i = 1; i < v.size(); ++i)
//	{
//		if (v[i] != v[i - 1])
//			f(v[i]);
//	}
//	int mx = 0;
//	for (int i = 2; i < 2000000; ++i)
//		if (simple(i) && cnt[i] > mx)
//			mx = cnt[i];
//	cout << mx << '\n';
//}
//
//#include <iostream>
//#include <cstdio>
//#include <cstdlib>
//#include <string>
//#include <iomanip>
//#include <vector>
//#include <algorithm>
//#include <utility>
//#include <queue>
//#include <cmath>
//
//using namespace std;
//typedef long long ll;
//
//
//ll n,m,i,j,k;
//ll p[140][150];
//
//void test()
//{
//	cin>>n;
//	i=1;j=2;
//	p[1][1]=1;
//	for(ll q=2;q<n*n;)
//	{
//		for(;i<=n && j>=1;++i,--j,++q)  p[i][j]=q;
//		if(i<=n && j<1) ++j;
//		else    {--i;j+=2;}
//		for(;i>=1 && j<=n;++j,--i,++q)  p[i][j]=q;
//		if(j<=n)++i;
//		else    {i+=2;--j;}
//	}
//	for(ll i=1;i<=n;++i)
//	{
//		for(ll j=1;j<=n;++j)
//			cout<<p[i][j]<<' ';
//		cout<<endl;
//	}
//}
//
//
//int main()
//{
//	ios_base::sync_with_stdio(0);
//	test();
//	return 0;
//}
