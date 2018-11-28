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

bool istidy(int a){
  int k;
  do{
    k = a % 10;
    a /= 10;
    if(a%10 > k) return false;
  }while(a > 0);
  return true;
}

int ans_(int a){
  int m = 1;
  for(int i = 1; i <= a; i++){
    if(istidy(i)) m = max(m, i);
  }
  return m;
}

void recleft(string &S, int a){
  if(a < 1) return;
  
  if(S[a] < S[a-1]){
    //make the current one 9
    //decrease the previous one
    S[a] = '9';
    S[a-1]--;
    
  }
  else if(S[a - 1] == '0'){
    //make the current one 9
    S[a] = '9';
  }

  recleft(S, a-1);
}

int main()
{
  lll T, a, b, c, d, e, f, g, h, i, j, k, l, m, n, r, x, y, z, v, N, ans, sum, ret, fir, sec, left, right, num;
  long long int A[MAX], B[MAX], C[MAX], D[MAX], L[MAX], R[MAX];

  string S, AN;


  // return 0;

  scl(T);
  b = 0;

  while(T--)
  {



  // for(d = 1; d < 3000; d++){
    // cout << "N: " << a << " ans: " << ans_(a) << endl;  
  
    b++;
    cin >> S;
    // cin >> d;
    // stringstream ss;
    // ss << d;
    // S = ss.str();

    for(a = 0; a < S.size() - 1; a++){
      if(S[a] > S[a + 1]){
        recleft(S, a+1);  
        for(c = a + 2; c < S.size(); c++){  
          S[c] = '9';
        }
        break;
      }
    }    

    if(S[0] == '0')
      AN = S.substr(1);
    else 
      AN = S;

    // stringstream rr(AN);
    // rr >> e;

    // if(e != ans_(d)){
    //   debug3(e, ans_(d), d);
    // }
    // cout << AN << " " << ans_(d) << endl;
    cout << "Case #" << b << ": " << AN << endl;
  }
  // }


  return 0;
}