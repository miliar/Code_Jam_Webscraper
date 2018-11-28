#include <bits/stdc++.h>
using namespace std;
long long pre[10][20];
string toString(long long n)
{
    string ret="";
    while(n)
    {
        ret+=char(n%10+'0');
        n/=10;
    }
    reverse(ret.begin(),ret.end());
    return ret;
}
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int t;
    cin>>t;
    int tt=1;
    for (int i=0;i<10;i++)
    {
        pre[i][1]=i;
        for (int j=2;j<19;j++)
        {
            pre[i][j]=pre[i][j-1]*10+i;
        }
    }
    pre[10][0]=1;
    for (int i=1;i<19;i++)
        pre[10][i]=pre[10][i-1]*10;
    while(t--)
    {
        long long n;
        cin>>n;
        string s=toString(n);
        long long ret=0;
        int rem=s.size();
        for (int i=0;i<s.size();i++)
        {
            for (int j=9;j>=0;j--)
            {
                if (ret*pre[10][rem]+pre[j][rem]<=n){
                    ret=ret*10+j;
                    break;
                }
            }
            rem--;
        }
        cout<<"Case #"<<tt++<<": "<<ret<<endl;
    }
}
