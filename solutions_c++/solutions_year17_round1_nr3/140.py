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

ll divideup(ll a, ll b)
{
	return (a + b - 1) / b;
}

ll attacksNeeded(ll att, ll buf, ll h)
{
	ll best = divideup(h, att);
	ll crntTurns = 0;
	while (true)
	{
		++crntTurns;
		att += buf;
		ll nbest = crntTurns + divideup(h, att);
		if (nbest <= best)
		{
			best = nbest;
		}
		else
		{
			break;
		}
	}
	return best;
}

ll simulate(ll health, ll maxHealth, ll attNeeded, ll hisAttack)
{
	if (hisAttack <= 0)
	{
		return attNeeded;
	}

	ll used = 0;
	ll killTurns = divideup(health, hisAttack);
	if (attNeeded <= killTurns)
	{
		return attNeeded;
	}

	used += killTurns;
	attNeeded -= (killTurns - 1);
	health = maxHealth - hisAttack;

	killTurns = divideup(health, hisAttack);
	if (killTurns <= 1)
	{
		return -1;
	}
	ll curesNeeded = (attNeeded - 2) / (killTurns - 1);
	used += attNeeded + curesNeeded;

	return used;
}

ll solve(ll myHealth, ll myAttack, ll hisHealth, ll hisAttack, ll buff, ll debuff)
{
	ll attackTurns = attacksNeeded(myAttack, buff, hisHealth);
	ll base = 100;
	ll bound = 3 * (attackTurns + 1) + base;
	ll crntTurns = 0;
	ll debuffs = 0;
	ll best = LINF;
	ll crntHealth = myHealth;
	while (crntTurns <= bound)
	{
		ll sim = simulate(crntHealth, myHealth, attackTurns, hisAttack);
		if (sim >= 0)
		{
			best = min(best, crntTurns + sim);
		}
		if (crntHealth - (hisAttack - debuff) > 0)
		{
			hisAttack -= debuff;
			++debuffs;
		}
		else
		{
			crntHealth = myHealth;
		}
		++crntTurns;
		crntHealth -= hisAttack;
		if (crntHealth <= 0)
		{
			break;
		}
		if (crntTurns >= base && debuffs <= 10)
		{
			break;
		}
	}
	if (best == LINF)
	{
		throw 1;
	}
	else
	{
		return best;
	}
}

int main()
{
	int t;
	cin >> t;
	jk(t)
	{
		printf("Case #%d: ", k+1);
		try {
			ll a, b, c, d, e, f;
			cin >> a >> b >> c >> d >> e >> f;
			cout << solve(a, b, c, d, e, f) << endl;
		}
		catch(...)
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}
}
