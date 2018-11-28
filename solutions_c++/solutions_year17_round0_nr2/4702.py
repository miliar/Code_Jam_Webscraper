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
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    Int T;
    cin>>T;
    for (Int k=1;k<=T;++k)
    {
        Int N;
        cin>>N;
        cout<<"Case #"<<k<<": ";
        vi V;
        while (N)
        {
            V.pb(N%10);
            N=N/10;
        }
        reverse(V.begin(),V.end());
        bool flag=1;
        for (Int i=1;i<V.size();++i)
        {
            if (V[i]<V[i-1])
                flag=0;
        }
        if (flag)
        {
            for (Int i=0;i<V.size();++i)
                cout<<V[i];
            cout<<"\n";
            continue;
        }
        Int tmp=0;
        flag=1;
        for (Int i=0;i<V.size();++i)
        {
            tmp+=V[i];
            if (tmp<i+1)
            {
                flag=0;
                break;
            }
        }
        if (flag==0)
        {
            for (Int i=1;i<V.size();++i)
                cout<<9;
            cout<<"\n";
            continue;
        }
        Int last=1;
        for (Int i=0;i<V.size();++i)
        {
            flag=1;
            do
            {
                ++last;
                for (Int j=i;j<V.size();++j)
                {
                    if (last-V[j]>0)
                    {
                        flag=0;
                        break;
                    }
                    if (last-V[j]<0)
                        break;
                }
            }while (flag&&last<=9);
            last--;
            cout<<last;
            if (last<V[i])
                last=9;
        }
        cout<<"\n";
    }
    return 0;
}
