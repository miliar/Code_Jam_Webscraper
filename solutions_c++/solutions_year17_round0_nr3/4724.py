#include <bits/stdc++.h>

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, b) for(int x = 0; x < (b); ++x)
#define SIZE(c) ((int)c.size())
#define ALL(c) (c).begin(), (c).end()
#define MP make_pair
#define ST first
#define PB push_back
#define ND second

using namespace std;

typedef long double LD;
typedef long long LL;
typedef vector <int> VI;
typedef pair <int, int> PII;
typedef vector <PII> VPII;
typedef pair <int, PII> PIII;

const int MAXN = 1e6 + 9;

class Cmp
{
    public:
    bool operator()(const PIII& a, const PIII& b)
    {
        if(min(a.ND.ST, a.ND.ND) == min(b.ND.ST, b.ND.ND))
          {
              if(max(a.ND.ST, a.ND.ND) == max(b.ND.ST, b.ND.ND))
                {
                    return a.ST > b.ST;
                }
              
              return max(a.ND.ST, a.ND.ND) < max(b.ND.ST, b.ND.ND);
          }
        
        return min(a.ND.ST, a.ND.ND) < min(b.ND.ST, b.ND.ND);
    }
};

set <int> occup;
priority_queue <PIII, vector <PIII>, Cmp> kol;

void dodaj(int a, int b)
{
    if(b - a - 1 == 0)
      return;
    
    int mid = a + b;
    mid /= 2;
    
    kol.push(MP(mid, MP(mid - a, b - mid)));
}

int main()
{
    int n, t, k;
    int num = 0;
    PIII tmp;
    
    cin>>t;
    
    while(t--)
      {
          num++;
          occup.clear();
          
          scanf("%d %d", &n, &k);
          
          while(!kol.empty())
            kol.pop();
          
          dodaj(0, n + 1);
          
          REP(i, k - 1)
            {
                tmp = kol.top();
                kol.pop();
                
                dodaj(-tmp.ND.ST + tmp.ST, tmp.ST);
                dodaj(tmp.ST, tmp.ST + tmp.ND.ND);
            }
          
          cout<<"Case #"<<num<<": "<<max(kol.top().ND.ST - 1, kol.top().ND.ND - 1)<<" "<<min(kol.top().ND.ST - 1, kol.top().ND.ND - 1)<<endl;
      }
    
    //system("pause");
    return 0;
}
