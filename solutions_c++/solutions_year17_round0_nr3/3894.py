#include<cstdio>
#include<queue>
using namespace std;

struct S
{
  long long N;
  long long L;
  long long R;

  S(long long n, long long l, long long r) : N(n), L(l), R(r)
  {
  }

  bool operator<(const struct S& other) const
  {
    if (N != other.N) return N < other.N;
    if (L != other.L) return L < other.L;
    if (R != other.R) return R < other.R;
    return false; //< They are equal
  }
};

priority_queue<S> q;

int main()
{
  int T;
  scanf("%d", &T);
  for(int t=1; t<=T; t++) {
    priority_queue<S> empty;
    swap( q, empty );
    long long L, R, K, N, M;
    scanf("%lld %lld", &N, &K);
    q.push(S(N, 0, N+1));
    while(!q.empty() && --K) {
      struct S s = q.top(); q.pop();
      L = s.L; N = s.N; R = s.R;
      M = L+(N+2)/2;
      /* printf("%d: %d--%d--%d\n", K+1, L, M, R); */
      q.push(S((M-L)-1, L, M));
      q.push(S((R-M)-1, M, R));
    }
    struct S s = q.top(); q.pop();
    L = s.L; N = s.N; R = s.R;
    M = L+(N+2)/2;
    /* printf("%d: %d--%d--%d\n", K+1, L, M, R); */
    printf("Case #%d: %lld %lld\n", t, M-L-1, R-M-1);
  }
}
