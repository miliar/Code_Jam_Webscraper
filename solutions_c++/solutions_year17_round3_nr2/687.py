
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cassert>
#define pb push_back
#define mk make_pair
#define F first
#define S second
#define pi 3.1415926535

#define MOD (1000000007)
using namespace std;
vector<pair <int,int> > v[2];
vector<pair< pair<int,int> ,int> > v2;
int arr[500][3];
int solve()
{
    v2.clear();
    for(int i=0;i<v[0].size();i++)
        v2.pb(mk(mk(v[0][i].F,v[0][i].S),0));
    
    for(int i=0;i<v[1].size();i++)
        v2.pb(mk(mk(v[1][i].F,v[1][i].S),1));
    
    sort(v2.begin(),v2.end());
    for(int i=0;i<v2.size();i++)
    {
        arr[i][0]=v2[i].F.F;
        arr[i][1]=v2[i].F.S;
        arr[i][2]=v2[i].S;
        
        printf("%d %d %d\n",arr[i][0],arr[i][1],arr[i][2]);
    }
    
    vector<int> inb,f[2];
    int prev=arr[0][2];
    int st=arr[0][0];
    int m[2];
    int sw=0;
    m[0]=0;m[1]=0;
    for(int i=1;i<v2.size();i++)
    {
        if(arr[i][2]==prev)
        {
            f[prev].pb(arr[i][0]-arr[i-1][1]);
            continue;
        }
        sw++;
        m[prev]+=arr[i-1][1]-st;
        st=arr[i][0];
        prev=arr[i][2];
        inb.pb(st-arr[i-1][1]);
    }
    printf("f[0]: ");
    for(int i=0;i<f[0].size();i++)
        printf("%d ",f[0][i]);
    printf("\n");
    printf("f[1]: ");
    for(int i=0;i<f[1].size();i++)
        printf("%d ",f[1][i]);
    printf("\n");
    printf("inb: ");
    for(int i=0;i<inb.size();i++)
        printf("%d ",inb[i]);
    printf("\n");
    printf("m[%d]=%d  m[%d]=%d  sw=%d\n",0,m[0],1,m[1],sw);


    int n=v2.size()-1;
    if(arr[n][2]==arr[0][2])
    {
        m[arr[n][2]]+=1440-st;
        m[arr[n][2]]+=arr[0][0]-0;
        f[arr[n][2]].pb(1440-arr[n][1]+arr[0][0]-0);
    }
    else
    {
        sw++;
        m[prev]+=arr[n][1]-st;
        inb.pb(1440-arr[n][1]+arr[0][0]);
    }
    
    printf("f[0]: ");
    for(int i=0;i<f[0].size();i++)
        printf("%d ",f[0][i]);
    printf("\n");
    printf("f[1]: ");
    for(int i=0;i<f[1].size();i++)
        printf("%d ",f[1][i]);
    printf("\n");
    printf("inb: ");
    for(int i=0;i<inb.size();i++)
        printf("%d ",inb[i]);
    printf("\n");
    printf("m[%d]=%d  m[%d]=%d  sw=%d\n",0,m[0],1,m[1],sw);
    int sum=0;
    for(int i=0;i<inb.size();i++)
        sum+=inb[i];
    
    int t=720-min(m[0],m[1]);
    if(t<=sum)
        return sw;
    
    
    t-=sum;
    printf("t=%d\n",t);
    int ind;
    if(m[0]<m[1])
        ind=1;
    else
        ind=0;
    sort(f[ind].rbegin(),f[ind].rend());
    for(int i=0;i<f[ind].size();i++)
        printf("f[%d][%d]=%d\n",ind,i,f[ind][i]);
    for(int i=0;i<f[ind].size();i++)
    {
        t-=f[ind][i];
        printf("t=%d\n",t);
        sw+=2;
        if(t<=0)
            break;
        
    }
    return sw;

}
/*int solve(int a,int b)
{
    int mins=0,cnt=0,ia=0,ib=0,na=v[a].size(),nb=v[b].size();
    while(ia<na && ib<nb)
    {
        
    }
}*/
int main(void)
{
    ifstream infile;
    infile.open("in.txt");
    
    ofstream outfile;
    outfile.open("out.txt");
    
    int t,c,j,c1,c2,j1,j2,cc=1;
    //long long h,r,ans,tmp;
    infile >> t;
    
    while(t--)
    {
        infile>>c>>j;
        v[0].clear();
        v[1].clear();
        for(int i=0;i<c;i++)
        {
            infile>>c1>>c2;
            v[0].pb(mk(c1,c2));
        }
        for(int i=0;i<j;i++)
        {
            infile>>j1>>j2;
            v[1].pb(mk(j1,j2));
        }
        sort(v[0].begin(),v[0].end());
        sort(v[1].begin(),v[1].end());
        int ans = solve();
       // cout<<n<<" "<<k<<endl;
        outfile<<"Case #"<<cc++<<": "<<ans<<endl;
        //cout<<"Case #"<<cc<<": "<<d<<endl;
        printf("Case #%d: %d\n",cc,ans);
    }

    
    outfile.close();
    infile.close();
}