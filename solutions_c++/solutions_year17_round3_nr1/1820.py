#include<bits/stdc++.h>
using namespace std;
#define li long long int
#define ii pair<li,li>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define vi vector<li>
#define vii vector<ii>
#define INF 9999999999999
#define MAXN 100005
#define sz size()
#define ins insert
template <class T>
void fastread(T &a)
{
    static char c;
    static int fh;
    while (((c = getchar()) < '0' || c > '9') && c != '-');
    if (c == '-') fh = -1, a = 0;
    else fh = 1, a = c - '0';
    while ((c = getchar()) <= '9' && c >= '0') a = (a << 3) + (a << 1) + c - '0';
    a = a * fh;
}
template <class T>
void write(T a)
{
    if (a == 0) putchar('0');
    else
    {
        if (a < 0) putchar('-'), a = -a;
        static char c[30];
        static int c0;
        c0 = 0;
        while (a) c[++c0] = a % 10 + '0', a /= 10;
        while (c0) putchar(c[c0--]);
    }
}
#define pi 3.14159265359
li n;
ii a[1005];
li memoise[1005][1005][2];
li solution(li i,li k,bool f)
{
    if(i<0 || k==0) { return 0; }
    if(memoise[i][k][f]!=-1) {  return memoise[i][k][f]; }
    if(f)
    {
        return memoise[i][k][f]=max(a[i].fi*a[i].fi+2*a[i].fi*a[i].se+solution(i-1,k-1,0),solution(i-1,k,1));
    }
    return memoise[i][k][f]=max(2*a[i].fi*a[i].se+solution(i-1,k-1,0),solution(i-1,k,0));
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    li testing; fastread(testing);
    for(li testcase=1;testcase<=testing;testcase++)
    {
        li k,i,j; fastread(n); fastread(k);
        for(i=0;i<n;i++) { fastread(a[i].fi); fastread(a[i].se); }
        for(i=0;i<=n;i++) for(j=0;j<=n;j++) memoise[i][j][0]=memoise[i][j][1]=-1;
        sort(a,a+n);
        double ans=(double)solution(n-1,k,1);
        cout<<"Case #"<<testcase<<": "<<setprecision(30)<<(double)pi*ans<<endl;
    }
    return 0;
}
