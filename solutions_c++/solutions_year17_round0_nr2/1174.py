#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

string n;
string solve()
{
    bool flag=0;
    for(int i=n.length()-1;i>0;i--)
        if(n[i]<n[i-1])
            flag=1;
    if(!flag)
        return n;
    reverse(n.begin(), n.end());
    string ans="";
    int j=n.length()-1;
    for(int i=j; i>0; i--)
    {
        if(n[i]<n[i-1])
            j=i-1;
        if(n[i]>n[i-1])
            break;
    }
    n[j]--;
    if(j==n.length()-1 && n[j]=='0')
    {
        for(int i=1; i<n.length(); i++)
            ans+="9";
        return ans;
    }
    for(int i=n.length()-1; i>=j; i--)
        ans+=n[i];
    for(int i=j-1; i>=0; i--)
        ans+="9";
    return ans;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        printf("Case #%d: ", ca++);
        cin>>n;
        cout<<solve()<<endl;
    }
    return 0;
}
