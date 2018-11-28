#include<iostream>
#include<cstdio>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<algorithm>
#include<map>
#include<iomanip>
#include<cstring>
#include<stdlib.h>
#include<climits>
#include<bitset>
#include<cstdint>
#include<stack>
#include<queue>
#define fi first
#define se second
#define pb push_back
#define oo (1<<30)
#define fr(i,N) for(int i=0;i<N;i++)
#define frr(i,N) for(int i=N;i>=0;i--)
#define fro(i,N) for(int i=1;i<=N;i++)
#define endall(x) return cout<<x<<endl,0;
#define CLR(x) memset(x, -1, sizeof x);
using namespace std;
typedef long double LD;
typedef long long int LL;
typedef pair<int,int> pii;
typedef pair<LL,int> pli;
typedef vector<int> vi;
const int dx[] = {0, -1,  0, 1, -1, 1,  1, -1};
const int dy[] = {1,  0, -1, 0,  1, 1, -1, -1};
const double EPS = 1e-9;
const long double PI = 3.1415926535897932384L;
const long long int INF64 = 9223372036854775807;
const int INF32 = 2147483647;
const int MOD = 1000000000+7;
const int MAX = 10000000+7;
map<int, bool> tidy;

bool check(int x){
    string s;
    while(x){
        s += ((x % 10) + '0');
        x /= 10;
    }
    int cnt = 0;
    reverse(s.begin(), s.end());
    for(int i = 0; i < s.size() - 1; i++){
        int now = s[i];
        int next = s[i + 1];
        if(now <= next)
            cnt++;
        else return false;
    }
    return true;
}

int main(){
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    freopen("B-small-attempt5.in","r",stdin);
    freopen("out2.out","w",stdout);
    for(int i = 0; i < 1000; i++)
        if(check(i))
            tidy[i] = true;
    int t;
    cin >> t;
    int c = 1;
    while(t--){
        int x;
        cin >> x;
        do{
            if(tidy[x]){
                cout << "Case #" << c++ << ": " << x << endl;
                break;
            }
        }while(x--);
    }
}
