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

int main() {
#ifdef __APPLE__
    ifstream cin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream cout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
    FILE* outputReadFile = fopen("/Users/byunghoon/Desktop/Programs/Programs/out.txt","r");
#endif

    int numCases;
    cin >> numCases;
    
    for (int i = 0; i < numCases; i++) {
        string pancakes;
        int k, ans = 0;
        cin >> pancakes >> k;
        
        for (int j = 0; j <= pancakes.length() - k; j++) {
            if (pancakes[j] == '+') continue;
            ans += 1;
            for (int a = 0; a < k; a++)
                pancakes[j + a] = pancakes[j + a] == '+' ? '-' : '+';
        }
        for (int j = pancakes.length() - k + 1; j < pancakes.length(); j++)
            if (pancakes[j] == '-') ans = -1;
        
        cout << "Case #" << (i+1) << ": ";
        if (ans == -1)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << ans << endl;
    }
    
#ifdef __APPLE__
    fclose(outputReadFile);
#endif
    
    return 0;
}
