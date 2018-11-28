//template.cpp
#include <bits/stdc++.h>
using namespace std;

#define lll long long int  
#define mp make_pair
#define pb push_back

#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d%d",&x,&y)
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define scl(x) scanf("%lld",&x)
#define scl2(x,y) scanf("%lld%lld",&x,&y)
#define scl3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z)
#define scstr(x) scanf("%s",x)
#define pf(x) printf("%d",x)
#define pfl(x) printf("%lld",x)
#define pfstr(x) printf("%s",x) 


#define newl() printf("\n")
#define fl(i,n) for (i=0;i<n;i++)
#define fl1(i,n) for (i=1;i<=n;i++)
#define fla(i,n,a) for (i=a;i<n;i++)
#define mem(a,i) memset(a,i,sizeof(a))

typedef pair<int,int> pii;
typedef pair<int,pair<int,int> > pipii ;
typedef pair<lll,pair<lll,lll> > plpll ;
typedef pair<lll,lll> pll;
typedef pair<lll,int> pli;
#define gcd __gcd

#define debug(x) cout<<"debug->"<<#x<<"::"<<x<<endl
#define debug2(x,y) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n"
#define debug3(x,y,z) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n"
#define debug4(x,y,z,P) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\t"<<#P<<" :: "<<P<<"\n"
#define debug5(x,y,z,P,O) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\t"<<#P<<" :: "<<P<<"\t"<<#O<<" :: "<<O<<"\n"
#define itr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)


#define MOD 1000000009
#define MAX 100001

int main()
{
  lll T, a, b, c, d, e, f, g, h, i, j, k, l, m, n, r, x, y, z, v, N, ans, sum, ret, fir, sec, left, right, num;

  int cntsolve ;
  string A;

  k = 0;
  scl(T);
  while(T--)
  {
    k++;
    cin >> A;
    cin >> a;

    cntsolve = 0;
    ans = 0;  //no. of flips
    for(i = 0; i <= A.size() - a; i++){
      // debug(i);
      if(A[i] == '-'){
        ans++;
        for(j = i; j < i + a; j++){
          if(A[j] == '+') A[j] = '-';
          else A[j] = '+';
        }
      }
    }

    for(; i < A.size(); i++)
      if(A[i] == '-')
        cntsolve = 1;

    cout << "Case #" << k << ": ";
    if(cntsolve)
      cout << "IMPOSSIBLE\n";
    else 
      cout << ans << "\n";
  }

  return 0;
}