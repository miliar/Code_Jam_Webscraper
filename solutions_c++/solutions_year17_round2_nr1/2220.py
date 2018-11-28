#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <stack>
#include <queue>
#include <set>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstdlib>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#define ri(X) scanf("%d", &(X))
#define rii(X, Y) scanf("%d%d", &(X), &(Y))
#define riii(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define all(a) (a).begin(),(a).end()

#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll;

int mod1 = int(1e9) + 7;

int main(){

    int t;
    ri(t);

    for(int cas=1; cas<=t; cas++) {

        double d;
        int n;
        cin >> d >> n;

        double t = 0;
        for(int i=0; i<n; i++) {
            double k,s;
            cin >> k >> s;
            t = max(t, (d-k)/s);
        }

        double ans = d/t;

        cout.precision(20);
        cout << "Case #" << cas << ": " << ans << endl;
    }

    return 0;
}
