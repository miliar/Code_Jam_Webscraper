#include<bits/stdc++.h>
//#include<windows.h>

#define nl              cout<<"\n"
#define sz(x)           (int)((x).size())
#define len(x)          (x).length()
#define all(a)          (a).begin(),(a).end()
#define rep(i,n)        for( int i=0;i<(int)(n);i++)
#define brep(i,n)       for( int i=(n);i>=0;i-- )
#define repp(i,a,b)     for( int i = (a); i < (b); i++ )
#define ll      long long int
#define pb      push_back
#define mp      make_pair
#define F       first
#define S       second
#define vi      vector<int>
#define vll     vector<ll>
#define pii     pair<int,int>
#define vpii    vector<pair<int,int> >
#define bits    __builtin_popcountll
#define mod     1000000007
#define test int tes; cin >> tes; while( tes-- > 0 )
#define fast ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;
ll a,b,x,y,m,t,p,q;
int k,n,tt;
string s;
int A[100001];

ll maanam(int *a, int M, int N) {
  ll sa[M]; 
  rep(i,M) sa[i] = 0;
  ll sum=0, ans=0;
  rep(i,M)
  {
    sa[i] = (a[i]+sum)%2 != 1;
    sum += sa[i] - ( i >= N-1 ? sa[i-N+1] : 0 );
    ans += sa[i];
    if(i>M-N and sa[i]!=0) return -1;
  }
  return ans;
}

int main() {
 freopen("A-large.in","r",stdin);
 freopen("op.txt","w",stdout);
  cin>>tt;
  for(int i=1;i<=tt;i++)
  {
  	cin>>s>>k;
  	n = len(s);
  	rep(i,n)
  		A[i] = (s[i]=='+');
  	long long int ans = maanam(A, n, k);
	if(ans == -1)
		cout<<"Case #"<<i<<": "<<"IMPOSSIBLE",nl;
    else
		cout<<"Case #"<<i<<": "<<ans,nl;
 }
}
