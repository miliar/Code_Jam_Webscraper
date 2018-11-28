

#include <iostream>
#include <cstdio>

using namespace std;
int a[20];
int b[20];
long long solve(string s)
{
    int len = s.size();
    for (int i = 0; i < len; ++i)
    {
        a[i] = s[i] - '0';
    }
    int mn = 0;
    for (int i = 0; i < len; ++i){
        if (a[i] >= mn){
            b[i] = a[i];
            mn = a[i];
        }else{
            b[i] = a[i];
            int cur = i;
            while(cur > 0 && b[cur] < b[cur - 1]){
                b[cur] = 9;
                b[cur - 1]--;
                cur--;
            }

            for (int j = i; j < len; ++j)
                b[j] = 9;
            break;
        }
    }
    long long ans = 0;
    for (int i = 0; i < len; ++i)
        ans = ans * 10 + b[i];
    return ans;
}
int main(int argc, const char * argv[]) {
    freopen("/Users/Andrew/Desktop/GCJ2017/GCJ2017/A.txt", "r", stdin);
    freopen("/Users/Andrew/Desktop/GCJ2017/GCJ2017/Aans.txt", "w", stdout);
    int tests;
    cin >> tests;
    int testCounter = 1;
    string s;
    while (testCounter <= tests) {
        cin >> s;

        cout << "Case #" << testCounter << ": "  <<        solve(s) <<  endl;
        testCounter++;
    }
    return 0;
}
