//Round 1B 2017
#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define CLEAR(a) memset(a,0,sizeof a)
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define fr freopen("input.txt", "r", stdin);
#define fw freopen("output.txt", "w", stdout);
typedef long long LL;
typedef pair<int,int> pii;
const int MOD = 1e9 + 7;
const int MAX = 1e3 + 5;


// int solve(int idx, int f, int prev, int x, int y){
//     int z = idx-x-y;

//     if(x > a[1] || y > a[2] || z > a[3]) return 0;

//     if(dp[idx][f][prev][x][y] != -1) return dp[idx][f][prev][x][y];

//     if(idx == n){
//        if(f == prev) return 0;
//        return 1;
//     }

//     int ans = 0;

//     FOR(i, 1, 3){
//         if(i == prev) continue;
//         int nx = x, ny = y;
//         if(i == 1) nx++;
//         else if(i == 2) ny++;

//         if(idx == 0) ans |= solve(idx+1, i, i, nx, ny);
//         else ans |= solve(idx+1, f, i, nx, ny);
//     }

//     return dp[idx][f][prev][x][y] = ans;
// }

// char ch[] = {'R', 'Y', 'B'};

// void print(int idx, int f, int prev, int x, int y){

//     if(idx == n) return;

//     int pos, nnx, nny;

//     FOR(i, 1, 3){
//         if(i == prev) continue;
        
//         int nx = x, ny = y;
//         if(i == 1) nx++;
//         else if(i == 2) ny++;

//         int ret = 0;
        
//         if(idx == 0) ret = solve(idx+1, i, i, nx, ny);
//         else ret = solve(idx+1, f, i, nx, ny);

//         if(ret) {
//             pos = i;
//             nnx = nx;
//             nny = ny;
//         }
//     }

//     cout << ch[pos-1];
//     if(idx == 0) print(idx+1, pos, pos, nnx, nny);
//     else print(idx+1, f, pos, nnx, nny);
// }

char ch[] = {'R', 'Y', 'B'};

int n;
vector<pii> a;

int check(string s){
    REP(i, n){
        if(s[i] == s[(i+1)%s.size()]) return 0;
    }
    return 1;
}

void solve(){
    string ret = "";
    int flag = 1;
    REP(i, n) ret += '*';

    sort(a.begin(), a.end());

    int rev = 0;

    for(int i=2;i>=0;i--){
        int cnt = a[i].F;
        char c = ch[a[i].S];
        if(rev == 0){
        int j = 0;
        while(j < n && cnt){
            if(ret[j] == '*'){
                ret[j] = c;
                cnt--;
                j+=2;
            }
            else j++;
        }
       }
       else{
        int j = n-1;

        while(j >=0 && cnt){
            if(ret[j] == '*'){
                ret[j] = c;
                cnt--;
                j-=2;
            }
            else j--;
         }
        } 
        if(cnt) {
            flag = 0;
            break;
        }
        rev = 1- rev;
    }

    REP(i, n){
        if(ret[i] == '*'){
            flag = 0;
            break;
        }
    }
    if(flag == 0 || check(ret) == 0){

        cout <<"IMPOSSIBLE";
    }
    else{
        cout << ret;
    }
}

 main() {
    fr;fw;
    int cases = 1, T;
    cin >> T;
    while(T--){
       cin >> n;
       a.clear();
       int w = 0;
       REP(i, 6) {
        int x;
        cin >> x;
        if(i%2) continue;
        a.pb(mp(x, w++));
       }
       
      
       cout << "Case #"<<cases++ <<": ";
       solve();
       cout <<"\n";
    }
    return 0;
}