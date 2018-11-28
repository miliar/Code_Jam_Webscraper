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

class Solve2SAT
{
	int N;
	vector<vector<int>> edges;
	vector<int> componentID;
	vector<int> orderNum;
	stack<int> S;
	stack<int> P;
	int counter;
	int nextComponentID;
	vector<vector<int>> components;
	vector<int> ans;

	void dfs(int x)
	{
		assert(orderNum[x] < 0);
		orderNum[x] = counter++;
		S.push(orderNum[x]);
		P.push(x);

		foreach(o, edges[x])
		{
			if (orderNum[o] < 0)
				dfs(o);
			else if (componentID[o] < 0)
			{
				while (S.top() > orderNum[o])
					S.pop();
			}
		}
		if (S.top() == orderNum[x])
		{
			int id = componentID[x] = nextComponentID++;
			vector<int> crntComp;
			S.pop();
			while (P.top() != x)
			{
				componentID[P.top()] = id;
				crntComp.push_back(P.top());
				P.pop();
			}
			crntComp.push_back(x);
			components.push_back(crntComp);
			P.pop();
		}
	}

public:

	Solve2SAT(int n) : N(n * 2), edges(n * 2)
	{}

	void AddImplication(int a, int b)
	{
		edges[a].push_back(b);
	}

	// a OR b
	void AddCondition(int a, int b)
	{
		AddImplication(a ^ 1, b); // a OR b therefore NOT a implies b
		AddImplication(b ^ 1, a); // a OR b therefore NOT b implies a
	}

	void setAns(int x, int v)
	{
		if (ans[x] >= 0) assert(ans[x] == v);
		ans[x] = v;
	}

	vector<int> findAssignment()
	{
		componentID = orderNum = vector<int>(N, -1);
		counter = nextComponentID = 0;
		ji(N) if (componentID[i] < 0)
			dfs(i);
		ji(N / 2)
			if (componentID[i * 2] == componentID[i * 2 + 1])
				return {};
		ans = vector<int>(N, -1);
		foreach(C, components)
		{
			bool anyFalse = false;
			foreach(v, C) anyFalse |= ans[v] == 0;
			int val = anyFalse ? 0 : 1;
			foreach(v, C)
			{
				setAns(v,     val);
				setAns(v ^ 1, val ^ 1);
			}
		}
		vector<int> realAns(N / 2);
		ji(N / 2) realAns[i] = ans[i * 2];
		return realAns;
	}
};

char transition[256][256];
int dr[256];
int dc[256];
int packIdx[256];

void dfs(const vector<vector<char>>& grid, vector<vector<vector<char>>>& seen, set<PII>& result, int r, int c, char d)
{
	bool first = true;
	while (true)
	{
		if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size())
		{
			return;
		}
		if (seen[r][c][packIdx[d]])
		{
			return;
		}
		seen[r][c][packIdx[d]] = true;
		if (grid[r][c] == '.')
		{
			result.insert({r, c});
		}
		if (grid[r][c] == '-' || grid[r][c] == '|')
		{
			if (!first)
			{
				throw 1;
			}
		}
		if (grid[r][c] == '#')
		{
			return;
		}
		if (grid[r][c] == '/' || grid[r][c] == '\\')
		{
			d = transition[d][grid[r][c]];
		}
		r += dr[d];
		c += dc[d];
		first = false;
	}
}

pair<set<PII>, bool> flood_fill(const vector<vector<char>>& grid, int startr, int startc, char d1, char d2)
{
	int r = grid.size();
	int c = grid[0].size();

	auto seen = make2d(r, c, vector<char>(4));
	set<PII> result;
	try {
		dfs(grid, seen, result, startr, startc, d1);
		dfs(grid, seen, result, startr, startc, d2);
	} catch (...) {
		return make_pair(set<PII>(), false);
	}
	return make_pair(result, true);
}

int encode(PII x)
{
	return (x.first*2+x.second)^1;
}

ostream& operator << (ostream& o, PII x)
{
	return o << x.first << ',' << x.second;
}

void solve(vector<vector<char>> grid)
{
	int r = grid.size();
	int c = grid[0].size();

	auto deps = make2d<vector<pair<int, int>>>(r, c);
	vector<pair<int, int>> must;
	vector<pair<int, int>> beamPosns;
	jij(r, c)
	{
		if (grid[i][j] == '-' || grid[i][j] == '|')
		{
			int idx = beamPosns.size();
			beamPosns.emplace_back(i, j);
			auto a = flood_fill(grid, i, j, '<', '>');
			auto b = flood_fill(grid, i, j, '^', 'v');
			if (!a.second && !b.second)
			{
				cerr << "Beam hits something in both directions" << endl;
				throw 1;
			}
			if (!b.second)
			{
				must.emplace_back(idx, 0);
			}
			if (!a.second)
			{
				must.emplace_back(idx, 1);
			}
			if (a.second)
			{
				for (auto pt : a.first)
				{
					deps[pt.first][pt.second].emplace_back(idx, 0);
				}
			}
			if (b.second)
			{
				for (auto pt : b.first)
				{
					deps[pt.first][pt.second].emplace_back(idx, 1);
				}
			}
		}
	}
	int vars = beamPosns.size();
	Solve2SAT algo(vars);
	jij(r, c)
	{
		if (grid[i][j] == '.')
		{
			if (deps[i][j].empty())
			{
				cerr << "Cell can't be covered" << endl;
				throw 1;
			}
			assert(deps[i][j].size() <= 2);
			// cerr << "Condition: " << deps[i][j][0] << ' ' << deps[i][j].back() << endl;
			int a = encode(deps[i][j][0]);
			int b = encode(deps[i][j].back());
			algo.AddCondition(a, b);
		}
	}
	for (auto pr : must)
	{
		// cerr << "Must[" << pr << "]\n";
		int x = encode(pr);
		algo.AddCondition(x, x);
	}
	auto assign = algo.findAssignment();
	if (assign.empty())
	{
		cerr << "No satisfying assignment" << endl;
		throw 1;
	}
	ji(assign.size())
	{
		// cerr << assign[i];
		auto pt = beamPosns[i];
		char& c = grid[pt.first][pt.second];
		assert(assign[i] == 0 || assign[i] == 1);
		c = "-|"[assign[i]];
	}
	// cerr << endl;
	printf("POSSIBLE\n");
	ji(r)
	{
		jj(c)
		{
			putchar(grid[i][j]);
		}
		putchar('\n');
	}
}

int main()
{
	dc['<'] = -1;
	dc['>'] = 1;
	dr['^'] = -1;
	dr['v'] = 1;

	packIdx['>'] = 0;
	packIdx['^'] = 1;
	packIdx['<'] = 2;
	packIdx['v'] = 3;

	transition['>']['/'] = '^';
	transition['^']['/'] = '>';
	transition['<']['/'] = 'v';
	transition['v']['/'] = '<';

	transition['>']['\\'] = 'v';
	transition['^']['\\'] = '<';
	transition['<']['\\'] = '^';
	transition['v']['\\'] = '>';

	int t;
	rint(t);
	for (int k = 1; k <= t; k++)
	{
		int r, c;
		rint(r);
		rint(c);
		auto grid = make2d<char>(r, c);
		ji(r)
		{
			string s;
			cin >> s;
			jj(c)
			{
				grid[i][j] = s[j];
			}
			assert(s.length() == c);
		}
		printf("Case #%d: ", k);
		try {
			solve(grid);
		} catch (...) {
			printf("IMPOSSIBLE\n");
		}
	}
}