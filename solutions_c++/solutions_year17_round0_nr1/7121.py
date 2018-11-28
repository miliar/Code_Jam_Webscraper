#include<bits/stdc++.h>
using namespace std;
string str;
int n,x,dp[700][500];
int call(int pos,int val)
{
    //cout<<pos<<" "<<val<<endl;
    //cout<<str<<endl;
    int p;
    if(val%43==0)
    {
        p=val/43;
        if(p==x)
        {
           // cout<<str<<endl;
            return pos;
        }
    }
    if(pos>5000)
    {
       // cout<<'p'<<endl;
        return -1;
    }
    //if(dp[pos][val]!=-1) return dp[pos][val];
    int sum=0,ret=-1,i,j;
    for(i=0;i<=x-n;i++)
    {
        if(str[i]=='+') continue;
        for(j=i;j<i+n;j++)
        {
            if(str[j]=='+')
            {
                str[j]='-';
                val+=2;
            }
            else if(str[j]=='-')
            {
                str[j]='+';
                val-=2;
            }
        }
        ret=call(pos+1,val);

    }
    return ret;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output3.txt","w",stdout);
    int i,j,y,z,t;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        str.clear();
        cin>>str>>n;
        x=str.size();
        int sum=0;
        //memset(dp,-1,sizeof(dp));
        for(j=0;j<x;j++)
        {
            sum+=str[j];
        }
        y=call(0,sum);
        //cout<<str<<endl;
        if(y==-1) cout<<"Case #"<<i<<": IMPOSSIBLE\n";
        else cout<<"Case #"<<i<<": "<<y<<"\n";
    }


}
