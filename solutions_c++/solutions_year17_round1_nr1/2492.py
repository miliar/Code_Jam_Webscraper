#include<iostream>
#include<algorithm>
#include<math.h>
#include<cstring>
#include<iomanip>
#include<stdio.h>
#include<limits>
#include<unordered_map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#define gcd __gcd
#define pb(x) push_back(x)
#define ll long long
#define in(x) scanf("%d",&x)
#define mod 1000000007LL
#define sz(x) x.size()
#define mst(x,a) memset(x,a,sizeof(x))
#define pii pair<ll,ll>
#define F first
#define S second
#define m_p make_pair
#define all(v) (v.begin(),v.end())
using namespace std;
char a[25][25];
int r,c;
bool tool[25];
int t;
int main()
{
    //ios::sync_with_stdio(0);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    cin>>t;
    for(int test=1;test<=t;test++)
    {

        cin>>r>>c;

        for(int i=0;i<r;i++) for(int j=0;j<c;j++) cin>>a[i][j];
//        for(int i=0;i<r;i++)
//        {
//            for(int j=0;j<c;j++)
//                 cout<<a[i][j]<<" ";
//            cout<<endl;
//        }

        for(int i=0;i<r;i++)
        {
            tool[i]=0;
            for(int j=0;j<c;j++)
            {
                if(a[i][j]!='?')
                {
//                    cout<<i<<" "<<j<<endl;
                    tool[i]=1;
                    for(int k=j+1;k<c;k++)
                    {
                        if(a[i][k]!='?')
                            break;
                        a[i][k]=a[i][k-1];
                    }
                    for(int k=j-1;k>=0;k--)
                    {
                        if(a[i][k]!='?')
                            break;
                        a[i][k]=a[i][k+1];
                    }
                }
            }
        }
//        for(int i=0;i<r;i++)
//        {
//            for(int j=0;j<c;j++)
//                 cout<<a[i][j]<<" ";
//            cout<<endl;
//        }
        for(int i=0;i<r;i++)
        {
           if(!tool[i])
           {
               int k=i+1;
               while(!tool[k]&&k<r)
                k++;
               if(k<r)
               {
                   for(int j=0;j<c;j++)
                    a[i][j]=a[k][j];
               }
               k=i-1;
               while(!tool[k]&&k>=0)
                    k--;
               if(k>=0)
               {
                   for(int j=0;j<c;j++)
                    a[i][j]=a[k][j];
               }
           }
        }
        cout<<"Case #"<<test<<": ";
        cout<<endl;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
                 cout<<a[i][j];
            cout<<endl;
        }

    }
    return 0;
}


