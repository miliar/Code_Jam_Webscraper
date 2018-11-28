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

ofstream fout ("C-Small-2.out");
ifstream fin ("C-small-2-attempt0.in");

#define cin fin
#define cout fout

int ans = 0 , n = 0 , k = 0;

multiset <int> s;

int main() {
	ios::sync_with_stdio(0);
	int t;
	cin >> t;

	for(int tt = 0; tt < t ;tt++){
        s.clear();
        cin >> n >> k;
        ans = 0;
        s.insert(-n);
        for(int i = 0 ; i < k-1;i++){
            int tp = *s.begin();
            s.erase(s.begin());
            tp = -tp;
            if(tp > 2){
                s.insert(-((tp-1)/2));
                s.insert(-(tp/2));
            }
            else{
                if(tp == 2){
                    s.insert(-1);
                }
            }
            //cerr << i << ' ' << *s.begin()<< endl;
        }

        ans = *s.begin();
        ans = -ans;
        //cerr << ans << endl;
        cout << "Case #" << tt+1 << ": " ;
        cout << (ans/2) << ' ' <<  ((ans-1)/2)<< endl;

	}
}
