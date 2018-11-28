#include<bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define SZ(v) (int)v.size()
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))
#define iter(it,s) for(__typeof(s.begin())it = s.begin();it!=s.end();it++)
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

const int OO = (int) 2e9;
const double eps = 1e-9;

// 1 based
int daysInMonths[] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };
#define Nd 0
#define Ed 1
#define Sd 2
#define Wd 3

using namespace std;

int main()
{

    std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
#endif

    char s[1005];
    int t, k, c=0;
    scanf("%d", &t);
    while(t--){
        int flips=0;
        bool flag=true;
        c++;
        scanf("%s %d", s, &k);
        for(int i=0; i<strlen(s)-k+1; i++){
            if(s[i]=='-'){
                for(int j=i; j<i+k; j++){
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            flips++;
            }
        }
        for(int i=0; i<strlen(s); i++){
            if(s[i]=='-'){
                printf("Case #%d: IMPOSSIBLE\n", c);
                flag=false;
                break;
            }
        }
        if(flag)
            printf("Case #%d: %d\n", c, flips);
    }
    return 0;
}
