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
pair<int, int> A[100];
int B[100100];
void eval()
{
    int n, r, o, y, g, b, v, i;
    cin>>n>>r>>o>>y>>g>>b>>v;
    A[0] = mp(r, 0);
    A[1] = mp(y, 1);
    A[2] = mp(b, 2);
    for (i = 0; i < n; i++) {
        sort(A, A + 3);
        if (i == 0) {
            B[i] = A[2].second;
            A[2].first--;
        } else {
            if (B[i - 1] == A[2].second) {
                B[i] = A[1].second;
                A[1].first--;
                if (A[1].first < 0) {
                   cout<<"IMPOSSIBLE\n";
                    return;
                }
            } else {
                B[i] = A[2].second;
                A[2].first--;
            }
        }
    }
    if (B[0] == B[n - 1]) {
            int t = B[n - 1];
            B[n - 1] = B[n - 2];
            B[n - 2] = t;

    }
    for (i = 0; i < n; i++) {
        if (i == 0) {
            if (B[n - 1] == B[i]) {
                cout<<"IMPOSSIBLE\n";
                return;
            }
        } else {
            if (B[i] == B[i - 1]) {
                cout<<"IMPOSSIBLE\n";
                return;
            }
        }
    }
    for (i = 0; i < n; i++) {
        if (B[i] == 0) {
            cout<<"R";
        }
        if (B[i] == 1)
        {
            cout<<"Y";
        }
        if (B[i] == 2) {
            cout<<"B";
        }
    }
    cout<<"\n";

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
