#include<bits/stdc++.h>
#define ll long long int
#define ite iterator
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define ioS ios::sync_with_stdio(false);
#define re0 return 0;
using namespace std ;

ll n,i,j,k,y,x,q,z,t,mod,m,flag,ans,lo,md,hi,l,r ;
ll inf = 10000000000000 ;

vector<ll>v  ;
ll a[3000]  ;
map<ll,ll> m1  ;
map<ll,ll>::iterator itr,itr1 ;
int f(string s,int k){
n=s.size() ;
for(i=0;i<=n+k;i++){a[i]=0;}
x = 0 ;
flag=1;ans =0 ;
for(i=0;i<n;i++){ x+=a[i] ;
        if(s[i]=='-'){
         if(x%2!=1){
            if((i+k)>n){flag=0;}
            else{a[i+k]-=1;x++;ans++;}
         }
        }
        else{
            if(x%2==1){
               if((i+k)>n){flag=0;}
            else{a[i+k]-=1;x++;ans++;}
            }
        }
}
if(flag){return ans;}
return -1;
}
int main(){
    ioS ;
        freopen("input.txt","r",stdin) ;
          freopen("output.txt","w",stdout) ;
       cin >> t ;
for(int ss=1;ss<=t;ss++){
 string s1  ; int k1 ;
cin >> s1 >> k1  ;

int ans1 = f(s1,k1);
reverse(s1.begin(),s1.end()) ;
int ans2 = f(s1,k1) ;
if(ans1>ans2){swap(ans1,ans2);}
if(ans1!=-1){ans=ans1;}
else{ans=ans2 ;}
cout << "Case #" << ss << ": " ;
if(ans==-1){cout << "IMPOSSIBLE\n" ;}
else{cout << ans << endl ;}

}

}
