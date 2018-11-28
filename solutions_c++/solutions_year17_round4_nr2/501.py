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
int res2, N, C;
int Roll[10010], Per[1021], P[1021], B[1021], maxima;
int check(int mid) {
    if (mid < maxima) {
        return 0;
    }
    int carry = 0, res1, i;
    res1 = res2 = 0;
    for (i = N - 1; i >= 0; i--) {
        if (Roll[i] < mid) {
            carry = max(0, carry - (mid - Roll[i]));
        } else {
            carry = carry + Roll[i] - mid;
            res2 += (Roll[i] - mid);
        }
    }

    if (carry == 0) {
        return 1;
    } else {
        return 0;
    }
}
void eval()
{
    int M, st, en, mid, num1, num2, ans, i;
     maxima = 0;
    set0(Roll);
    set0(Per);
    cin>>N>>C>>M;
    for (i = 0; i < M; i++) {
        cin>>P[i]>>B[i];
        P[i]--;
        B[i]--;
        Roll[P[i]]++;
        Per[B[i]]++;
    }

    for (i = 0; i < C; i++) {
        maxima = max(maxima, Per[i]);
    }

    st = maxima;
    en = M;

    while (en >= st) {
        mid = (st + en) >> 1;
        num1 = check(mid);
        num2 = check(mid - 1);

        if (num1 && !num2) {
            ans = mid;
            break;
        }
        if (num1) {
            en = mid - 1;
        } else {
            st = mid + 1;
        }
    }


    check(ans);
    cout<<ans<<" "<<res2<<"\n";
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
