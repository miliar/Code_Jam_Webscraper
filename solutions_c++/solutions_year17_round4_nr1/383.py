#include <bits/stdc++.h>
using namespace std;

#define loop(i,n) for(int i = 0;i < int(n);i++)
#define rloop(i,n) for(int i = int(n);i >= 0;i--)
#define range(i,a,b) for(int i = int(a);i <= int(b);i++)
#define SZ(c) int(c.size())
#define ALL(c) c.begin(), c.end()
#define RALL(c) c.rbegin(), c.rend()
#define PI acos(-1)
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define sfi1(v) scanf("%d",&v)
#define sfi2(v1,v2) scanf("%d %d",&v1,&v2)
#define sfi3(v1,v2,v3) scanf("%d %d %d",&v1,&v2,&v3)
#define sfll1(v) scanf("%I64d",&v);
#define sfll2(v1,v2) scanf("%I64d %I64d",&v1,&v2)
#define sfll3(v1,v2,v3) scanf("%I64d %I64d %I64d",&v1,&v2,&v3)

typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long ll;
typedef pair<int, int> pii;

const int N = 105;
int v[N];
int m[6];

int main()
{


	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    int t;
    sfi1(t);
    range(T,1,t){
        memset(m,0,sizeof m);
        int n , p;
        sfi2(n,p);
        loop(i,n)sfi1(v[i]);
        loop(i,n)v[i]%= p;
        loop(i,n)m[v[i]]++;
        int ans = 0;
        if(p == 2){
            ans += m[0];
            ans += (m[1]/2);
            m[1] -= (m[1]/2) * 2;
            if(m[1])ans++;
        }else if(p == 3){
            ans += m[0];
            int mn = min(m[1],m[2]);
            ans += mn;
            m[1] -= mn;
            m[2] -= mn;

            //three ones
            mn = m[1]/3;
            ans += mn;
            m[1] -= mn*3;

            //three twos
            mn = m[2]/3;
            ans += mn;
            m[2] -= mn*3;

            if(m[1] || m[2])ans++;
        }else{
            ans += m[0];
            //2
            ans += (m[2]/2);
            m[2] -= (m[2]/2) * 2;

            //1-3
            int mn = min(m[1],m[3]);
            ans += mn;
            m[1] -= mn;
            m[3] -= mn;
            if(m[2] && m[1] >= 2){
                ans++;
                m[2] = 0;
                m[1] -= 2;
            }

            //1
            ans += (m[1]/4);
            m[1] -= (m[1]/4)*4;

            //2-3
            if(m[2] && m[3] >= 2){
                ans++;
                m[2] = 0;
                m[3] -= 2;
            }

            //3
            ans += (m[3]/4);
            m[3] -= (m[3]/4)*4;

            if(m[1] || m[2] || m[3])ans++;
        }
        printf("Case #%d: %d\n",T,min(ans, n));
    }


    return 0;
}
