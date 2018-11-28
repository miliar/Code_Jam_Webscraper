#include <bits/stdc++.h>
using namespace std;

#define jjs(i, s, x) for (int i = (s); i < int(x); ++i)
#define jjl(i, x) jjs(i, 0, x)
#define ji(x) jjl(i, x)
#define jj(x) jjl(j, x)
#define jk(x) jjl(k, x)
#define jij(a, b) ji(a) jj(b)
#define jij2d(v) jij((v).size(), (v)[i].size())
#define jjdescent(i, s, e) for (int i = (s)-1; i >= int(e); --i)
#define jjrev(i, s) jjdescent(i, s, 0)
#define foreach(x, C) for (auto& x : (C))
#define INF ((int) 1e9+10)
#define LINF ((long long) 1e16)
#define pb push_back
#define mp make_pair

#define rint readInteger
template<typename T>
bool readInteger(T& x)
{
	char c, r = 0, n = 0;
	x = 0;
	while (true)
	{
		c = getchar();
		if (c < 0 && !r)
			return 0;
		else if (c == '-' && !r)
			n = 1;
		else if (c >= '0' && c <= '9')
			x = x * 10 + c - '0', r = 1;
		else if (r)
			break;
	}
	if (n)
		x = -x;
	return 1;
}

template<typename T>
vector<T> readIntegral(int n)
{
	vector<T> ret(n);
	for (int i = 0; i < n; i++)
		readInteger(ret[i]);
	return ret;
}

auto readInts = readIntegral<int>;
auto readLongs = readIntegral<long long>;

template<typename T>
vector<vector<T>> make2d(size_t r, size_t c)
{
	return vector<vector<T>>(r, vector<T>(c));
}

template<typename T>
vector<vector<T>> make2d(size_t r, size_t c, const T& def)
{
	return vector<vector<T>>(r, vector<T>(c, def));
}

template <typename T, T MOD>
struct ModInt
{
	T value;
	ModInt() : value(0)
	{}
	ModInt(T x)
	{
		x %= MOD;
		if (x < 0)
			x += MOD;
		value = x;
	}

public:
	ModInt& operator += (ModInt x)
	{
		value += x.value;
		if (value >= MOD)
			value -= MOD;
		return *this;
	}
	ModInt& operator -= (ModInt x)
	{
		value -= x.value;
		if (value < 0)
			value += MOD;
		return *this;
	}
	ModInt& operator *= (ModInt x)
	{
		value *= x.value;
		value %= MOD;
		return *this;
	}
	ModInt& operator /= (ModInt x)
	{
		x.invert();
		return *this *= x;
	}

	ModInt operator + (ModInt x) const
	{
		ModInt o = *this;
		o += x;
		return o;
	}
	ModInt operator - (ModInt x) const
	{
		ModInt o = *this;
		o -= x;
		return o;
	}
	ModInt operator * (ModInt x) const
	{
		ModInt o = *this;
		o *= x;
		return o;
	}
	ModInt operator / (ModInt x) const
	{
		ModInt o = *this;
		o /= x;
		return o;
	}
	bool operator == (ModInt x) const
	{
		return value == x.value;
	}
	bool operator != (ModInt x) const
	{
		return !(*this == x);
	}

	ModInt operator - () const
	{
		return ModInt(0) - *this;
	}

	ModInt operator ^ (long long x) const
	{
		ModInt ret = 1 % MOD;
		ModInt mul = *this;
		while (x)
		{
			if (x & 1)
				ret *= mul;
			mul *= mul;
			x >>= 1;
		}
		return ret;
	}
	ModInt& operator ^= (long long x)
	{
		return *this = *this ^ x;
	}

private:
	void invert()
	{
		*this ^= MOD-2;
	}
public:
	friend ostream& operator << (ostream& out, const ModInt& x)
	{
		return out << x.value;
	}
};

template<typename T>
using v2d = vector<vector<T>>;

typedef ModInt<long long, 1000000007> mint;
typedef long long ll;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef v2d<int> VVI;
typedef vector<ll> VLL;
typedef v2d<ll> VVLL;
typedef vector<char> VCH;
typedef v2d<char> VVCH;

int main()
{
	int t;
	rint(t);
	for (int k = 1; k <= t; k++)
	{
		int n, p;
		rint(n);
		rint(p);
		VI g(n);
		ji(n) rint(g[i]);
		ji(n) g[i] %= p;
		VI cnt(p);
		ji(n) ++cnt[g[i]];
		int ans = 0;
		ans += cnt[0];
		if (p == 4)
		{
			int z = min(cnt[1], cnt[3]);
			ans += z;
			cnt[1] -= z;
			cnt[3] -= z;
			int y = cnt[2] / 2;
			ans += y;
			cnt[2] -= y*2;
			int crem = 0;
			while (true)
			{
				int take = -1;
				if (cnt[2] > 0)
				{
					take = 2;
				}
				else if (cnt[1] > 0)
				{
					take = 1;
				}
				else if (cnt[3] > 0)
				{
					take = 3;
				}
				if (take == -1)
				{
					break;
				}
				if (crem == 0)
				{
					++ans;
				}
				--cnt[take];
				crem += take;
				crem %= p;
			}
		}
		else if (p == 3)
		{
			int z = min(cnt[1], cnt[2]);
			ans += z;
			cnt[1] -= z;
			cnt[2] -= z;
			int crem = 0;
			while (true)
			{
				int take = -1;
				if (cnt[2] > 0)
				{
					take = 2;
				}
				else if (cnt[1] > 0)
				{
					take = 1;
				}
				if (take == -1)
				{
					break;
				}
				if (crem == 0)
				{
					++ans;
				}
				--cnt[take];
				crem += take;
				crem %= p;
			}
		}
		else
		{
			assert(p==2);
			ans += (cnt[1]+1)/2;
		}
		printf("Case #%d: %d\n", k, ans);
	}
}
