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


void add(string &S, int cnt, char c)
{
  while(cnt--)
  {
    int find_split = -1;
    int n = S.size();

    for (int i = 0; find_split == -1 and i < n - 1; i++)
      if ( S[i] != c and S[i+1] != c and S[i]==S[i+1])
        find_split = i;
    if (find_split == -1 and S[0]!= c and S[n-1] != c and S[0]==S[n-1])
        find_split = n-1;

    for (int i = 0; find_split == -1 and i < n - 1; i++)
      if ( S[i] != c and S[i+1] != c)
        find_split = i;
    if (find_split == -1 and S[0]!= c and S[n-1] != c)
        find_split = n-1;
    S += c;
    if (find_split >= 0 and find_split < n-1)
    {
      for (int i = n; i > find_split+1; i--)
        S[i] = S[i-1];
      S[find_split+1] = c;
    }
  }
}

string solve(vector<pair<int,char>> A)
{
  sort(A.begin(), A.end());
  reverse(A.begin(), A.end());
  if (A[0].F > A[1].F + A[2].F) return "IMPOSSIBLE";
  string ret = "";
  for (int i = 0; i < A[0].F; i++) ret += A[0].S;
  for (int i = 1; i < A.size(); i++)
    add(ret, A[i].F, A[i].S);
  return ret;
}


int main()
{
  int t; cin >> t; int T = t; while(t--)
  {
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    vector<pair<int, char>> A = { {r, 'R'}, {y, 'Y'}, {b, 'B'}};
    string ANS = solve(A); 
    cout << "Case #" << T-t << ": " << ANS << endl;
  }
  return 0;	
}
