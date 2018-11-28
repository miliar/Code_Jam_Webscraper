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

const int MAXN = 1e3 + 9;

char s[MAXN];
bitset <MAXN> cake, cake2;

int main()
{
    int n, t, k;
    int num = 0, wyn, wyn2;
    
    cin>>t;
    
    while(t--)
      {
          num++;
          wyn = wyn2 = 0;
          
          scanf("%s %d", s, &k);
          
          cake.reset();
          cake.flip();
          
          n = 0;
          while(s[n]) n++;
          
          REP(i, n)
            {
                if(s[i] == '+')
                  cake[i] = 1;
                
                else
                  cake[i] = 0;
            }
          
          cake2 = cake;
          
          int wsk = 0;
          
          while(cake.count() != MAXN)
            {
                if(wsk + k - 1 >= n)
                  break;
                
                if(cake[wsk] == 0)
                  {
                      wyn++;
                      
                      FOR(i, wsk, wsk + k - 1)
                        cake.flip(i);
                  }
                
                wsk++;
            }
          
          if(cake.count() != MAXN)
            wyn = MAXN;
          
          wsk = n - 1;
          
          while(cake2.count() != MAXN)
            {
                if(wsk - k + 1 < 0)
                  break;
                
                if(cake2[wsk] == 0)
                  {
                      wyn2++;
                      
                      FORD(i, wsk, wsk - k + 1)
                        cake2.flip(i);
                  }
                
                wsk--;
            }
          
          if(cake2.count() != MAXN)
            wyn2 = MAXN;
          
          wyn = min(wyn, wyn2);
          
          if(wyn == MAXN)
            printf("Case #%d: IMPOSSIBLE\n", num);
          
          else
            printf("Case #%d: %d\n", num, wyn);
      }
    
    //system("pause");
    return 0;
}
