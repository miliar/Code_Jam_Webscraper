#define WYTE 133
#include<bits/stdc++.h>
#define X first
#define Y second
#define mp(x,y) make_pair((x),(y))
#define eb(...) emplace_back(__VA_ARGS__)
#define SZ(x) int((x).size())
#define ALL(x) (x).begin(),(x).end()
#define INIT(x,y) memset((x),(y),sizeof(x))
#define PQ priority_queue
#define IT iterator
#define INF 1e9
#define EPS 1e-7
#define MOD 1000000007
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

int main()
{
    freopen("A-large.in","rb",stdin);
    freopen("output.txt","wb",stdout);
    int t,ii,k,i,j,cnt;
    bool err;
    string s;
    cin>>t;
    for(ii=1;ii<=t;++ii)
    {
        cin>>s>>k;
        cnt=0;
        for(i=0;i<SZ(s);++i)
        {
            if(s[i]=='-')
            {
                if(i+k>SZ(s))break;
                ++cnt;
                for(j=i;j<i+k;++j)
                {
                    if(s[j]=='+')s[j]='-';
                    else s[j]='+';
                }
            }
        }
        err=0;
        for(i=0;i<SZ(s);++i)
        {
            if(s[i]=='-')err=1;
        }
        cout<<"Case #"<<ii<<": ";
        if(err)
        {
            cout<<"IMPOSSIBLE\n";
        }
        else
        {
            cout<<cnt<<"\n";
        }
    }
}
