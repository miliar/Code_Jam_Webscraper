#include <bits/stdc++.h>
using namespace std;
void input()
{
    freopen("ain.txt","r",stdin);
    freopen("aout.txt","w",stdout);
}
void solveCaseSmall(int testCase);
void solveCaseCSmall(int testCase);

int main()
{
    input();
    int testCases;
    scanf("%d",&testCases);
    for(int testCase = 1; testCase <= testCases; testCase++)
        solveCaseCSmall(testCase);
}
const int MAXN = 110;
struct pancake
{
    int r,h;
    void read()
    {
        scanf("%d%d",&r,&h);
    }
}pdsa[MAXN];
bool cmp(pancake p1, pancake p2)
{
    if(p1.r==p2.r) return p1.h>p2.h;
    return p1.r<p2.r;
}
typedef long long ll;
struct maxholder
{
    vector<ll> val;
    maxholder(int k)
    {
        val.resize(k);
    }
    void ins(ll x)
    {
        if(val.size()==0) return;
        if(x<val[0]) return;
        val[0]=x;
        for(int i=0;i<val.size()-1;i++)
        {
            if(val[i]>val[i+1]) swap(val[i],val[i+1]);
        }

    }
    ll get()
    {
        if(val.size()==0) return 0;
        ll ret = 0;
        for(int i=0;i<val.size();i++)
        {
            if(val[i]==0) return -1ll;
            ret += val[i];
        }
        return ret;
    }
    void debug()
    {
        for(int i=0;i<val.size();i++) printf("%lld ",val[i]);
        printf("\n");
    }
};
double pi = acos(-1.0);
typedef pair<int,int> pii;
pii jamie[MAXN], cameron[MAXN];
bool within720(pii a, pii b)
{
    if(a.first>b.first) swap(a,b);
    //clockwise
    if(b.second-a.first<=720) return true;
    if(a.second + 1440 - b.first <=720) return true;
    return false;
}
void solveCaseSmall(int testCase)
{
    printf("Case #%d: ",testCase);
    int actJ,actC;
    scanf("%d%d",&actJ, &actC);
    for(int i=1;i<=actJ;i++)
        scanf("%d%d",&jamie[i].first,&jamie[i].second);
    for(int i=1;i<=actC;i++)
        scanf("%d%d",&cameron[i].first,&cameron[i].second);
    if(actJ == 0)
    {
        if(actC == 1)
        {
            cout << 2 << endl;
        }
        else if(actC == 2)
        {
            if(within720(cameron[1],cameron[2])) cout << 2 << endl;
            else cout << 4 << endl;
        }
    }
    else if(actJ == 1)
    {
        cout << 2 << endl;
    }
    else if(actJ == 2)
    {
        if(within720(jamie[1],jamie[2])) cout << 2 << endl;
        else cout << 4 << endl;
    }
}
double p[MAXN];
int val[MAXN];
priority_queue<int> pq;
void solveCaseCSmall(int testCase)
{
    printf("Case #%d: ",testCase);
    int n,k;
    scanf("%d%d",&n,&k);
    double x;
    scanf("%lf",&x);
    for(int i=1;i<=n;i++)
    {
        scanf("%lf",&p[i]);
    }
    sort(p+1,p+n+1);
    p[n+1]=1.0;
    for(int i=1;i<=n&&x>0;i++)
    {
        double dif = p[i+1]-p[i];
        int num = i;
        if(x > dif * num)
        {
            for(int j = 1; j <= i; j++)
                p[j]=p[i+1];
            x -= dif * num;
        }
        else
        {
            double inc = x / num;
            for(int j=1;j<=i;j++) p[j]+=inc;
            x = 0;
        }
    }
    double ans = 1.0;
    for(int i=1;i<=n;i++) ans*=p[i];
    printf("%.8f\n",ans);
}
