#include<bits/stdc++.h>
using namespace std;
vector<int> ans;
string s;
int start;
int  test;
int k;
int check(int a)
{
    ans.clear();
    while(a)
    {
        ans.push_back(a%10);
        a=a/10;
    }
    sort(ans.begin(),ans.end());
    int l=0;
    for(int i=0;i<ans.size();i++)
    {
        l=l*10+ans[i];
    }
    //cout<<l<<" "<<a<<"\n";
    return l;
}
int main()
{
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        start=0;
        scanf("%d",&k);
        if(check(k)==k)
        {
            printf("Case #%d: %d\n",t,k);
            continue;
        }
        for(int i=k-1;i>=1;i--)
        {
           // cout<<"----"<<check(i)<<"\n";
            if(check(i)==i)
            {printf("Case #%d: %d\n",t,i);
            break;
            }
        }

    }
}

