#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

const int infinity = 1e9 + 9;

int sgn(int x) {
  return (0 < x) - (x < 0);
}
int abs(int x) {
  return x * sgn(x);
}

int AC, AJ;
vector< pair<int, int> > events;

int main()
{
  int T;
  scanf("%d ", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    scanf(" %d %d", &AC, &AJ);
    events.clear();
    for (int i = 0; i < AC; ++i) {
      int C, D;
      scanf(" %d %d", &C, &D);
      events.push_back( make_pair(C, +(D-C)) );
    }
    for (int i = 0; i < AJ; ++i) {
      int J, K;
      scanf(" %d %d", &J, &K);
      events.push_back( make_pair(J, -(K-J)) );
    }

    // sort events
    sort(events.begin(), events.end());

    // initialize segments
    int fixed_Cameron = 0;
    int fixed_Jamie = 0;
    vector<int> between_Cameron;
    vector<int> between_Jamie;

    // accumulate segments
    pair<int, int> last_event = events[AC + AJ - 1];
    int last_start = last_event.first;
    int last_end = last_start + abs(last_event.second) - 24*60;
    int last_sgn = sgn(last_event.second);

    int num_transitions = 0;
    for (int i = 0; i < AC + AJ; ++i) {
      int start = events[i].first;
      int duration = abs(events[i].second);
      int sign = sgn(events[i].second);
      if (sign == +1) { // Cameron is busy
        fixed_Jamie += duration;
        if (last_sgn == sign) // Camberon was busy, between Jamie
          between_Jamie.push_back(start - last_end);
        else // Jamie was busy, transition
          num_transitions++;
      }
      if (sign == -1) { // Jamie is busy
        fixed_Cameron += duration;
        if (last_sgn == sign) // Jamie was busy, between Cameron
          between_Cameron.push_back(start - last_end);
        else // Cameron was busy, transition
          num_transitions++;
      }

      last_sgn = sign;
      last_end = start + duration;
    }

    // count additional transitions
    sort(between_Cameron.begin(), between_Cameron.end());
    sort(between_Jamie.begin(), between_Jamie.end());
    
    int sum = fixed_Cameron;
    int i = 0;
    while ((i < between_Cameron.size()) && (sum + between_Cameron[i] <= 720)) {
      sum += between_Cameron[i];
      i++;
    }
    num_transitions += 2 * (between_Cameron.size() - i);
    
    sum = fixed_Jamie;
    i = 0;
    while ((i < between_Jamie.size()) && (sum + between_Jamie[i] <= 720)) {
      sum += between_Jamie[i];
      i++;
    }
    num_transitions += 2 * (between_Jamie.size() - i);

    // output
    printf("Case #%d: %d\n", Ti, num_transitions);
  }
  return 0;
}
