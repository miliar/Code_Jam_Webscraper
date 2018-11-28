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

ll n,i,j,k,y,x,z,t,mod,m,flag,ans,lo,md,hi,l,r,ans1,ans2 ;
ll inf = 10000000000000 ;
ll a[200000],b[200000];
vector<pair<char,ll> >v[20000]   ;
map<ll,ll> m1  ;
string s[2000] ;

int main(){
    ioS ;
freopen("input.txt","r",stdin) ;
freopen("output.txt","w",stdout) ;

cin >> t ;
for(int zz=1;zz<=t;zz++){
cin >> n >> m ;
for(i=0;i<n;i++){
    cin >> s[i] ;v[i].clear() ;
}

for(i=0;i<n;i++){
    for(j=0;j<m;j++){
        if(s[i][j]!='?'){v[i].pb(mp(s[i][j],j)) ;}
    }
}

int done = 0 ;
char c ;
for(i=0;i<n;i++){ int ds=v[i].size() ; //cout << i << " " << ds << "gege\n" ;
    for(j=0;j<ds;j++){
        c=v[i][j].ff ;
        for(k=(v[i][j].ss-1);k>=0;k--){
            if(s[i][k]=='?'){s[i][k]=c;}
            else{break;}
        }
        for(k=(v[i][j].ss+1);k<m;k++){
             if(s[i][k]=='?'){s[i][k]=c;}
            else{break;}
        }

    }
    if(ds>0){
    for(j=done;j<i;j++){
        for(k=0;k<m;k++){
         if(s[j][k]=='?')   s[j][k]=s[i][k] ;
        }
    }
    done=i+1;
    }
}

if(done<=(n-1)){
    for(j=done;j<n;j++){
        for(k=0;k<m;k++){
          if(s[j][k]=='?')  s[j][k]=s[done-1][k] ;
        }
    }
}

cout << "Case #" << zz << ":\n" ;
for(i=0;i<n;i++){
    cout <<s[i] << endl ;
}

}
}
