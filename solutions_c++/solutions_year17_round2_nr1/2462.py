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
	D k, s;
};

node arr[1000];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		D d;
		int n;
		cin >> d >> n;
		for (int i = 0; i < n; ++i)
			cin >> arr[i].k >> arr[i].s;
		
		sort(arr, arr + n, [](node a, node b) {return a.k < b.k;});
		D time = 0;
		for (int i = 0; i < n; ++i)
			time = max(time, (d - arr[i].k) / arr[i].s);
		
		cout.precision(20);
		cout << "Case #" << t + 1 << ": ";
		cout << fixed << d / time << '\n';
	}
	
	fclose(stdin);
	fclose (stdout);
	
	return 0;
}

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
