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
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;


int main()
{
  int t; cin >> t; int T = t; while(t--)
  {
    int D; cin >> D;
    int n; cin >> n;

    double max_time = 0;

    while (n--)
    {
      int d, s; 
      cin >> d >> s; d = D - d;
      max_time = max(max_time, (double)d / s);
    }
    cout << "Case #" << T-t << ": ";
    printf("%.7lf\n",(double)D / max_time );
  }
  return 0;	
}
