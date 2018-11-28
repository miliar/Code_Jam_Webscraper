#include<bits/stdc++.h>
#define ll long long int
#define ite iterator
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define ioS ios::sync_with_stdio(false);
#define re0 return 0;
#define pii pair<ll,ll>
using namespace std ;

ll n,i,j,k,y,x,z,t,mod,m,flag,lo,md,hi,l,r,ans1,ans2 ;
ll inf = 10000000000000 ;
ll a[200000];
double ans ;
vector<ll>v,b   ;
map<ll,map<ll,ll> > m1  ;
 bool prime[1000002];
string s ;
map<ll,ll>m2;
map<ll,map<ll,ll> >::iterator itr,itr1 ;
map<ll,ll>::iterator itr3,itr4 ;
vector<ll>::iterator itr5,itr6,itr7 ;ll d;
int main(){
    ioS ;
    freopen("input.txt","r",stdin) ;
    freopen("output.txt","w",stdout) ;
    cin >> t ;
for(int zz=1;zz<=t;zz++){
cin >> d >> n ;
ans =10000000000000.0;
for(i=0;i<n;i++){
    cin >> x >> y ;
   // cout << x << " " << y << " " ;
   // cout <<(1.0*d*y)/(1.0*(d-x)) << endl ;
    if((1.0*d*y)/(1.0*(d-x))<=ans)ans=(1.0*d*y)/(1.0*(d-x));
}
printf("Case #%d: %0.9f\n",zz,ans) ;
}
}
