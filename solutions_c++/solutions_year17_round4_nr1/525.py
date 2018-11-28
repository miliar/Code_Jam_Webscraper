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
int dp[5][102][102][102], N, P;
int G[1000], B[101];
int f(int cur, int one, int two, int three) {
    int res = 0;
    if ((one + two + three) == 0) return 0;
    if (cur != 0) {
        res = 1;
    }
    if (dp[cur][one][two][three] != -1) return dp[cur][one][two][three];
    int res2 = 500;
    if (one > 0)
    res2 = min(res2, f((cur + 1) % P, one - 1, two, three));
    if (two > 0)
    res2 = min(res2, f((cur + 2) % P, one, two - 1, three));
    if (three > 0)
    res2 = min(res2, f((cur + 3) % P, one, two, three-1));
    res = res + res2;
    return dp[cur][one][two][three] = res;
}
void eval()
{
    int i;
    setN(dp);
    cin>>N>>P;
    B[1] = B[2] = B[3] = 0;
    for (i = 0; i < N; i++) {
        cin>>G[i];
        G[i] = G[i] % P;
        if (G[i] != 0)
        B[G[i]]++;
    }
    //trace3(B[1], B[2], B[3])
    cout<<N - f(0, B[1], B[2], B[3])<<"\n";
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
