//
#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<climits>
#include<fstream>
#include<iomanip>
#include<queue>
#include<stack>
#define lli long long

using namespace std;

bool used[101][101][101][101];
int dp[101][101][101][101],buff,debuff,starthp;

int rec(int hd, int ad, int hk,int ak)
{

    int p=INT_MAX,p1;
//cout<<hd<<" "<<ad<<" "<<hk<<" "<<ak<<endl;

    if(hk<=0)return 0;
    if(hd<=0)return -1;

    if(ak<0)ak=0;
//cout<<hd<<" "<<ad<<" "<<hk<<" "<<ak<<"!"<<endl;
    if(used[hd][ad][hk][ak])return dp[hd][ad][hk][ak];

    p1=rec(hd-ak,ad,hk-ad,ak);
    if(p1!=-1)p=min(p,p1);

    if(buff!=0 && ad<hk)p1=rec(hd-ak,ad+buff,hk,ak);
    if(buff!=0 && ad<hk && p1!=-1)p=min(p,p1);

    if(hd<starthp-ak)p1=rec(starthp-ak,ad,hk,ak);
    if(hd<starthp-ak && p1!=-1)p=min(p,p1);

    if(debuff!=0 && ak>0 && ak-debuff>=0)p1=rec(hd-ak+debuff,ad,hk,ak-debuff);
    if(debuff!=0 && ak>0 && ak-debuff<0)p1=rec(hd,ad,hk,0);

    if(debuff!=0 && ak>0 && p1!=-1)p=min(p,p1);


    if(p==INT_MAX)p=-2;
    dp[hd][ad][hk][ak]=p+1;
    used[hd][ad][hk][ak]=1;
    return p+1;


}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ifstream cin ("input.in");
    ofstream cout("output.txt");

    int T,p,hd,ad,hk,ak;
    cin>>T;


    for(int t1=1;t1<=T;t1++)
    {
        //cout<<t1<<endl;
        cout<<"Case #"<<t1<<": ";

        memset(used,0,sizeof(used));
        memset(dp,0,sizeof(dp));

        cin>>hd>>ad>>hk>>ak>>buff>>debuff;
        starthp=hd;

        p=rec(hd,ad,hk,ak);

        if(p==-1){cout<<"IMPOSSIBLE"<<"\n";}
        else cout<<p<<"\n";



    }

    return 0;
}

