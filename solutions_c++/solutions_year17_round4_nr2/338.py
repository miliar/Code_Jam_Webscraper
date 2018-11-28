#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

const int N_MAX = 2000;
const int C_MAX = 2000;
const int M_MAX = 2000;
int N, C, M; // N seats, C customer ids, M tickets
int buyers[M_MAX];
int seats[M_MAX];

int cust_tickets[C_MAX][N_MAX];
int num_tickets[C_MAX];

void init() {
  cin >> N >> C >> M;
  for (int i = 0; i < C_MAX; i++)
    for (int j = 0; j < N_MAX; j++)
      cust_tickets[i][j] = 0;
  for (int i = 0; i < C_MAX; i++)
    num_tickets[i] = 0;

  for (int i = 0; i < M; i++) {
    cin >> seats[i] >> buyers[i];
    buyers[i]--;
    seats[i]--;

    num_tickets[buyers[i]]++;
    cust_tickets[buyers[i]][seats[i]]++;
  }
}

int get_cost(int k) {
  for (int i = 0; i < C; i++) {
    if (num_tickets[i] > k)
      return -1;
  }

  int cost = 0;
  int free = 0;
  for (int i = 0; i < N; i++) {
    int ct = 0;
    for (int c = 0; c < C; c++)
      ct += cust_tickets[c][i];

    if (ct > k + free) {
      return -1;
    } else if (ct > k) {
      cost += ct - k;
      free -= ct - k;
    } else {
      free += k - ct;
    }
  }
  return cost;
}

void solve_case(int t) {
  init();

  int min_rides = 1;
  int max_rides = M; // is doable
  while (min_rides < max_rides) {
    int mid = (max_rides + min_rides) / 2;
    if (get_cost(mid) == -1) {
      min_rides = mid + 1;
    } else {
      max_rides = mid;
    }
  }

  int cost = get_cost(min_rides);
  assert(cost != -1);
  cout << "Case #" << t << ": " << min_rides << " " << cost << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
