#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
 
typedef long long ll;
typedef pair<int,ll> pp;
typedef map<pp,ll> mpp;
typedef vector<pp> vv;
typedef deque<pp> dq;

int chk(string s)
{
    for(int i=0;i<s.length();i++)
        if(s[i]=='-')
            return 0;
    return 1;
}

int main()
{
    int t;
    scanf("%d",&t);
    
    for(int z=1;z<=t;z++)
    {
        string s;
        int k,n;
        cin>>s>>k;
        
        n=s.length();
        int cnt=0;
        for(int i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                for(int j=i;j<(i+k) && (i+k)<=n;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                cnt++;
            }
        }
        if(chk(s)==1)
            printf("Case #%d: %d\n",z,cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n",z);
    }
    return 0;
}
