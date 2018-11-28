#include<bits/stdc++.h>
#define LL long long
using namespace std;
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("output2.txt","w",stdout);
    string str;
    LL i,j,k,n,x,y,z;
    cin>>n;
    for(i=1;i<=n;i++)
    {
        str.clear();
        LL cnt=0;
        cin>>str;
        x=str.size();
        for(j=0;j<str.size()-1;j++)
        {
            if(str[j]==str[j+1]) cnt++;
            else if(str[j+1]>str[j]) cnt=0;
            else if(str[j]>str[j+1])
            {
                if(str[j]=='1')
                {
                    str.clear();
                    for(k=0;k<x-1;k++) str+='9';
                }
                else
                {
                    //str[j]--;
                    //for(k=j-1;k>=j-cnt;k--) str[k]--;
                    str[j-cnt]--;
                    for(k=(j-cnt)+1;k<x;k++) str[k]='9';
                }
            }
        }
        cout<<"Case #"<<i<<": "<<str<<"\n";
    }
}
