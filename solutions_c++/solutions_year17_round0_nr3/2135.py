#include<bits/stdc++.h>
using namespace std;

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
  cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
  const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

#define si(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define pi(x) printf("%d\n",x)
#define F first
#define S second
#define PB push_back
#define MP make_pair

typedef long long LL;
typedef pair<LL,LL> PLL;
typedef map<LL,LL> MLL;

LL can_accomodate(MLL & A)
{
  LL ret = 0;
  MLL B;
  for (auto p : A)
    if (p.F > 0 and p.S > 0)
    {
      ret += p.S;
      B.insert(p);
    }
  A = B;
  return ret;
}

void accomomdate(MLL & A, LL & k)
{
  k -= can_accomodate(A);
  MLL B;
  for (auto p : A)
  {
    LL X = p.F - 1;
    LL x = X / 2;
    if (x > 0) B[x] += p.S;
    x = X - x;
    if (x > 0) B[x] += p.S;
  }
  assert(B.size() < 3);
  A = B;
}


int main()
{
  int t; cin >> t; int T = t; while(t--)
  {
    LL n, k; 
    cin >> n >> k;
    MLL A;
    A[n] = 1;
    while (k > can_accomodate(A))
      accomomdate(A, k);
    vector<PLL> B(A.begin(), A.end());
    reverse(B.begin(), B.end());
    for (auto b : B)
      if (b.S < k)
      {
        k -= b.S;
      }
      else
      {
        LL X = b.F - 1;
        cout << "Case #"<<T-t<<": " << X - (X/2) << " " << X/2 << endl;
        break;
      }
  }
  return 0;	
}
