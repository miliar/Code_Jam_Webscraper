#include </Users/byunghoon/Desktop/Programs/bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef pair<ii, ii> iiii;
typedef pair<int, bool> ib;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vb> vvb;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<pll> vpll;

bool isTidy(int n) {
    int prevDigit = 10;
    while (n > 0) {
        int digit = n % 10;
        n /= 10;
        if (digit > prevDigit) return false;
        prevDigit = digit;
    }
    return true;
}

int main() {
#ifdef __APPLE__
    ifstream cin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream cout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
    FILE* outputReadFile = fopen("/Users/byunghoon/Desktop/Programs/Programs/out.txt","r");
#endif

    int numCases;
    cin >> numCases;
    
    for (int i = 0; i < numCases; i++) {
        int N;
        cin >> N;
        cout << "Case #" << (i+1) << ": ";
        
        for (int j = N; j >= 1; j--) {
            if (isTidy(j)) {
                cout << j << endl;
                break;
            }
        }
    }
    
#ifdef __APPLE__
    fclose(outputReadFile);
#endif
    
    return 0;
}
