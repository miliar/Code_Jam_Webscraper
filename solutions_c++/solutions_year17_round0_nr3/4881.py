#include<bits/stdc++.h>
using namespace std;
#define fs first
#define sc second
#define MAX 100000
#define pb push_back
#define mp make_pair
#define INF (1LL<<61)
#define MOD 1000000007
typedef long long Int;
typedef pair<Int,Int> pii;
typedef vector<Int> vi;
typedef vector<pii> vii;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    Int T;
    cin>>T;
    for (Int k=1;k<=T;++k)
    {
        Int N,K,last;
        cin>>N>>K;
        map<Int,Int>M;
        M[N]++;
        while(1)
        {
            Int x=(M.rbegin())->fs;
            if (M[x]>=K)
            {
                last=x;
                break;
            }
            else
            {
                if (x%2)
                    M[x/2]+=2*M[x];
                else
                {
                    M[x/2]+=M[x];
                    M[x/2-1]+=M[x];
                }
                K-=M[x];
                M.erase(x);
            }
        }
        cout<<"Case #"<<k<<": ";
        if (last%2)
            cout<<last/2<<" "<<last/2<<"\n";
        else
            cout<<last/2<<" "<<last/2-1<<"\n";
    }
    return 0;
}
