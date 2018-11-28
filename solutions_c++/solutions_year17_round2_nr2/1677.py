/**



   Pradip chandra karmaker
   Comilla University(6th_ICT)

*/



#include<bits/stdc++.h>
using namespace std;
#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define clr(a) memset(a,0,sizeof a)
#define neg(a) memset(a,-1,sizeof a)
#define Sort(a) sort(a.begin(),a.end())
#define All(a) a.begin(),a.end()
typedef long long i64;
typedef pair<int,int> pi;
#define mod 1000000007LL





template<class T>T Bitcnt(T a){int sum=0;while(a){if(a&1)sum++;a/=2;}return sum;}
template<class T>T Max3(T a,T b,T c){return max(a,max(b,c));}
template<class T>T Lcm(T a,T b){T tmp=__gcd(a,b);return (a/tmp)*b;}
template<class T> T Pow(T a,T b){T ans=1;T base=a;while(b){if(b&1)ans=(ans*base);base=(base*base);b/=2;}return ans;}
i64 Bigmod(i64 a,i64 b)
{
    i64 res=1;
    i64 pw=a%mod;
    while(b>0)
    {
       if(b&1)res=(res*pw)%mod;
       pw=(pw*pw)%mod;
       b/=2;
    }
    return res;
}


#define s1(a) scanf("%d",&a)
#define s2(a,b) scanf("%d %d",&a,&b)
#define s3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define sl1(a) scanf("%lld",&a)
#define sl2(a,b) scanf("%lld %lld",&a,&b)
#define sl3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define p1(a) printf("%d",a)
#define p2(a,b) printf("%d %d",&a,&b)
#define NL printf("\n")
#define N 4000000
#define rep(i,a,b)    for(int i=a;i<=b;i++)
#define rrep(i,b,a)   for(int i=b;i>=a;i--)
#define fs(i,a,s)     for(int i=a;s[i];i++)

int a_x[]={1,-1,0,0};
int a_y[]={0,0,1,-1};
i64 X,Y;

void extend_euclid(i64 a,i64 b)
{
    if(b==0)
    {
        X=1;Y=0;return;
    }
    extend_euclid(b,a%b);
    i64 x,y;
    x=Y;
    y=X-(a/b)*Y;
    X=x;
    Y=y;
}
i64 inverse_modulo(i64 a,i64 b)
{
    extend_euclid(a,b);
    return (X+mod)%mod;
}

/** dijkstra,bitmask,ME,scc,backtracking,grid dp,segment tree,bit,LCA,bfs,dfs,BPM,MAX_FLOW,MCM,Tree dp,kmp,MST,Meet in the middle*/

/**Triangle characteristics,Phi,bitwise_seive,SOD,articulation,topological,HLD,Z,knapsack,Coin,Digit,LIS,LCS,minimum vertex
cover,josephus,chinese remainder,square root decomposition,ternary search,binary search,Number of theory(divisor,prime),chinese remainder,Generic functoin,Convex hull*/

/*************************************************************************************************************************************************************************************************/

  int arr[1005];
  int col[10];
int main()
{

    freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);


   int test;
   scanf("%d",&test);
   char res[]={'C','R', 'O', 'Y', 'G', 'B', 'V'};
   for(int ca=1;ca<=test;ca++)
   {
       int n;
       int tot;
       scanf("%d",&tot);
       for(int j=1;j<=6;j++)
        scanf("%d",&col[j]);
        int pos=0;
        int poss=1;
        memset(arr,0,sizeof arr);
         while(pos<tot)
       {
            int i;
            int mx=0;
            for(int j=1;j<=6;j++){
                    if(col[j]>mx){mx=col[j];i=j;}
            }
             //cout<<i<<endl;

          while(col[i])
         {

               if(pos==0)arr[pos++]=i,col[i]--;
               else if(arr[pos-1]!=i){arr[pos++]=i;col[i]--;}

               if(pos==tot)break;
              int yes=0;
              int now;
             for(int j=1;j<=6;j++){

                 if(i==j)continue;

                 if(col[j]>yes){yes=col[j];now=j;}

             }
             if(yes==0)poss=0;
              if(poss==0)break;
              col[now]--;
              arr[pos++]=now;
         }
         if(poss==0)break;
       }
         for(int i=0;i<tot;i++)
         {
             if(arr[i]==arr[(i+1)%tot])poss=0;
         }

       if(poss==0)printf("Case #%d: IMPOSSIBLE\n",ca);
       else
       {
           printf("Case #%d: ",ca);
           for(int i=0;i<tot;i++)
            printf("%c",res[arr[i]]);
           puts("");

       }
   }
}
