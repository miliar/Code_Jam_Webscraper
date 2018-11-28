#include<bits/stdc++.h>
using namespace std;
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define pri(x) printf("%d\n", x)
#define mp make_pair
#define pb push_back
#define BUFF ios::sync_with_stdio(false);
#define imprime(v) for(int X=0;X<v.size();X++) printf("%d ", v[X]); printf("\n");
#define endl "\n"
const int INF= 0x3f3f3f3f;
const long double pi= acos(-1);
typedef long long int ll;
typedef long double ld;
typedef pair<int,ll> ii;
typedef vector<int> vi;
typedef vector< vector< int > > vvi;
const int MOD=1e9+7;
const ll LINF=0x3f3f3f3f3f3f3f3f;

ll get_max(ll interv)
{
  return interv/2LL;
}

ll get_min(ll interv)//1->0, 2->0, 3->1, 4->1, 5->2
{
  return (interv-1LL)/2LL;
}

void solve()
{
  map<ll,ll> intervs;
  ll n;
  ll k;
  cin>>n>>k;
  ll kk=k;
  k--;
  intervs[n]=1;
  while(k>0)
  {
    auto it=intervs.rbegin();
    ll sz=it->first;
    ll qte=it->second;
    if(qte<=k)
    {
      intervs.erase(sz);
      intervs[get_max(sz)]+=qte;
      intervs[get_min(sz)]+=qte;
    }
    k-=qte;
  }
  assert(!intervs.empty());
  auto it=intervs.rbegin();
  cout<<get_max(it->first)<<" "<<get_min(it->first)<<endl;
}

int main()
{
  int tc;
  cin>>tc;
  for(int t=1;t<=tc;t++)
  {
    cout<<"Case #"<<t<<": ";
    solve();
  }
  return 0;
}
