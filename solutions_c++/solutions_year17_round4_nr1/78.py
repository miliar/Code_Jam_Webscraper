#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

typedef int _loop_int;
#define REP(i,n) for(_loop_int i=0;i<(_loop_int)(n);++i)
#define FOR(i,a,b) for(_loop_int i=(_loop_int)(a);i<(_loop_int)(b);++i)
#define FORR(i,a,b) for(_loop_int i=(_loop_int)(b)-1;i>=(_loop_int)(a);--i)

#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define DEBUG_VEC(v) cout<<#v<<":";REP(i,v.size())cout<<" "<<v[i];cout<<endl
#define ALL(a) (a).begin(),(a).end()

#define CHMIN(a,b) a=min((a),(b))
#define CHMAX(a,b) a=max((a),(b))

// mod
const ll MOD = 1000000007ll;
#define FIX(a) ((a)%MOD+MOD)%MOD

// floating
typedef double Real;
const Real EPS = 1e-11;
#define EQ0(x) (abs(x)<EPS)
#define EQ(a,b) (abs(a-b)<EPS)
typedef complex<Real> P;

int n,p;
int a[125];

int memo3[125][125];
int memo4[125][125][125];
int calc3(int a,int b){
  if(a<0 || b<0)return -252521;
  if(a==0 && b==0)return 0;
  if(a*1 + b*2 < 3)return 1;
  if(memo3[a][b]!=-1)return memo3[a][b];
  memo3[a][b] = 0;
  REP(i,4)REP(j,4)if((i*1+j*2)%3==0)CHMAX(memo3[a][b], calc3(a-i,b-j)+1);
  return memo3[a][b];
}
int calc4(int a,int b,int c){
  if(a<0 || b<0 || c<0)return -252521;
  if(a==0 && b==0 && c==0)return 0;
  if(a*1 + b*2 + c*3 < 4)return 1;
  if(memo4[a][b][c]!=-1)return memo4[a][b][c];
  memo4[a][b][c] = 0;
  REP(i,5)REP(j,5)REP(k,5)if((i*1+j*2+k*3)%4==0)CHMAX(memo4[a][b][c], calc4(a-i,b-j,c-k)+1);
  return memo4[a][b][c];
}

void solve(){
  scanf("%d%d",&n,&p);
  REP(i,n)scanf("%d",a+i);
  if(p==2){
    int ans = 0;
    int c1 = 0;
    REP(i,n)if(a[i]%2==0){
      ans++;
    }else{
      c1++;
    }
    ans += (c1+1)/2;
    printf("%d\n",ans);
  }else if(p==3){
    int ans = 0;
    int c1 = 0;
    int c2 = 0;
    REP(i,n)if(a[i]%3==0){
      ans++;
    }else if(a[i]%3==1){
      c1++;
    }else{
      c2++;
    }
    ans += calc3(c1,c2);
    printf("%d\n",ans);
  }else if(p==4){
    int ans = 0;
    int c1 = 0;
    int c2 = 0;
    int c3 = 0;
    REP(i,n)if(a[i]%4==0){
      ans++;
    }else if(a[i]%4==1){
      c1++;
    }else if(a[i]%4==2){
      c2++;
    }else{
      c3++;
    }
    ans += calc4(c1,c2,c3);
    printf("%d\n",ans);
  }else{
    puts("HA?");
  }
}

int main(){
  REP(i,125)REP(j,125)memo3[i][j] = -1;
  REP(i,125)REP(j,125)REP(k,125)memo4[i][j][k] = -1;
  int t;
  scanf("%d",&t);
  REP(i,t){
    printf("Case #%d: ",i+1);
    solve();
  }
  return 0;
}
