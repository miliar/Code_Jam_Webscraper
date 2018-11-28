#include <bits/stdc++.h>
using namespace std;
vector <int> values;
long long calc(long long n)
{
    long long temp=n;
    long long nilai=0;
    while(temp>0)
    {
        values.push_back(temp%10);
        temp/=10;
    }
    if(values.size()==1) return values[0];
    bool tanda=true;
    while(tanda){
        for(int i=values.size()-2;i>=0;i--)
        {
            if(values[i+1]>values[i])
            {
                values[i+1]--;
                for(int j=i;j>=0;j--)
                {
                    values[j]=9;
                }
            }
        }
        for(int i=values.size()-2;i>=0;i--)
        {
            if(values[i+1]>values[i])
            {
                tanda=true;
                break;
            }
            tanda=false;
        }
    }
    for(int i=values.size()-1;i>=0;i--)
    {
        nilai+=values[i];
        if(i>0)nilai*=10;
    }
    return nilai;
}


int main()
{
    int tc;
    long long n;
    //freopen("B-large.in","r",stdin);
    //freopen ("B-large.out","w",stdout);
    cin>>tc;
    for(int i=1;i<=tc;i++)
    {
        values.clear();
        cin>>n;
        printf("Case #%d: %lld\n",i,calc(n));
    }

    return 0;
}
