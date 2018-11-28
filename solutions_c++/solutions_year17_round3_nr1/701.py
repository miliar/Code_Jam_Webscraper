#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef double dd;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

#define FOR(i,a,b) for (int (i) = (a); (i) < (b); (i)++)
#define DOW(i,b,a) for (int i = (b); i >= (a); i--)
#define pb(a) push_back(a)
#define ALL(a) (a).begin(),(a).end()
#define fi first
#define se second

template<typename T>
void print_array(T* arr, int num) {
   FOR(i, 0, num) cout << arr[i] << ' ';
   cout << endl;
}

template<typename T> 
void print_vector(vector<T> vec) {
   FOR(i,0,vec.size()) cout << vec[i] << ' ';
   cout << endl;
}

const dd PI = acos(-1.0);
int tc,n,k;
pair<dd,int> arr[1010];
dd area[1010];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("test.txt", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &tc);
    FOR(c,1,tc+1) {
        scanf("%d %d", &n, &k);
        FOR(i,0,n) {
            int r,h;
            scanf("%d %d", &r, &h);
            arr[i] = make_pair((dd)h * r * 2 * PI, i);
            area[i] = (dd)r * r * PI;
        }
        dd ans = 0.0;
        sort(arr,arr + n,greater<pair<dd,int>>());
        FOR(i,0,n) {
            int idx = arr[i].se;
            dd cur = area[idx] + arr[i].fi;
            int a = k - 1;
            FOR(j,0,a) {
                if (j == i) a++;
                else cur += arr[j].fi;
            }
            ans = max(ans, cur);
        }
        printf("Case #%d: %.9f\n", c, ans);
    }
}