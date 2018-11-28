// Made By Haireden Aibyn
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define fname ""
#define INF 2147483647
#define MOD 1000000007
#define mp make_pair
#define F first
#define S second
#define sc scanf
#define all(x) x.begin(), x.end()
#define size(x) int(x.size())
#define pr printf
#define deb(x) cerr << " | " << #x << " = " << x
#define pb push_back
#define ex exit(0)
#define y1 y4

typedef long long ll;
typedef unsigned long long ull;

const int N = 100500;

string can(string s) {
       int pos = 0;
       for (int i = 0; i < size(s); ++i) {
           if (i != size(s) - 1) {
              if (s[i + 1] < s[i]) {
                 pos = i;
                 break;
              }
           } else {
              pos = size(s);
           }       
       }       
       if (pos == size(s)) return s;
       if (s[pos] == '1') return "";
       while (pos) {
             if (s[pos] - 1 >= s[pos - 1]) 
                 break;
             pos--;
       }
       if (s[pos] == '1') return "";
       string ans = "";
       for (int i = 0; i < pos; i++) ans += s[i];
       ans += char(s[pos] - 1); 
       for (int i = pos + 1; i < size(s); i++) ans += "9";
       return ans;
}

int main() {
    /*srand(time(NULL));
    #ifndef ONLINE_JUDGE
    freopen(fname".in", "r", stdin);
    freopen(fname".out", "w", stdout);
    #endif*/
    ios_base::sync_with_stdio(0);
    int test;
    cin >> test;
    for (int tt = 1; tt <= test; tt++) {
        string s;        
        cin >> s;
        string res = can(s);
        cout << "Case #" << tt << ": ";
        if (res != "") {
           cout << res;
        } else {
           for (int i = 0; i < size(s) - 1; i++) {
               cout << "9";           
           }
        }
        cout << endl;
    }
    #ifndef ONLINE_JUDGE
       cerr << clock() << " ms";
    #endif
    return 0;
}