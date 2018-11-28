/*Divyam Goyal - IIT-BHU*/
#include<bits/stdc++.h>
using namespace std;

#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define bitcount    __builtin_popcountll
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define ll long long
#define mp(a,b) make_pair(a,b)
#define F first
#define S second
#define pb(x) push_back(x)
#define MOD 1000000007
#define MAX 100005

void pr(vector<int>v)
{
    for(int i=0;i<v.size();i++){
        cout<<v[i];
    }
    cout<<"\n";
}

int main()
{
    //ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    //freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    int qt;
    sd(qt);
    for(int t=1;t<=qt;t++)
    {
        printf("Case #%d: ",t);

        ll n;
        cin>>n;
        vector<int>v;
        while(n)
        {
            v.pb(n%10);
            n/=10;
        }
        n=v.size();

        int k=-1;

        for(int i=0;i<=n-1;i--)
        {
            if(v[i]>v[i+1]){
                k=i;
                while(k>=0&&v[k]==v[i])
                    k--;
                break;
            }
        }
        k++;
        int tmp=0;
        for(int i=0;i<n-1;i++)
        {
            if(v[i]>v[i+1])tmp=1;
        }
        if(!tmp)
        {
            pr(v);
            continue;
        }

        trace1(k);

        v[k]--;
        for(int i=k+1;i<n;i++)
            v[i]=9;
        tmp=0;
        for(int i=0;i<n;i++)
        {
            if(v[i]==0)
            {
                if(tmp)cout<<v[i];
            }
            else
            {
                tmp=1;
                cout<<v[i];
            }
        }
        cout<<"\n";





    }






    return 0;


}