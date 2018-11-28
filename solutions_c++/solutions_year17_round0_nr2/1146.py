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

int t;
string s;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("test.txt", "r", stdin);
    freopen("B.out", "w", stdout);
    cin >> t;
    FOR(k,1,t+1) {
        cin >> s;
        FOR(i,0,s.length() - 1) {
            if (s[i] > s[i + 1]) {
                s[i]--;
                FOR(j,i + 1,s.length()) s[j] = '9';
                i = -1;
            }
        }
        printf("Case #%d: %lld\n", k, atoll(s.c_str()));
    }
}