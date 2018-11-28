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
long double P[1002], U;
int N;
bool check(long double num) {
    int i;
    long double res = 0.0;
    for (i = 0; i < N; i++) {
        if (P[i] < num) {
            res = res + (num - P[i]);
        }
    }
    if (res > U) {
        return 0;
    } else {
        return 1;
    }
}
void eval()
{
    int K, i;
    long double st, en, mid;
    int res ;
    cin>>N>>K;
    cin>>U;
    for (i = 0; i < N; i++) {
        cin>>P[i];
    }
    st = 0.0;
    en = 1.0;

    while ((en - st) >= 1e-15) {
        mid = (st + en) / 2.0l;
        res = check(mid);
        if (res == 0) {
            en = mid;
        } else {
            st = mid;
        }
    }
   // trace1(mid);
    long double fres = 1.0;
    for (i = 0; i < N; i++) {
        if (P[i] > mid) {
            fres = fres * P[i];
        } else {
            fres = fres * mid;
        }
    }
    cout.precision(10);
    cout<<fixed<<fres<<"\n";
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
