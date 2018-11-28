#include<bits/stdc++.h>
#define s(x) scanf("%d",&x)
#define ll long long
#define l(x) scanf("%I64d",&x)
#define cst int t; s(t); while(t--)
#define fr freopen("A-small-attempt0 (1).in", "r", stdin)
#define fo freopen("out.txt", "w", stdout)
#define finp ios_base::sync_with_stdio(false)
#define pb push_back
#define pf printf

using namespace std;

struct data
{
    ll r, h;
};

bool sortbyR(const data &a, const data &b)
{
    return a.r>b.r;
}


int n, k;
data a[1009];

ll process(int pos, ll maxArea, int pl, bool base)
{
    if(pl == 0 || pos >=n)
        return maxArea;
    else{
        ll add;
        if(!base)
            add = a[pos].r * a[pos].r;
        else
            add = 0;


        return max(
                 process(pos+1, maxArea + 2*a[pos].r*a[pos].h + add, pl-1, true),
                 process(pos+1, maxArea, pl, base)
                 );
        }
    return 0;
}

int main()
{
    fr;
    fo;
    int cs =1;
    cst{
        cin>>n>>k;
        double pi = 3.14159265359;

        for(int i=0; i<n; i++)
            cin>>a[i].r>>a[i].h;
        sort(a, a+n, sortbyR);
        //for(int i=0 ;i<n; i++)   cout<<a[i].r<<' '<<a[i].h<<endl;
        double res = process(0, 0, k, false)*pi ;

        printf("Case #%d: %.9lf\n",cs++, res );


    }
    return 0;
}
