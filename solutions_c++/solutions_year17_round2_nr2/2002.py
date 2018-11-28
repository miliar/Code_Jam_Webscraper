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
vector<char>s ;
map<ll,ll>m2;
pair<ll,char>p[300000] ;
int main(){
    ioS ;
    freopen("input.txt","r",stdin) ;
    freopen("output.txt","w",stdout) ;
    cin >> t ;
for(int zz=1;zz<=t;zz++){

cin >> n;  string sd = "ROYGBV" ; s.clear() ;

for(i=0;i<6;i++){
    cin >> p[i].ff ;
p[i].ss=sd[i];}

 flag=1;
 sort(p,p+6) ;x=5 ;
 for(i=0;i<n;i++){s.pb('A') ;}
 for(i=0;i<n;){
    if(p[x].ff>0&&x>=0){
        s[i]=p[x].ss;  p[x].ff--;
    }
    else if(p[x].ff==0){x--;i-=2;}
    i+=2;
 }
  for(i=1;i<n;){
    if(p[x].ff>0&&x>=0){
        s[i]=p[x].ss;  p[x].ff--;
    }
    else if(p[x].ff==0){x--;i-=2;}
    i+=2;
 }
 for(i=0;i<n;i++){
    if(s[i]==s[(i+1)%n]){flag=0;}
 }
    //for(i=0;i<n;i++){cout << s[i] ;}
cout << "Case #" << zz << ": " ;
 if(flag){
    for(i=0;i<n;i++){cout << s[i] ;}cout << endl ;
 }
 else{
    cout << "IMPOSSIBLE\n" ;
 }

}
}
