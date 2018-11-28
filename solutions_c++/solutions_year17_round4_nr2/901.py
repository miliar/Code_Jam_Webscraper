#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

const int MAXN = 1010, MAXM = 1010, MAXC = 1010, d = 0;

int T, N, C, M, seat[MAXM], person[MAXM];
// N = seats
// C = customers
// M = tickets

int rides_per_customer[MAXC];
vector<int> want_seat[MAXN]; // want_seat[i] = customers who want seat i

/*
keep track of number of leftover seats
keep track of number of rides being used
for each seat:
  find all customers who want that seat
  increase the number of rides you need based on # of such customers, and also # of such customers who are already riding in some seat from earlier
  update leftover seats accordingly
*/
int next_rides_per_customer[MAXC];

int main() {
  scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    if (d) cout << endl;
    if (d) cout << "CASE " << t << endl;

    scanf("%d %d %d", &N, &C, &M);
    for (int i = 1; i <= C; ++i) {
      rides_per_customer[i] = 0;
    }
    for (int i = 1; i <= N; ++i) {
      want_seat[i].clear();
    }

    for (int i = 0; i < M; ++i) {
      scanf("%d %d", &seat[i], &person[i]);
      want_seat[seat[i]].push_back(person[i]);
    }

    int leftover_seats = 0;
    int rides = 0;
    int promotions = 0;
    for (int seat = 1; seat <= N; ++seat) {
      if (d) cout << "starting with seat " << seat << "; leftover_seats = " << leftover_seats << "; rides = " << rides << "; promotions = " << promotions << endl;
      sort(want_seat[seat].begin(), want_seat[seat].end());
     
      while (true) {
        if (d) cout << "will " << rides << " rides be enough?" << endl;
        bool enough = true;
        // Is there enough space for everyone?
        int count = 0;
        int use_from_leftover = 0;
        int cur_seat_remaining = rides;
        for (int i = 1; i <= C; ++i) {
          next_rides_per_customer[i] = 0;
        }
        for (int i = 0; i < want_seat[seat].size(); ++i) {
          count++;
          if (i == want_seat[seat].size() - 1 || want_seat[seat][i] != want_seat[seat][i + 1]) {
            int pers = want_seat[seat][i];

            if (d) cout << "person " << pers << " wants seat " << seat << " with freq " << count << endl;

            if (rides_per_customer[pers] + count > rides) {
              enough = false;
              if (d) cout << "not enough; this customer wants " << (rides_per_customer[pers] + count) << " rides but we only have " << rides << endl;
              break;
            }

            next_rides_per_customer[pers] = count;

            int use_current_seat = min(cur_seat_remaining, count);
            cur_seat_remaining -= use_current_seat;
            int excess = count - use_current_seat;
            use_from_leftover += excess;
            if (use_from_leftover > leftover_seats) {
              enough = false;
              break;
            }

            count = 0;
          }
        }

        if (enough) {
          promotions += use_from_leftover;
          leftover_seats = cur_seat_remaining + leftover_seats - use_from_leftover;
          for (int i = 1; i <= C; ++i) {
            rides_per_customer[i] += next_rides_per_customer[i];
          }
          break;
        }
        rides++;
        leftover_seats += seat - 1;
      }
    }

    printf("Case #%d: %d %d\n", t, rides, promotions);
  }

  return 0;
}
