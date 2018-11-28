#include<bits/stdc++.h>
using namespace std;
#define loop(i,L,R) for(int i=(L);i<=(R);i++)
#define rept(i,L,R) for(int i=(L);i<(R);i++)
#define isc(n) scanf("%d",&n)
#define llsc(n) scanf("%lld",&n)
#define dsc(n) scanf("%lf",&n)
#define enl cout<<endl
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define xx first
#define yy second
typedef long long ll;
typedef pair<int,int>PI;
typedef pair<pair<int,int>,int>PII;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas=0;
    isc(t);
    while(t--)
    {
        string in;
        cin>>in;
        int l=in.size();
        if(l==1)
        {
            cout<<"Case #"<<++cas<<": "<<in<<endl;
            continue;
        }
        int i=1;
        while(i<l && in[i]>=in[i-1])i++;
        if(i!=l)
        {
            i--;
            while(i>=0 && in[i]==in[i-1])i--;
            in[i]--;
            i++;
            while(i<l){in[i]='9';i++;}
            i=0;
            while(in[i]=='0')i++;
            //cout<<i<<endl;
            in.erase(0,i);
        }
        cout<<"Case #"<<++cas<<": "<<in<<endl;
    }
    return 0;
}

