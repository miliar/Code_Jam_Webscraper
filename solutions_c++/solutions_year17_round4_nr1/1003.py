#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <assert.h>     /* assert */


#define _CRT_SECURE_NO_WARNINGS
using namespace std;

typedef long long ll;
const double pi=acos(-1.0);
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
typedef map<string, int> simp;
#define sz(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define rep(i,b) for(int i=0;i<b;i++)
#define For(i,a,b) for(int i=a;i<b;i++)
template<class T> inline void Swap(T &a,T &b){T c=a;a=b;b=c;}
#define Sort(v) sort((v).begin(), (v).end())
#define Uni(v) Sort(v),(v).erase(unique((v).begin(), (v).end()), (v).end())
#define cl(a,b) memset(a,b,sizeof(a))

const int oo=1000000;

#pragma warning(disable:4996)

#define QX "A"

int main()
{
//	freopen(QX ".txt","r",stdin);
//	freopen(QX "-small-attempt0.in","r",stdin);freopen(QX "-small-attempt0.out","w",stdout);
//	freopen(QX "-small-attempt1.in","r",stdin);freopen(QX "-small-attempt1.out","w",stdout);
	freopen(QX "-large.in","r",stdin);freopen(QX "-large.out","w",stdout);
//	freopen(QX "-large-practice.in","r",stdin);freopen(QX "-large-practice.out","w",stdout);

    int T=0;
	scanf("%d",&T);

	for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        int N,P;
        cin>>N>>P;
        int cc[4];
        cl(cc,0);
        rep(i,N) {
            int n;
            cin>>n;
            cc[n%P]++;
        }

        int ans = cc[0];
        if (P == 2) {
            ans += (cc[1]+1) / 2;
        } else if (P == 3) {
            // group of size 2: [1 2]
            ans += min(cc[1], cc[2]);
            // group of size 3: [1 1 1] or [2 2 2]
            if (cc[1] > cc[2]) {
                cc[1] -= cc[2];
                ans += (cc[1] + 2) / 3;
            } else {
                cc[2] -= cc[1];
                ans += (cc[2] + 2) / 3;
            }
        } else if (P == 4) {
            // group size of 2: [2 2] or [1 3]
            ans += cc[2] / 2;
            cc[2] %= 2;
            int cc13 = min(cc[1], cc[3]);
            ans += cc13;
            // put leftover as 1 (1 is the same as 3)
            cc[1] = max(cc[1],cc[3]) - cc13;
            cc[3] = 0;
            // group size of 3: [1 1 2] or [3 3 2]
            if (cc[2] > 0 && cc[1] >= 2) {
                cc[2] = 0;
                cc[1] -= 2;
                ans += 1;
            }
            // group size of 4: [1 1 1 1] or [3 3 3 3]
            ans += cc[1] / 4;
            cc[1] %= 4;
            if (cc[1] + cc[2] > 0) {
                ans += 1;
            }
        }

        // output
        cout << "Case #"<<caseId<<": "<<ans<<endl;
	}
    return 0;
}
