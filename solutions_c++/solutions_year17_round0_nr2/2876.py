#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define pll pair<LL, LL>
#define pii pair<int,int>

#define mp make_pair
#define pb push_back
#define fs first
#define sc second

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define EPS 1e-6
#define MOD (1000000007)
#define PI  2*acos(0);

#define fore(iter,v) for(iter=v.begin(); iter!=v.end(); iter++)
#define forup(i,a,n) for(i=a; i<n; i++)
#define rep(i,n) for(i=0; i<n; i++)
#define SET(a, v) memset(a, v, sizeof a)
#define all(a) a.begin(),a.end()
#define ALLOC0(N)   (int*)calloc(N, sizeof(int));

#define gi(x) scanf("%d",&x)
#define gl(x) scanf("%lld",&x)


#define ps(x) printf("%s",x)
#define pi(x) printf("%d",x)
#define pl(x) printf("%lld", x)
#define pn printf("\n")
#define spc printf(" ")
#define gc getchar

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,bk;
    cin>>t;
    for(bk=1;bk<=t;bk++)
    {
        cout<<"Case #"<<bk<<": ";
        string s;
        ll i,j,k=1;
        cin>>s;
        for(i=0;i<s.size()-1;i++)
        {
            if(s[i]<s[i+1])
                k=1;
            else if(s[i]==s[i+1])
                k++;
            else
                break;
        }

        if(i!=s.size()-1)
        {
            if(s[i]=='1' && i-k+1!=0)
                s[i-k]=s[i-k]-1;
            else
                s[i-k+1]=s[i-k+1]-1;
            for(j=i-k+2;j<s.size();j++)
                s[j]='9';
        }

        if(s[0]=='0')
            s.erase(s.begin());
        cout<<s<<endl;

    }
    return 0;
}
