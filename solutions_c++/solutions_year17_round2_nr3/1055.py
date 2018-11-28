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
ll N, Sum[10010];
long double S[100100];
ll E[100100];
ll D[1001][1002];
ll K[1001][1001];
long double dp[1001][1001];
long double f(ll idx, ll horse) {
    if (idx == N - 1) return 0;
    if (K[idx][horse] != -1) return dp[idx][horse];
    ll dist;
    long double res = 1e12;
    if (idx == 0) {
        dist = Sum[idx + 1];
    } else {
        dist = Sum[idx + 1] - Sum[idx];
    }
    if (E[idx] >= dist) {
     res = (((long double)D[idx][idx + 1])/S[idx]) +  f(idx + 1, idx);
    }

    if (horse == 0) {
        dist = Sum[idx + 1];
    } else {
        dist = Sum[idx + 1] - Sum[horse];
    }
    if (E[horse] >= (dist)) {
        res = min(res,  (((long double)D[idx][idx + 1])/S[horse]) +  f(idx + 1, horse));
    }
    K[idx][horse] = 1;
    return dp[idx][horse] = res;
}

void eval()
{
    ll i, U, V, Q, j;
   setN(K);
   cin>>N>>Q;
   for (i = 0; i < N; i++) {
        cin>>E[i]>>S[i];
   }
   for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            cin>>D[i][j];
        }
   }
   while (Q--) {
        cin>>U>>V;
        Sum[0] = 0;
        for (i = 1; i < N; i++) {
            Sum[i] = Sum[i - 1] + D[i - 1][i];
        }
        cout.precision(10);
        cout<<fixed<<f(0, 0)<<"\n";
   }
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
