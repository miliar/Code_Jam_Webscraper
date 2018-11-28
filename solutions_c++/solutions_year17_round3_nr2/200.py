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
int dp[1450][3][800], H[1500], cur, CTRJ, first;
int f(int idx, int pl, int CTRC) {

    if (H[idx] == pl || H[idx] == 0) {

        if (pl == 1) {
            CTRC++;
        }
        CTRJ = idx + 1 - CTRC;
        if (CTRJ > 720 || CTRC > 720) {
            return MOD;
        }
        int res = MOD, next;
        next = (idx + 1) % 1440;
        if (idx == 1439) {
            if (pl == first) {
                return 0;
            } else {
                return 1;
            }
        }
        if (dp[idx][pl][CTRC] != -1) {
            return dp[idx][pl][CTRC];
        }
        if (H[next] == 0 || H[next] == pl) {
            res = min(res, f(next, pl, CTRC));
            if (H[next] == 0) {
                res = min(res, 1 + f(next, 3 - pl, CTRC));
            }
        } else {
            res = min(res, 1 + f(next, 3 - pl, CTRC));
        }
        return dp[idx][pl][CTRC] = res;
    } else {
        return MOD;
    }
}
void eval()
{
    int S, E, Ac, Aj, i, j, res = MOD;
    cin>>Ac>>Aj;
    set0(H);

    for (i = 0; i < Ac; i++) {
        cin>>S>>E;
        for (j = S; j < E; j++) {
            H[j] = 1;
        }
    }
    for (i = 0; i < Aj; i++) {
        cin>>S>>E;
        for (j = S; j < E; j++) {
            H[j] = 2;
        }
    }


    cur = i;
    if (H[0] == 0 || H[0] == 1) {
        first = 1;
        setN(dp);
        res = f(0, 1, 0);
    }

    if (H[0] == 0 || H[0] == 2) {
        first = 2;
        setN(dp);
        res = min(res, f(0, 2, 0));
    }
    cout<<res<<"\n";
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
