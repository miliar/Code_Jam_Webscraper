#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define ll              long long
#define llu             unsigned long long
#define pb              push_back
#define MOD             1000000007
#define MAX             1000007
#define eps             1e-8
#define inf             0x3f3f3f3f
#define INF             2e18
#define clr(a)          memset(a,0,sizeof(a))
#define reset(a)        memset(a,-1,sizeof(a))
#define ff              first
#define ss              second
#define pLL             pair<ll,ll>
#define mp              make_pair
#define pi              pair<int,int>
#define READ(f)         freopen(f,"r",stdin)
#define WRITE(f)        freopen(f,"w",stdout)
#define pii             2.0*acos(0.0)
#define all(a)          a.begin(),a.end()
#define rall(a)         a.rbegin(),a.rend()
#define SQR(a)          ((a)*(a))
#define Unique(a)       sort(all(a)),a.erase(unique(all(a)),a.end())
#define int_map         map<int,int>
#define v_map           map<int,vector<int> >
#define long_map        map<ll,ll>
#define IO              ios::sync_with_stdio(false)
#define inputline(a)    getline(cin,a)
#define min3(a,b,c)     min(a,min(b,c))
#define max3(a,b,c)     max(a,max(b,c))
#define min4(a,b,c,d)   min(min(a,b),min(c,d))
#define max4(a,b,c,d)   max(max(a,b),max(c,d))
#define max5(a,b,c,d,e) max(max3(a,b,c),max(d,e))
#define min5(a,b,c,d,e) min(min3(a,b,c),min(d,e))
#define FOR(a,it)       for(Iterator(a) it = a.begin();it != a.end(); it++)
#define rFOR(a,it)      for(rIterator(a) it = a.rbegin();it != a.rend(); it++)
#define vi              vector <int>
#define vL              vector <ll>
#define dbg(a)          cout<<a<<endl
int d8x[]={-1,-1,0,1,1,1,0,-1};
int d8y[]={0,1,1,1,0,-1,-1,-1};
template <typename T> using orderset = tree <T, null_type, less<T>, rb_tree_tag,tree_order_statistics_node_update>;
template <typename T> inline T GCD (T a,T b ) {a = abs(a);b = abs(b); if(a < b) swap(a, b); while ( b ) { a = a % b; swap ( a, b ); } return a;}
template <typename T> inline T EGCD(T a,T b,T &x,T &y){if(a == 0) {x = 0;y = 1;return b;}T x1, y1;T d = EGCD(b % a, a, x1, y1);x = y1 - (b / a) * x1;y = x1;return d;}
template <typename T> inline T LCM(T x,T y){T tp = GCD(x,y);if( (x / tp) * 1. * y > 9e18) return 9e18;return (x / tp) * y;}
template <typename T> inline T BigMod(T A,T B){T ret = 1;while(B){if(B & 1) ret = (ret * A);A = (A * A);B = B >> 1;}return ret;}
template <typename T> inline T InvMod (T A,T M = MOD){return BigMod(A,M-2);}

vector<int>v[50];
char str[30][30];
int main(void)
{
    READ("input.txt");
    WRITE("output.txt");
    int T,N=0;
    scanf("%d",&T);
    while(++N<=T){
        int row,col;
        for(int i=0;i<50;i++)v[i].clear();
        scanf("%d%d",&row,&col);
        for(int i=0;i<row;i++){
            scanf("%s",str[i]);
        }
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(str[i][j]!='?')v[i].pb(j);
            }
        }
        int last_row=0;
        for(int i=0;i<row;i++){
            int last_col=-1;
            for(int j=0;j<v[i].size();j++){
                int temp=v[i][j];
//                cout<<i<<" "<<temp<<endl;
                for(int k=last_col+1;k<=temp;k++){
                    str[i][k]=str[i][temp];
                    last_col=k;
                }
                last_row=i;
            }
            if(last_row < i){
                for(int j=0;j<col;j++)str[i][j]=str[last_row][j];
                last_col=col-1;
            }
//            cout<<str[i]<<endl;
            if(last_col + 1 < col && last_col>=0){
                int temp=v[last_row][v[last_row].size()-1];
                for(int k=temp+1;k<col;k++){
                    str[i][k]=str[i][temp];
                    last_col=k;
                }
            }
        }
        for(int i=row-2;i>=0;i--){
            for(int j=0;j<col;j++){
                if(str[i][j]=='?')str[i][j]=str[i+1][j];
            }
        }
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(str[i][j]=='?')str[i][j]='A';
            }
        }
        printf("Case #%d:\n",N);
        for(int i=0;i<row;i++)printf("%s\n",str[i]);
    }
    return 0;
}
