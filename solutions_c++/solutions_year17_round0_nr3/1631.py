#include<bits/stdc++.h>
#define x first
#define y second
using namespace std;
typedef long long LL;
typedef long double LD;
const LL LLinf=9e18+5;
const int MOD=1e9 + 7;
const LD pi = acos(-1.0L);
const int NMAX = 100000+69;
const int INF = 0x3f3f3f3f;

int T;
LL n,k;
LL rsl, rsr;

void rec(LL a, LL sza, LL b, LL szb){
    if(k<=sza){
      rsl = a/2;
      rsr = (a+1)/2 - 1;
      return;
    }
    else
    {
      k-=sza;
      if(k<=szb){
        rsl = b/2;
        rsr = (b+1)/2 - 1;
        return;
      }
      k-=szb;
    }
    LL na = a/2;
    LL nb = (a/2)-1;
    LL szna = 0; 
    LL sznb = 0;
    if(a/2 == na)
      szna+=sza;
    if((a+1)/2 - 1== na)
      szna+=sza;
    if(a/2 == nb)
      sznb+=sza;
    if((a+1)/2 - 1== nb)
      sznb+=sza;

    if(b/2 == na)
      szna+=szb;
    if((b+1)/2 - 1== na)
      szna+=szb;
    if(b/2 == nb)
      sznb+=szb;
    if((b+1)/2 - 1== nb)
      sznb+=szb;

    rec(na, szna, nb, sznb);
}

void solve(){
  cin>>T;
  for(int tt=1; tt<=T; tt++){
    cout<<"Case #"<<tt<<": ";
    cin>>n>>k;
    rec(n, 1, n, 0);
    cout<<rsl<<" "<<rsr<<"\n";
  }
}

int main()
{
  cout<<setprecision(6)<<fixed;
	ios_base::sync_with_stdio(0);
	cin.tie(0);


  solve();
	 
	return 0;
}
