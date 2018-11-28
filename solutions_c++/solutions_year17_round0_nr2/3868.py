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
vector<int>v;
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
        string s,ss="";
        cin>>s;
        ss+=s[0];
        int len=s.size();
       /// cout<<"Case #"<<c<<": ";
            for(int i=1;i<len;i++){
                if(s[i]<s[i-1])
                {
                    int j=i-1;
                    while(j>=0 && s[j]==s[i-1]){
                        j--;
                    }
                    j++;
                    s[j]--;
                  //  cout<<j<<" "<<s[j]<<endl;
                    for(int k=j+1;k<len;k++)s[k]='9';
                    break;
                }
            }

            cout<<"Case #"<<c<<": ";
            for(int i=0;i<s.size();i++)
            {
                if(s[i]=='0')continue;
                cout<<s[i];
            }
            cout<<endl;

//        printf("Case #%d: %d\n",c,n);
    }
    return 0;
}


