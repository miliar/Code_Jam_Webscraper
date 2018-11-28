/*
       _ _              ___ _____ ___   __   
__   _(_) | ____ _ ___ / _ \___  / _ \ / /_  
\ \ / / | |/ / _` / __| | | | / / | | | '_ \ 
 \ V /| |   < (_| \__ \ |_| |/ /| |_| | (_) |
  \_/ |_|_|\_\__,_|___/\___//_/  \___/ \___/ 
                                             
 VIKAS SINGH */
    
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
#define FILEINOUT               freopen("A-large.in","r",stdin);freopen("output.out","w",stdout);
#define FAST_IN_OUT             ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

using namespace std;


int main(){
    FILEINOUT 
    FAST_IN_OUT
    int t;
    cin>>t;
    for (int ii = 1; ii <=t ; ++ii)
    {
        int n,k;
        string s;
        cin>>s>>k;
        n=s.length();
        int ans=0;
        for (int i = 0; i <=n-k; ++i)
        {
           if(s[i]=='-'){
              for (int j = i; j < i+k; ++j)
              {
                 if(s[j]=='-'){
                  s[j]='+';
                 }else{
                  s[j]='-';
                 }
              }
              ans++;
           }
        }
        bool is=false;
        for (int i = 0; i < n; ++i)
        {
          if(s[i]=='-'){
            is=true;
          }
        }
        if(is){
          cout<<"Case #"<<ii<<": IMPOSSIBLE\n";
        }else
        cout<<"Case #"<<ii<<": "<<ans<<endl;
    }
}