#include <bits/stdc++.h>
using namespace std;
void input()
{
    freopen("ain.txt","r",stdin);
    freopen("aout.txt","w",stdout);
}
void solveCaseSmall(int testCase);
void solveCaseCSmall(int testCase);
void solveCaseBBig(int testCase);
int main()
{
    input();
    int testCases;
    scanf("%d",&testCases);
    for(int testCase = 1; testCase <= testCases; testCase++)
        solveCaseBBig(testCase);
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
struct ev
{
    int bg, en, tp;
    ev(int _bg, int _en, int _tp)
    {
        bg = _bg;
        en = _en;
        tp = _tp;
    }
};
vector<ev> events;
bool cmp(ev e1, ev e2)
{
    return e1.bg < e2.bg;
}
void solveCaseBBig(int testCase)
{
    events.clear();
    int left1 = 720, left2 = 720;
    printf("Case #%d: ",testCase);
    int n, m;
    scanf("%d %d", &n, &m);
    int answer = n;
    for(int i=1;i<=n;i++)
    {
        int bg, en;
        scanf("%d%d",&bg,&en);
        left1 -= (en - bg);
        events.push_back(*new ev(bg, en, 1));
    }
    for(int i=1;i<=m;i++)
    {
        int bg, en;
        scanf("%d%d",&bg, &en);
        left2 -= (en - bg);
        events.push_back(*new ev(bg, en, 2));
    }
    sort(events.begin(), events.end(), cmp);
    int LEFT = left1;
    vector<int> jj, jc, cc;
    for(int i=0;i<events.size()-1;i++)
    {
        if(events[i].tp == events[i+1].tp)
        {
            if(events[i].tp == 1) {jj.push_back(events[i+1].bg - events[i].en);}
            else {cc.push_back(events[i+1].bg - events[i].en);}
        }
        else jc.push_back(events[i+1].bg - events[i].en);
    }
    if(events[n + m - 1].tp == events[0].tp)
    {
        if(events[0].tp == 1) jj.push_back(events[0].bg + 1440 - events[n+m-1].en);
        else {cc.push_back(events[0].bg + 1440 - events[n+m-1].en);}
    }
    else jc.push_back(events[0].bg + 1440 - events[n+m-1].en);
    sort(jj.begin(),jj.end());
    sort(jc.begin(),jc.end());
    sort(cc.begin(),cc.end());
    reverse(cc.begin(),cc.end());
    /*for(auto x:jj) printf("%d ",x);printf("\n");
    for(auto x:jc) printf("%d ",x);printf("\n");
    for(auto x:cc) printf("%d ",x);printf("\n");*/
    //printf("LEFT %d\n", LEFT);
    for(auto x: jj)
    {
        if(LEFT>=x)
        {
            LEFT-=x;
            answer--;
        }
        else
        {
            printf("%d\n",2*answer);
            return;
        }
        //printf("ANSWER %d LEFT %d\n", answer, LEFT);
    }
    for(auto x: jc)
    {
        if(LEFT>=x)
        {
            LEFT-=x;
        }
        else
        {
            printf("%d\n",2*answer);
            return;
        }
        //printf("ANSWER %d LEFT %d\n", answer, LEFT);
    }
    if(LEFT ==0)
        {
            printf("%d\n",2*answer);
            return;
        }
    for(auto x : cc)
    {
        int takes = min(x, LEFT);
        LEFT -= takes;
        answer ++;
        if(LEFT == 0)
        {
            printf("%d\n",answer*2);
            return;
        }
        //printf("ANSWER %d LEFT %d\n", answer, LEFT);
    }
    printf("%d\n",-1);
    return;
 }
