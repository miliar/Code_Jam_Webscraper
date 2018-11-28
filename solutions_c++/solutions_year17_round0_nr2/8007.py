#include <bits/stdc++.h>
#define X first
#define Y second

#define bitAt(a,b) (a & (1<<b))

using namespace std;

typedef long long LL;
typedef pair <int, int> PII;
typedef pair <LL,LL> PLL;

const int Maxn = 100*1000 + 250;
const int Mod = 1000 * 1000 * 1000 + 7;
const int abMax = 1 << 30 ;
const double EPS = 1e-9;
const double PI = acos(-1.0);

ofstream fout ("B-Small.out");
ifstream fin ("B-small-attempt0.in");

#define cin fin
#define cout fout

bool isTidy (int n ){

    bool ret = true;

    int l = n%10;
    n = (n-l)/10;
    while(n>0){
        int r = n%10;
        if(l<r) ret = false;
        l = r;
        n = (n-l)/10;
    }
    return ret;
}

int n = 0 , ans = 0;

int main() {
	ios::sync_with_stdio(0);
	int t;
	cin >> t;
	for(int tt = 0; tt < t ;tt++){

        cin >> n;
        for(int i = n;i>0;i--){
            if(isTidy(i)){
                ans = i;
                break;
            }
        }

        cout << "Case #" << tt+1 << ": " ;
        cout << ans;
        cout << endl;
	}
}
