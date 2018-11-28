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

int numCases, N, K;

int distLeft(vb &stalls, int pos) {
    for (int a = pos; a >= 0; a--)
        if (stalls[a]) return pos - a;
    return -1;
}

int distRight(vb &stalls, int pos) {
    for (int a = pos; a <= N+1; a++)
        if (stalls[a]) return a - pos;
    return -1;
}

int main() {
#ifdef __APPLE__
    ifstream cin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream cout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
    FILE* outputReadFile = fopen("/Users/byunghoon/Desktop/Programs/Programs/out.txt","r");
#endif

    cin >> numCases;
    
    for (int i = 0; i < numCases; i++) {
        cin >> N >> K;
        cout << "Case #" << (i+1) << ": ";
        
        vb stalls(N+2, false);
        stalls[0] = true;
        stalls[N+1] = true;
        
        int maxAns = -1;
        
        for (int j = 0; j < K; j++) {
            maxAns = -1;
            vector<iii> possibles;
            for (int k = 1; k <= N; k++) {
                if (stalls[k]) continue;
                int LS = distLeft(stalls, k);
                int RS = distRight(stalls, k);
                
                if (min(LS, RS) == maxAns) {
                    possibles.push_back(iii(ii(LS, RS), k));
                } else if (min(LS, RS) > maxAns) {
                    possibles = vector<iii>(1, iii(ii(LS, RS), k));
                    maxAns = min(LS, RS);
                }
                
//                printf("Stall %d: %d, %d: %d\n", k, LS, RS, min(LS, RS));
            }
//            printf("Size: %d\n", possibles.size());
            int ans1, ans2;
            if (possibles.size() == 1) {
                ans1 = max(possibles[0].first.first, possibles[0].first.second);
                ans2 = min(possibles[0].first.first, possibles[0].first.second);
                stalls[possibles[0].second] = true;
            } else {
                int minAns = 0;
                int minPos = -1;
                for (int k = 0; k < possibles.size(); k++) {
                    int mx = max(possibles[k].first.first, possibles[k].first.second);
                    int mn = min(possibles[k].first.first, possibles[k].first.second);
                    if (minAns < mx) {
                        minAns = mx;
                        minPos = possibles[k].second;
                        ans1 = mx;
                        ans2 = mn;
                    }
                }
                stalls[minPos] = true;
            }
            
//            for (bool stall : stalls)
//                cout << (stall ? "o" : ".");
//            cout << endl;
            
            if (j == K - 1) {
                cout << (ans1-1) << " " << (ans2-1) << endl;
            }
        }
    }
    
#ifdef __APPLE__
    fclose(outputReadFile);
#endif
    
    return 0;
}
