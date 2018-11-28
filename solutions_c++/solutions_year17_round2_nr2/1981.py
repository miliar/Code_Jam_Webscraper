/*
       _ _              ___ _____ ___   __   
__   _(_) | ____ _ ___ / _ \___  / _ \ / /_  
\ \ / / | |/ / _` / __| | | | / / | | | '_ \ 
 \ V /| |   < (_| \__ \ |_| |/ /| |_| | (_) |
  \_/ |_|_|\_\__,_|___/\___//_/  \___/ \___/ 
                                             
The following code is copied from https://google.com/find-it-yourself */
    
#include<bits/stdc++.h>
#define endl '\n'
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef std::vector<int> vi;
typedef std::vector<long long> vl;
#define all(v) v.begin(),v.end()
#define maxall(v) *max_element(all(v))
#define minall(v) *min_element(all(v))
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define min4(a,b,c,d) min(min(a,b),min(c,d))
#define max4(a,b,c,d) max(max(a,b),max(c,d))
#define f(a,b,c)                for(int a=b;a<c;a++)
#define s(x)                    scanf("%d",&x);
#define sl(x)                   scanf("%lld",&x);
#define s1d(a,n)                for(int ix=0;ix<n;ix++) cin>>a[ix];
#define p(x)                    printf("%d\n",x);
#define pl(x)                   printf("%lld\n",x);
#define p1d(a,n)                for(int ix=0;ix<n;ix++) printf("%d ",a[ix]); printf("\n");
#define p2d(a,n,m)              for(int ix=0;ix<n;ix++){ for(int jx=0;jx<m;jx++) printf("%d ",a[ix][jx]); printf("\n");}
#define MAX 1000005
#define MOD 1000000007
#define MAX_INT 2147483647
#define MAX_LONG 9223372036854775807LL
#define PI 3.14159265358979323846264338327950288
#define FILEINOUT               freopen("large1.in","r",stdin);freopen("output.out","w",stdout);
#define FAST_IN_OUT             ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

using namespace std;

int main(){
    FILEINOUT 
    FAST_IN_OUT
    
    int t;
    cin>>t;
    for(int j=0;j<t;j++) {

        int n,r,o,y,g,b,v;
        cin>>n>>r>>o>>y>>g>>b>>v;

        string s="";
        if(r>0){
          s="R";
          r--;
          n--;
        }else if(o>0){
          s="O";
          o--;
          n--;
        }else if(y>0){
          s="Y";
          y--;
          n--;
        }else if(g>0){
          s="G";
          g--;
          n--;
        }else if(b>0){
          s="B";
          b--;
          n--;
        }else if(v>0){
          s="V";
          v--;
          n--;
        }
        int i=1;
        bool flag=false;
        while(n){
           if(s[i-1]=='R'){
              if(y>0){
                y--;
                s+="Y";
                n--;
              }else if(g>0){
                g--;
                n--;
                s+="G";
              }else if(b>0){
                b--;
                n--;
                s+="B";
              }else{
                flag=true;
              }
           }else
           if(s[i-1]=='O'){
              if(v>0){
                v--;
                s+="V";
                n--;
              }else if(g>0){
                g--;
                n--;
                s+="G";
              }else if(b>0){
                b--;
                n--;
                s+="B";
              }else{
                flag=true;
              }
           }else
           if(s[i-1]=='Y'){
              if(r>0){
                r--;
                s+="R";
                n--;
              }else if(v>0){
                v--;
                n--;
                s+="V";
              }else if(b>0){
                b--;
                n--;
                s+="B";
              }else{
                flag=true;
              }
           }else
           if(s[i-1]=='G'){
              if(r>0){
                r--;
                s+="R";
                n--;
              }else if(v>0){
                v--;
                v--;
                s+="V";
              }else if(o>0){
                o--;
                n--;
                s+="O";
              }else{
                flag=true;
              }
           }else
           if(s[i-1]=='B'){
              if(y>0){
                y--;
                s+="Y";
                n--;
              }else if(r>0){
                r--;
                n--;
                s+="R";
              }else if(o>0){
                o--;
                n--;
                s+="O";
              }else{
                flag=true;
              }
           }else
           if(s[i-1]=='V'){
              if(y>0){
                y--;
                s+="Y";
                n--;
              }else if(g>0){
                g--;
                n--;
                s+="G";
              }else if(o>0){
                o--;
                n--;
                s+="O";
              }else{
                flag=true;
              }
           }
           if(flag) break;
           i++;
        }
        if(flag){
         cout<<"Case #"<<j+1<<": IMPOSSIBLE\n";  
        }else
        cout<<"Case #"<<j+1<<": "<<s<<endl;
    }
}