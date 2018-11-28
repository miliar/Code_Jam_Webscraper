#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
 
typedef long long ll;
typedef pair<int,ll> pp;
typedef map<pp,ll> mpp;
typedef vector<pp> vv;
typedef deque<pp> dq;


int main()
{
    int t;
    scanf("%d",&t);
    
    int ans[1001]={0};
    for(int i=1;i<=1000;i++)
    {
        int temp=i/10,l_rem=i%10,f=1;
        while(temp!=0)
        {
            int rem=temp%10;
            temp/=10;
            if(rem>l_rem)
            {
                f=0;
                break;
            }
            l_rem=rem;
        }
        if(f==0)
            ans[i]=ans[i-1];
        else
            ans[i]=i;
    }
    
    int i=1;
    while(t--)
    {
        int n;
        scanf("%d",&n);
        
        printf("Case #%d: %d\n",i,ans[n]);
        i++;
    }
    return 0;
}
