#include<bits/stdc++.h>
#define MOD 1000000007

/**
 *  Author : kaspers, Delhi Technological University
 */

#define mp(x,y) make_pair(x,y)
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define pi   3.14159265358979323846264338327950288
#define set0(a) memset(a,0,sizeof(a))
#define setN(a) memset(a,-1,sizeof(a))

using namespace std;

//Util Functions
template<class T> T gcd(T a,T b){if(b==0)return a;else return gcd(b,a%b);}
template<class T> T power(T a,T b){T result=1;while(b>0){if(b&1)	result = result * a;a = a*a;b>>=1;}return result;}
template<class T> T powerMod(T a,T b,T c){T result =1%c;while(b>0){if(b&1)result = (result * a)%c;a = (a*a)%c;b>>=1;}return result;}

typedef long long ll;
struct node {
    long double r, h;
};
bool compare(node l, node r) {
    return (l.r > r.r);
}
long double dp[1005][1005];
int N, K, H[1002][1002];
node A[1003];
long double f(int idx, int cakes) {
    if (cakes == K) {
        return 0.0;
    }
    if (idx == N) {
        return (-1e17);
    }

    if (H[idx][cakes] != 0) {
        return dp[idx][cakes];
    }
    long double res = f(idx + 1, cakes), tres = 0.0;
    if (cakes == 0) {
        tres = pi * A[idx].r * A[idx].r;
    }
    tres = tres + (2 * pi * A[idx].r * A[idx].h) + f(idx + 1, cakes + 1);
    H[idx][cakes] = 1;
    return dp[idx][cakes] = max(res, tres);
}
void eval()
{
    int i;
    set0(H);
    cin>>N>>K;
    for (i = 0; i < N; i++) {
        cin>>A[i].r>>A[i].h;
    }
    sort(A, A + N, compare);
    cout.precision(10);
    cout<<fixed<<f(0, 0)<<"\n";
}
int main()
{       freopen("input.txt","r",stdin);
    	freopen("output.txt","w",stdout);
    	cin.sync_with_stdio(0);
        cout.sync_with_stdio(0);
        int t, j = 1;
        cin>>t;
        while (t--) {
            cout<<"Case #"<<j++<<": ";
            eval();
        }
	return 0;
}
