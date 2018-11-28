#include <stdio.h>
#include <map>
#include <queue>

using namespace std;

struct Horse {
  int dist;
  int speed;
};

int dist[200][200];
Horse horse[200];
int n;

struct dijk {
  double dist;
  int left;
  int horse;
  int town;
};

bool operator<(const dijk& a, const dijk& b) {
  return a.dist > b.dist;
}

double search(int src, int dst) {
  priority_queue<dijk> q;
  map<int, map<int, bool> > visited;

  q.push(dijk { 0., horse[src].dist, src, src });
  while (!q.empty()) {
    dijk d = q.top();
    q.pop();

    //printf("in town %d with horse %d; have travelled %lf. %d km left.\n",
    //       d.town, d.horse, d.dist, d.left);

    visited[d.town][d.horse] = true;

    if (d.town == dst) {
      return d.dist;
    }

    for (int i = 0; i < n; i++) {
      // old horse
      if (dist[d.town][i] > -1 &&
          dist[d.town][i] <= d.left &&
          !visited[i][d.horse]) {
        q.push(dijk {
               d.dist + ((double)dist[d.town][i]) / (double)horse[d.horse].speed,
               d.left - dist[d.town][i],
               d.horse,
               i
        });
      }
      // new horse
      if (dist[d.town][i] > -1
          && dist[d.town][i] <= horse[d.town].dist &&
          !visited[i][d.town]) {
        q.push(dijk {
               d.dist + ((double)dist[d.town][i]) / (double)horse[d.town].speed,
               horse[d.town].dist - dist[d.town][i],
               d.town,
               i
        });
      }
    }
  }

  return -1;
}

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    int q;
    scanf("%d%d", &n, &q);

    for (int i = 0; i < n; i++) {
      scanf("%d%d", &horse[i].dist, &horse[i].speed);
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        scanf("%d", &dist[i][j]);
      }
    }

    printf("Case #%d: ", t);

    int src, dst;
    for (int i = 0; i < q; i++) {
      scanf("%d%d", &src, &dst);
      printf(" %lf", search(src - 1, dst - 1));
    }

    printf("\n");
  }

  return 0;
}
