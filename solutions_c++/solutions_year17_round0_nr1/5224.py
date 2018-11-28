#include <bits/stdc++.h>
using namespace std;
#define readfiles freopen("/home/andrewiski/NetBeansProjects/ACM/in.txt","r",stdin);freopen("/home/andrewiski/NetBeansProjects/ACM/out.txt","w",stdout)
#define clr(x,y) memset(x,y,sizeof(x))
#define pb push_back
#define mp make_pair
#define eps (1e-9)
#define oo (0x7fffffff)
#define OO (0x7fffffffffffffff)
#define PI acos(-1)
#define sqr(x) ((x)*(x))
#define moder (1000000007l)
#define ABS(x) ((x>0)?x:-x)
#define LOG2(x) ((log10(x))/(log10(2)))
#define UNSET(n,x) (n&(~(1 << x)))
#define SET(n,x) (n|(1<<x))
typedef long long int ll;
typedef unsigned long long int ull;
#define MAXN 7

int mn = 2000;
int k;

int check(string s) {
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '-') {
            return 0;
        }
    }
    return 1;
}

char flip(char c) {
    if (c == '+')
        return '-';
    else
        return '+';
}

void func(string s, int steps, int idx) {
    if (check(s)) {
        mn = min(mn, steps);
    } else {
        for (int i = idx; i < ((int) s.length()) - k+1; i++) {
            string temp = s;
            for (int j = 0; j < k; j++) {
                temp[i + j] = flip(temp[i + j]);
            }
            func(temp, steps + 1, i+1);
        }
    }
}

void solve() {
    int cases;
    cin>>cases;
    int c=0;
    while (cases--) {
        c++;
        mn = 2000;
        string s;
        cin >> s>>k;
        func(s, 0, 0);
        cout<<"Case #"<<c<<": ";
        if (mn != 2000)
            cout << mn << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
   // readfiles;
#ifndef ONLINE_JUDGE

    //  double begin = clock();
#endif
    solve();
    return 0;
#ifndef ONLINE_JUDGE
    //  printf("%.4f", (clock() - begin) / CLOCKS_PER_SEC);
#endif
}