#include<bits/stdc++.h>
#define MOD 1000000007

/**
 *  Author : kaspers, Delhi Technological University
 */

#define mp(x,y) make_pair(x,y)
#define trace1(x)                cout << #x << ": " << x << endl;
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
set<ll> S;
set<ll> ::iterator it;
map<ll, ll> H;

void eval()
{
    S.clear();
    H.clear();
    ll N, K, i, div, div1, div2, res1, res2, largest, maxSize = 0;
    cin>>N>>K;
    H[N] = 1;
    S.insert(N);
    while (1) {
        it = S.end();
        it--;
        largest = *(it);

        S.erase(largest);

        if (largest & 1ll) {

            div = largest >> 1ll;

            if (div > 0) {
                if (H[div] == 0) {
                    S.insert(div);
                }

                H[div] += (2ll * H[largest]);

            }
            if (H[largest] >= K) {
                res1 = res2 = div;
                break;
            }
            K = K - H[largest];
            H[largest] = 0;

        } else {
            div1 = ((largest >> 1ll));
            div2 = ((largest - 1ll) >> 1ll);
            if (H[largest] >= K) {
                res1 = div1;
                res2 = div2;
                break;
            }

            K = K - H[largest];
            if (div1 > 0) {
                if (H[div1] == 0) {
                    S.insert(div1);
                }
                H[div1] += H[largest];
            }

            if (div2 > 0) {
                if (H[div2] == 0) {
                    S.insert(div2);
                }
                H[div2] += H[largest];
            }
            H[largest] = 0;
        }

    }

    cout<<res1<<" "<<res2<<"\n";

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
