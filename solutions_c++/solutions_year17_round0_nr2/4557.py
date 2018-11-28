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

const LL INF = 1e9;
const LL MAX = INF * INF;

bool sprawdz(LL a)
{
    int ost = 9;
    
    while(a > 0)
      {
         if(a % 10 > ost)
           return false;
         
         ost = a % 10;
         a /= 10;
      }
    
    return true;
}

int main()
{
    int t, num = 0;
    LL n;
    
    cin>>t;
    
    while(t--)
      {
          num++;
          
          scanf("%lld", &n);
          
          if(sprawdz(n))
            {
                cout<<"Case #"<<num<<": "<<n<<endl;
                continue;
            }
          
          LL pot = 1, pot2;
          LL tmp2;
          LL wyn = 0;
          
          while(pot <= n)
            {
                LL tmp = n;
                
                tmp2 = n / pot;
                tmp2 %= 10;
                
                if(tmp2 == 0)
                  {
                      if(pot == MAX)
                        break;
                      
                      pot *= 10;
                      continue;
                  }
                
                tmp -= tmp2 * pot;
                tmp += (tmp2 - 1) * pot;
                
                pot2 = 1;
                
                while(pot2 < pot)
                  {
                      tmp2 = n / pot2;
                      tmp2 %= 10;
                      
                      tmp -= tmp2 * pot2;
                      tmp += 9 * pot2;
                      
                      pot2 *= 10;
                  }
                
                if(sprawdz(tmp))
                  wyn = max(wyn, tmp);
                
                if(pot == MAX)
                  break;
                
                pot *= 10;
            }
          
          cout<<"Case #"<<num<<": "<<wyn<<endl;
      }
    
    //system("pause");
    return 0;
}
