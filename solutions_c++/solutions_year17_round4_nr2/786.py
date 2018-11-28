#include <cassert>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

int const kMaxN = 1000;
int const kMaxM = 1000;

vector<int> g_adj[kMaxN];
int g_matchTo[kMaxM];
int g_color[kMaxM];

struct Order {
  int m_seat = 0;
  int m_customer = 0;
};

struct Result {
  Result() = default;
  Result(int numRides, int numPromotions)
      : m_numRides(numRides), m_numPromotions(numPromotions) {}

  int m_numRides = 0;
  int m_numPromotions = 0;
};

bool Go(int u, int color) {
  if (g_color[u] == color)
    return false;

  g_color[u] = color;
  for (int v : g_adj[u]) {
    if (g_matchTo[v] < 0 || Go(g_matchTo[v], color)) {
      g_matchTo[v] = u;
      g_matchTo[u] = v;
      return true;
    }
  }

  return false;
}

Result Solve(int n, int c, int m, vector<Order> const &orders) {
  assert(orders.size() == m);

  for (int i = 0; i < m; ++i)
    g_adj[i].clear();

  for (int i = 0; i < m; ++i) {
    for (int j = i + 1; j < m; ++j) {
      if (orders[i].m_customer == orders[j].m_customer)
        continue;
      if (orders[i].m_seat == orders[j].m_seat)
        continue;

      g_adj[i].push_back(j);
      g_adj[j].push_back(i);
    }
  }

  memset(g_matchTo, -1, sizeof(g_matchTo));
  memset(g_color, -1, sizeof(g_color));

  int numRides = 0;
  for (int i = 0; i < m; ++i) {
    if (g_matchTo[i] < 0) {
      if (Go(i, i))
        ++numRides;
    }
  }

  int numPromotions = 0;
  for (int i = 0; i < m; ++i) {
    if (g_matchTo[i] != -1)
      continue;
    for (int j = i + 1; j < m; ++j) {
      if (g_matchTo[j] != -1)
        continue;
      if (orders[i].m_customer == orders[j].m_customer)
        continue;
      assert(orders[i].m_seat == orders[j].m_seat);
      if (orders[i].m_seat != 0) {
        ++numRides;
        ++numPromotions;
        g_matchTo[i] = j;
        g_matchTo[j] = i;
        break;
      }
    }
  }

  for (int i = 0; i < m; ++i) {
    if (g_matchTo[i] == -1)
      ++numRides;
  }
  return Result(numRides, numPromotions);
}

int main() {
  int numTests;
  scanf("%d", &numTests);
  for (int testNum = 1; testNum <= numTests; ++testNum) {
    int n, c, m;
    scanf("%d%d%d", &n, &c, &m);

    vector<Order> orders(m);
    for (int i = 0; i < m; ++i) {
      scanf("%d%d", &orders[i].m_seat, &orders[i].m_customer);
      --orders[i].m_seat;
      --orders[i].m_customer;
    }

    auto const result = Solve(n, c, m, orders);
    printf("Case #%d: %d %d\n", testNum, result.m_numRides,
           result.m_numPromotions);
  }
  return 0;
}
