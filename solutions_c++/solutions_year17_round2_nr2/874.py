#include <cstdio>
#include <cstring>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

typedef pair<int, int> PII;

char colors[] = {'R', 'Y', 'B', 'G', 'V', 'O'};

void solve() {
  int N, R, O, Y, G, B, V;
  scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

  int pos[] = {R, Y, B};
  int neg[] = {G, V, O};

  for (int i = 0; i < 3; i++) {
    if (neg[i] > pos[i]) {
      printf("IMPOSSIBLE\n");
      return;
    }
    pos[i] -= neg[i];
  }

  for (int i = 0; i < 3; i++) {
    if (pos[i] == 0 && neg[i] > 0) {
      if (N != 2*neg[i]) {
        printf("IMPOSSIBLE\n");
        return;
      }
      // Only two complementary colors, same count.
      for (int j = 0; j < neg[i]; j++) {
        printf("%c%c", colors[i], colors[3+i]);
      }
      printf("\n");
      return;
    }
  }

  vector<PII> ord;
  for (int i = 0; i < 3; i++) ord.push_back(make_pair(pos[i], i));
  sort(ord.begin(), ord.end());

  // for (int i = 0; i < 3; i++) {
  //   printf("%d ", ord[i].first);
  // }
  // printf("\n");

  int extra2 = pos[ord[2].second] - pos[ord[1].second];
  if (extra2 > pos[ord[0].second]) {
    printf("IMPOSSIBLE\n");
    return;
  }

  vector<int> preans;
  int extra_left = extra2;
  for (int i = 0; i < pos[ord[0].second]; i++) {
    preans.push_back(ord[0].second);
    if (extra_left) {
      preans.push_back(ord[2].second);
      extra_left--;
    }
    preans.push_back(ord[1].second);
    preans.push_back(ord[2].second);
  }

  int middle_left = pos[ord[1].second] - pos[ord[0].second];
  for (int i = 0; i < middle_left; i++) {
    preans.push_back(ord[1].second);
    preans.push_back(ord[2].second);
  }

  // Compose answer.

  vector<bool> neg_done;
  for (int i = 0; i < 3; i++) {
    neg_done.push_back(neg[i] == 0);
  }

  int check = 0;
  for (int i = 0; i < (int)preans.size(); i++) {
    printf("%c", colors[preans[i]]);
    check++;
    if (!neg_done[preans[i]]) {
      for (int j = 0; j < neg[preans[i]]; j++) {
        printf("%c%c", colors[3+preans[i]], colors[preans[i]]);
        check += 2;
      }
      neg_done[preans[i]] = true;
    }
  }
  printf("\n");

  if (check != N) {
    printf("Daco plano!!!\n");
  }
}

int main() {
    int T;
    scanf("%d ", &T);
    for (int t = 0; t < T; t++) {
      printf("Case #%d: ", t+1);
      solve();
    }
}