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

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;

void process(string & s, int i, int k)
{
  while(k--)
  {
    if (s[i] == '-') s[i] = '+';
    else s[i] = '-';
    i++;
  }
}

int main()
{
  int test;
  cin >> test;
  int TEST = test;
  while (test--)
  {
    string s; int k; 
    cin >> s >> k ;
    int n = s.size();
    int ans = 0;
    for (int i = 0; i <= n - k; i++)
      if (s[i] == '-')
      {
        process(s, i, k);
        ans++;
      }
    bool done = true;
    for (int i = 0; i < n; i++)
      if (s[i] == '-')
      {
        done = false;
        break;
      }
    cout << "Case #" << TEST - test << ": ";
    if (done)
    {
      cout << ans << endl;
    }
    else
    {
      cout << "IMPOSSIBLE" << endl;
    }

  }
  return 0;	
}
