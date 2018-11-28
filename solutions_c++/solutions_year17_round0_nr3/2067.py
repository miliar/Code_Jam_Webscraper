#include <bits/stdc++.h>
#include <tr1/unordered_map>
typedef long long ll;
typedef unsigned long long ull;
#define clr(ma) memset(ma,-1,sizeof ma)
#define inf 1000000000
#define vi vector<int>
#define pi pair<int  ,int >
#define mk make_pair
#define getBit(m,i) ((m&(1<<i))==(1<<i))
#define setBit(m,i) (m|(1<<i))
#define setBit2(m,i) (m|(1ull<<i))
#define cont(i,ma) ((ma.find(i))!=(ma.end()))
#define in(i) scanf("%d",&i)
#define in2(i,j) scanf("%d%d",&i,&j)
#define in3(i,j,k) scanf("%d%d%d",&i,&j,&k)
#define in4(i,j,k,l) scanf("%d%d%d%d",&i,&j,&k,&l)
#define il(i) scanf("%I64d",&i)
#define itr map<ll,ll>::iterator
#define itr2 map<ll,map<ll,ll> >::iterator
#define id(k) scanf("%9lf",&k)
#define fi(ss) freopen (ss,"r",stdin)
#define fo(ss) freopen (ss,"w",stdout)
#define clean(vis)  memset(vis,0,sizeof vis)
#define mo(x) ((x)<P?(x):(x)-P)
#define mo2(x) ((x)>=0?(x):(x)+P)
#define fast ios_base::sync_with_stdio(0);cin.tie(0);
#define sc(s)  scanf("%s",s)
using namespace std;
struct Pair {
    int l, r;

    Pair(int a = 0, int b = 0) {
        l = a;
        r = b;
    }

    bool operator<(Pair p) const {
        if (p.r - p.l == r - l)
            return l > p.l;
        return (p.r - p.l) > (r - l);
    }
};
int  main()  {
        fi("/home/mohamedatef/ClionProjects/untitled1/input.txt");
        fo("/home/mohamedatef/ClionProjects/untitled1/out.txt");

        int t , n, k, cases = 1;
        in(t);
        priority_queue<Pair> pq ;

        while(t-- > 0) {
            in2(n, k);
            while (!pq.empty())pq.pop();
            pq.push(Pair(0, n - 1));

            while (k-- > 1) {
                Pair p = pq.top();
                pq.pop();
                int mid = (p.l + p.r) >> 1;

                pq.push(Pair(p.l, mid - 1));
                pq.push(Pair(mid + 1, p.r));
            }

            Pair p = pq.top();
            pq.pop();
            int mid = (p.l + p.r) >> 1;
            int a = (mid - 1) - p.l + 1;
            int b = p.r - (mid + 1) + 1;
            if (a < 0) a = 0;
            if (b < 0) b = 0;

            printf("Case #%d: %d %d\n", cases++, max(a, b), min(a, b));
        }
}

