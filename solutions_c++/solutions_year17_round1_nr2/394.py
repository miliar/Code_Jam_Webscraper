#include <iostream>
#include <cstring>
#include <utility>
#include <vector>

typedef std::pair<int, int> ii;

std::vector<ii> pack[51];
int need[51];

bool can(int i, int temp, int got)
{
	//std::cout << need[i] * got * 0.9 << ", " << temp << ", " << need[i] * got * 1.1 << '\n';
	bool ans = need[i] * got * 9LL <= 10LL * temp && 10LL * temp <= need[i] * got * 11LL;
	//std::cout << need[i] * got * 9LL << ", " << 10LL * temp << '\n';
	//std::cout << 10LL * temp << ", " << need[i] * got * 11LL << '\n';
	//std::cout << ans << '\n';
	return ans;
}

const int mv = 2020, me = 50*50*50*10;
const int INF = 100000;
const int src = mv - 1, sink = mv - 2;

int to[me], ant[me], cap[me], z;
int adj[mv], copy_adj[mv], fila[mv], level[mv];

int a[mv], b[mv];
int ans[mv][mv];

inline void add(int a, int b, int c)
{
	//std::cout << "adding edge between " << a << ", " << b << '\n';
	ant[z] = adj[a], to[z] = b, cap[z] = c, adj[a] = z++;
	std::swap(a, b);
	ant[z] = adj[a], to[z] = b, cap[z] = 0, adj[a] = z++;
}

int bfs()
{
	memset(level, -1, sizeof level);
	level[src] = 0;
	int front = 0, size = 0;
	fila[size++] = src;
	while(front < size)
	{
		int v = fila[front++];
		for(int i = adj[v]; i != -1; i = ant[i])
		{
			if(cap[i] && level[to[i]] == -1)
			{
				level[to[i]] = level[v] + 1;
				fila[size++] = to[i];
			}
		}
	}
	return level[sink] != -1;
}

int dfs(int v, int flow)
{
	if(v == sink)
		return flow;
	int f;
	for(int &i = copy_adj[v]; i!=-1; i = ant[i])
	{
		if(cap[i] && level[to[i]] == level[v]+1 && (f = dfs(to[i], std::min(flow, cap[i]))))
		{
			cap[i] -= f, cap[i^1] += f;
			return f;
		}
	}
	return 0;
}

int maxflow(){
	int ret = 0, flow;
	while(bfs())
	{
		memcpy(copy_adj, adj, sizeof adj);
		while((flow = dfs(src, 1 << 30)))
		{
			ret += flow;
		}
	}
	return ret;
}

void init()
{
	memset(adj, -1, sizeof adj);
	z = 0;
}

int main()
{
	int t;
	std::cin >> t;
	for(int te = 1; te <= t; te++)
	{
		int n, p;
		std::cin >> n >> p;
		for(int i = 0; i < n; i++)
			std::cin >> need[i];
		for(int i = 0; i < n; i++)
		{
			pack[i].clear();
			for(int j = 0; j < p; j++)
			{
				int temp;
				std::cin >> temp;
				//std::cout << "on (" << i << ", " << temp << ")\n";
				pack[i].push_back(ii(0, 0));
				int l, r;
				l = 0, r = temp / need[i];
				while(l != r)
				{
					int mid = (l + r) / 2;
					if(can(i, temp, mid))
						r = mid;
					else
						l = mid + 1;
				}
				r = int(1e6) + 10;
				if(!can(i, temp, l))
					l++;
				pack[i].back().first = l;
				r = int(1e6) + 10;
				while(l != r)
				{
					int mid = (l + r + 1) / 2;
					//long long cur = (long long)need[i] * mid * 10LL;
					if(can(i, temp, mid))
						l = mid;
					else
						r = mid - 1;
				}
				pack[i].back().second = l;
				if(pack[i].back().first == pack[i].back().second && !can(i, temp, l))
					pack[i].back() = ii(0, 0);
				//std::cout << "got " << pack[i].back().first << ", " << pack[i].back().second << '\n';
				//std::cout << "bound is (" << need[i] * pack[i].back().first * 9 << ", " << 10 * temp << ", " << need[i] * pack[i].back().second * 11 << ")\n";
			}	
		}
		init();
		for(int i = 0; i < n - 1; i++)
		{
			for(int j = 0; j < p; j++)
			{
				for(int k = 0; k < p; k++)
				{
					if(pack[i][j].second < pack[i + 1][k].first || pack[i][j].first > pack[i + 1][k].second)
						continue;
					add(i * p + j, (i + 1) * p + k, 1);
				}
			}
		}
		for(int i = 0; i < p; i++)
		{
			if(pack[0][i].first != 0)
				add(src, i, 1);
			if(pack[n - 1][i].first != 0)
				add((n - 1) * p + i, sink, 1);
		}
		std::cout << "Case #" << te << ": " << maxflow() << '\n';
	}
}