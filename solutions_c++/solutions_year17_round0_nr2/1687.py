#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define ll long long
int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cs=1;
    scanf("%d",&t);
    while(t--)
    {
        int i,j,n,k;
        string s;
        cin>>s;
        n=s.size();
        for(i=s.size()-1;i>=1;i--)
        {
            if(s[i]<s[i-1])
            {
                s[i-1]--;
                for(j=i;j<n;j++)
                    s[j]='9';
            }
        }
        printf("Case #%d: ",cs);
        for(i=0;i<n;i++)
            if(s[i]!='0')
                break;
        for(;i<n;i++)
            cout<<s[i];
        cout<<endl;
        cs++;
    }
    return 0;
}
