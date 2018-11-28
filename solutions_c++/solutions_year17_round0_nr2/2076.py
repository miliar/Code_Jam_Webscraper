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

int main()
{
  int t; cin >> t; int T = t; while(t--)
  {
    string a; cin >> a; 
    int n = a.size();
    int i = 1; 
    while(i<n)
    {
      if (a[i] < a[i-1])
        break;
      i++;
    }
    if (i != n)
    {
      int j = i - 1;
      while(j > 0 and a[j] == a[j-1]) j--;
      a[j]--;
      for (int k = j+1; k < n; k++) a[k] = '9';
    }
    while(a.size() > 1 and a[0] == '0'){ /*cout << a << "|" << a.substr(1) << endl;*/ a = a.substr(1);}
    cout << "Case #"<<T-t<<": " << a << endl;
  }
  return 0;	
}
