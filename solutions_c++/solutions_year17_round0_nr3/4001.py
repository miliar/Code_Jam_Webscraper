#pragma comment(linker, "/stack:640000000")

#include<bits/stdc++.h>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
#define ll long long int
#define scanl(a) scanf("%lld",&a)
#define scanii(a,b) scanf("%d%d",&a,&b)
#define scaniii(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define scanll(a,b) scanf("%lld%lld",&a,&b)
#define scanlll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define scani(a) scanf("%d",&a)
#define clr(a) memset(a,0,sizeof(a))
#define clr_(a) memset(a,-1,sizeof(a))
#define pb(a) push_back(a)
#define pii pair<int,int>
#define sqr(a) a*a
#define eps 1e-9
#define inf INT_MAX
#define pi acos(-1.0)
#define ff first
#define ss second
#define INF 1e18
#define endl '\n'
#define vsort(v) sort(v.begin(),v.end())
int arr[1000010];
vector<int>v;
multiset<int>st;

int main()
{
    /// ios_base::sync_with_stdio(0);
    /// cin.tie(0);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scani(t);
    for(int c=1;c<=t;c++)
    {
        clr(arr);
        int n,k;
        scanii(n,k);
        int p,q;
        int ans_m=0,ans_M=0;
        if(n==k)
        {
            printf("Case #%d: %d %d\n",c,0,0);
            continue;
        }
//        st.clear();
//        multiset<int>::iterator it;
//        st.insert(n);
        arr[n]=1;
        int temp=n,MAX=n;
        for(int i=1;i<=k;i++)
        {
            temp=MAX;
            if(temp==0)
            {
                ans_m=0;
                ans_M=0;break;
            }
            if(temp%2==1)
            {
                ans_M=temp/2;
                ans_m=temp/2;
            }
            else
            {
                ans_M=temp/2;
                ans_m=ans_M-1;
            }
            ans_m=max(ans_m,0);
            ans_M=max(ans_M,0);
            arr[ans_m]++;
            arr[ans_M]++;
            arr[temp]--;
            for(int i=temp;i>=0;i--)
            {
                if(arr[i]>0)
                {
                    MAX=i;break;
                }
            }
          //  cout<<n<<" "<<i<<" "<<ans_M<<" "<<ans_m<<endl;
        }
        printf("Case #%d: %d %d\n",c,ans_M,ans_m);
    }
    return 0;
}


