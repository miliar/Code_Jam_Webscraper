

#if 1
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <array>
#include <deque>
#include <algorithm>
#include <utility>
#include <cstdint>
#include <functional>
#include <iomanip>
#include <numeric>
#include <assert.h>

auto& in = std::cin;
auto& out = std::cout;

int32_t N;
int32_t E[10000];
int32_t S[10000];
int32_t DIST[100][100];
int64_t total_D[100];
double dp[100][100];
double func(int i, int use)
{
	if (i == N-1) {
		return 0;
	}
	if (dp[i][use]!=0.0) {
		return dp[i][use];
	}
	dp[i][use] = func(i + 1, i) + DIST[i][i + 1] / (double)S[i];
	if (E[use] >= (total_D[i + 1] - total_D[use])) {
		dp[i][use] = std::min(
			dp[i][use],
			func(i + 1, use) + DIST[i][i + 1] / (double)S[use]
		);
	}
	return dp[i][use];
}

template<typename T>
void fill_all(T& arr, const T& v) {
	arr = v;
}
template<typename T, typename ARR>
void fill_all(ARR& arr, const T& v) {
	for (auto& i : arr) { fill_all(i, v); }
}

int main()
{
	using std::endl;
	in.sync_with_stdio(false);
	out.sync_with_stdio(false);

	int TEST_CASE;
	in >> TEST_CASE;
	for (int32_t loop = 0; loop < TEST_CASE; ++loop)
	{
		out << "Case #" << loop + 1 << ": ";


		fill_all(dp, 0.0);
		int Q;
		in >> N>>Q;
		for (int32_t i = 0; i < N; ++i)
		{
			in >> E[i] >> S[i];
		}
		for (int32_t i = 0; i < N; ++i)for (int32_t j = 0; j < N; ++j)
		{
			in >> DIST[i][j];
		}
		for (int32_t i = 1; i < N; ++i)
		{
			total_D[i] = DIST[i-1][i];
			total_D[i] += total_D[i - 1];
		}
		for (int32_t i = 0; i < Q; ++i)
		{
			int u, v;
			in >> u >> v; --u; --v;
		}

		out << std::fixed << std::setprecision(50) << func(0, 0) << endl;
	}

	return 0;
}
#endif


#if 0
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <array>
#include <deque>
#include <algorithm>
#include <utility>
#include <cstdint>
#include <functional>
#include <iomanip>
#include <numeric>
#include <assert.h>

auto& in = std::cin;
auto& out = std::cout;


#include <queue>
#include <vector>
#include <functional>
#include <utility>
#include <algorithm>
#include <iterator>

using COST_T = uint32_t;
constexpr uint32_t N_MAX = 100;
constexpr COST_T INF = 1000 * 1000 * 1000 + 1000;//std::numeric_limits<double>::infinity()

#if defined(_MSC_VER) && defined(_DEBUG)
static_assert(false, "リリースでコンパイルしないと遅いよ！！");
#endif

struct edge {
	uint32_t to;
	COST_T cost;
	edge() {}
	edge(uint32_t to_, COST_T cost_)
		:to(to_), cost(cost_) {}
};
std::vector<edge> graph[N_MAX];//場所

//ダイクストラ
COST_T DIST_FROM_TO[N_MAX][N_MAX];
void Dijkstra1(uint32_t s)
{
	auto& Dist = DIST_FROM_TO;
	using P = std::pair<COST_T, uint32_t>;//cost pos
	std::priority_queue<P, std::vector<P>, std::greater<>> que;
	std::fill(std::begin(Dist), std::end(Dist), INF);

	Dist[s][s] = 0;
	que.emplace(0, s);
	while (!que.empty())
	{
		auto p = que.top(); que.pop();
		const auto& nowpos = p.second;
		const auto& nowcost = p.first;
		if (Dist[s][nowpos] < nowcost) { continue; }

		//for (int32_t to = 0; to < N; ++to)
		//{
		//	auto cost = nowcost + graph[nowpos][to];
		//	if (cost < D[to]) {
		//		D[to] = cost;
		//		que.emplace(D[to], to);
		//	}
		//}

		for (const auto& e : graph[nowpos])
		{
			auto cost = nowcost + e.cost;
			if (cost < Dist[s][e.to]) {
				Dist[s][e.to] = cost;
				que.emplace(cost, e.to);
			}
		}

	}
}
void Dijkstr2(uint32_t s)
{
	using P = std::pair<COST_T, uint32_t>;//cost pos
	std::priority_queue<P, std::vector<P>, std::greater<>> que;
	std::fill(std::begin(D), std::end(D), INF);

	D[s] = 0;
	que.emplace(0, s);
	while (!que.empty())
	{
		auto p = que.top(); que.pop();
		const auto& nowpos = p.second;
		const auto& nowcost = p.first;
		if (D[nowpos] < nowcost) { continue; }

		//for (int32_t to = 0; to < N; ++to)
		//{
		//	auto cost = nowcost + graph[nowpos][to];
		//	if (cost < D[to]) {
		//		D[to] = cost;
		//		que.emplace(D[to], to);
		//	}
		//}

		for (const auto& e : graph[nowpos])
		{
			auto cost = nowcost + e.cost;
			if (cost < D[e.to]) {
				D[e.to] = cost;
				que.emplace(cost, e.to);
			}
		}

	}
}


int32_t N;

int main()
{
	using std::endl;
	in.sync_with_stdio(false);
	out.sync_with_stdio(false);

	int Q;
	in >> Q;
	for (int32_t loop = 0; loop < Q; ++loop)
	{
		out << "Case #" << loop + 1 << ": ";

		in >> N;

		for (int32_t i = 0; i < N; ++i)
		{
			Dijkstra1(i);
		}
	}

	return 0;
}
#endif

#if 0
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <array>
#include <deque>
#include <algorithm>
#include <utility>
#include <cstdint>
#include <functional>
#include <iomanip>
#include <numeric>
#include <assert.h>

auto& in = std::cin;
auto& out = std::cout;

int32_t N;
int32_t R, O, Y, G, B, V;

template<typename T>
void fill_all(T& arr, const T& v) {
	arr = v;
}
template<typename T, typename ARR>
void fill_all(ARR& arr, const T& v) {
	for (auto& i : arr) { fill_all(i, v); }
}
char first;
std::string dp[6][1000];
std::string func(int bef, int N)
{
	if (!dp[bef][N].empty()) {
		return dp[bef][N];
	}
	if(bef == )
}
int main()
{
	using std::endl;
	in.sync_with_stdio(false);
	out.sync_with_stdio(false);

	int Q;
	in >> Q;
	for (int32_t loop = 0; loop < Q; ++loop)
	{
		out << "Case #" << loop + 1 << ": ";

		in >> N;
		in >> R>> O>> Y>> G>> B>> V;
		for (auto& arr : dp)for (auto& i : arr) { i.clear(); }
		if (R) { first = 0; }
		else if (Y) { first = 2; }
		else { first = 4; }
#if 1
		char RES[1024] = {};
		if ((R>(N / 2)) || (Y>(N / 2)) || (B>(N / 2)) || (O+1>B) || (G+1>R) || (V+1>Y)) {
			out << "IMPOSSIBLE\n"; continue;
		}
		for (int32_t i = 0; i < N; ++i)
		{

		}
#endif
#if 0
		if ((R>(N / 2)) || (Y>(N / 2)) || (B>(N / 2))) {
			out << "IMPOSSIBLE";
		}
		else {
			char RES[1024] = {};
			for (int32_t i = 0; i < R; ++i)
			{
				RES[i * 2] = 'R';
			}
			int32_t y = 0;
			for (; y < Y;)
			{
				auto n = (N - 1)&(~1);
				if (RES[n - (y * 2)] != 'R') {
					RES[n - (y * 2)] = 'Y';
					++y;
				}
				else {
					break;
				}
			}
			for (int32_t i = 0; y < Y&& i < N; ++i)
			{
				if (RES[i] == 0) {
					RES[i] = 'Y';
					++y;
				}
			}
			for (int32_t i = 0; i < N; ++i)
			{
				if (RES[i] == 0) {
					RES[i] = 'B';
				}
			}
			out << RES;
		}
#endif

		out << std::endl;
	}

	return 0;
}
#endif

#if 0
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <array>
#include <deque>
#include <algorithm>
#include <utility>
#include <cstdint>
#include <functional>
#include <iomanip>
#include <numeric>
#include <assert.h>

auto& in = std::cin;
auto& out = std::cout;

int32_t D,N;
int32_t a[100000];
int main()
{
	using std::endl;
	in.sync_with_stdio(false);
	out.sync_with_stdio(false);
	out << std::fixed << std::setprecision(9);

	int Q;
	in >> Q;
	for (int32_t loop = 0; loop < Q; ++loop)
	{
		in >>D>> N;
		long double max_speed = 1000000000000000.0;
		for (int32_t i = 0; i < N; ++i)
		{
			int64_t pos, speed;
			in >> pos >> speed;
			max_speed = std::min<long double>(max_speed, speed + (speed*pos) / (long double)(D - pos));
		}
		out << "Case #" << loop + 1 << ": ";
		out << max_speed;
		out << std::endl;
	}

	return 0;
}
#endif
