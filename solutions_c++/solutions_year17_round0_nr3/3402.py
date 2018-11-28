#include <cstdio>
#include <queue>

using namespace std;

struct room{
  int start;
  int end;
  int mid;
};

bool operator<(room t, room u){
  if (t.mid - t.start < u.mid - u.start) return true;// min
  if (t.mid - t.start > u.mid - u.start) return false;// min
  if (t.end - t.mid < u.end - u.mid) return true;// max
  if (t.end - t.mid > u.end - u.mid) return false;// max
  return t.start < u.start;
}

int T;
int n, k;

int main() {
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);

  scanf("%d", &T);
  for(int testcase = 1; testcase <= T; testcase++) {
    priority_queue<room> pq;
    scanf("%d %d", &n, &k);

    room x;
    x.start = 1;
    x.end = n;
    x.mid = (x.start + x.end) / 2;
    pq.push(x);

    for(int i = 0; i < k - 1; i++) {
      room av = pq.top();
      pq.pop();

      room l;
      l.start = av.start;
      l.end = av.mid - 1;
      l.mid = (l.start + l.end) / 2;
      if(l.start <= n && l.end >= 1 && l.start <= l.end) pq.push(l);

      room r;
      r.start = av.mid + 1;
      r.end = av.end;
      r.mid = (r.start + r.end) / 2;
      if(r.start <= n && r.end >= 1 && r.start <= r.end) pq.push(r);
    }

    room ans = pq.top();
    printf("Case #%d: %d %d\n", testcase, ans.end - ans.mid, ans.mid - ans.start);
  }
}
