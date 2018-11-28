#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef double flt;

struct Horse
{
    int start, speed;
};

void solve(int test_number)
{
    int d, n;
    cin >> d >> n;
    vector<Horse> horses;
    for (int q = 0; q < n; ++q)
    {
        int a, b;
        cin >> a >> b;
        horses.push_back({a, b});
    }
    
    sort(horses.begin(), horses.end(), [] (const Horse &a, const Horse &b) {
        return a.start < b.start;
    });
    
    flt start = horses[0].start, speed = horses[0].speed;
    for (int q = 1; q < (int)horses.size(); ++q)
    {
        if (horses[q].speed > speed)
            continue;
        flt time = (horses[q].start - start) / (speed - horses[q].speed);
        flt pos = start + speed * time;
        if (pos < d)
        {
            start = horses[q].start;
            speed = horses[q].speed;
        }
    }
    flt time = (d - start) / speed;
    cout.precision(10);
    cout << "Case #" << test_number << ": " << d / time << endl;
}

int main()
{
//  /*
    freopen("A-large.in", "r", stdin);
//  */
    
    int cnt_tests;
    cin >> cnt_tests;
    for (int _q = 0; _q < cnt_tests; ++_q)
    {
        solve(_q + 1);
    }
    
    
    return 0;
}
