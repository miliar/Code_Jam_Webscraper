//--------------**************---------------------
/* 
 #        "    ""#    ""#                      #        
 #   m  mmm      #      #     mmm    mmm    mmm#   mmm  
 # m"     #      #      #    #"  "  #" "#  #" "#  #"  # 
 #"#      #      #      #    #      #   #  #   #  #"""" 
 #  "m  mm#mm    "mm    "mm  "#mm"  "#m#"  "#m##  "#mm"  */


#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef pair<int,int> pii;
typedef long long ll;
typedef double ld;
typedef vector<int> vi;
#define fi first
#define se second
#define fe first
#define SZ 666666
#define si(n) scanf("%d",&n);
#define sl(n) scanf("%ld",&n);
#define pi(n) printf("%d\n",n);
#define pl(n) printf("%ld\n",n);
#define pf(n) printf("%f\n",n);
#define FILL(a,b) memset(a,0,sizeof(b));
#define rep(i,n) for(int i=0;i<n;i++)
#define reps(i,a,b) for(int i=1;i<=b;i++)
const int INF=1e9+5;
const int MOD=1000000007;

//--------------**************---------------------


vector< pair<ll ,char> >colors;
bool comp( pair< ll ,char >p, pair< ll ,char > q)
{
    return p.first>q.first;
}
vector<char >solution;
int main()
{
     ios::sync_with_stdio(0);
     ll  t;
     cin>>t;
     ll  count=0;
     ll  N, R, O, Y, G, B, V;
     for(int j=1;j<=t;j++)
     {
         for(int i=0;i<3;i++)
          colors.clear();
 
         count++;
         cin>>N>>R>>O>>Y>>G>>B>>V;
         colors.push_back(make_pair(R,'R'));
         colors.push_back(make_pair(Y,'Y'));
         colors.push_back(make_pair(B,'B'));
 
 
     sort(colors.begin(),colors.end(),comp);
     while(colors[1].first!=colors[2].first)
     {
         solution.push_back(colors[0].second);
         solution.push_back(colors[1].second);
         colors[0].first--;
         colors[1].first--;
     }
     if(colors[1].first*2<colors[0].first)
     {
         cout<<"Case #"<<j<<": "<<"IMPOSSIBLE";
         cout<<endl;
     }
     else
     {
         cout<<"Case #"<<j<<": ";
         for(int i=0;i<solution.size();i++)
         cout<<solution[i];
         ll  m = colors[0].first;
         for(int i =0;i<colors[1].first;i++)
         {
             if(m>0)
             {
                 cout<<colors[0].second;
                 m--;
             }
             cout<<colors[1].second;
             if(m>0)
             {
                   cout<<colors[0].second;
                 m--;
             }
             cout<<colors[2].second;
         }
         cout<<endl;
     }
 
     solution.clear();
}
    return 0;
}