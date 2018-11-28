#include <cstring>
#include <cmath>
#include <climits>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <functional>
#include <utility>
using namespace std;
const long inf = 1000000021L*1000000021L;
int testcase;

vector<string> mods;
char grid[100][100];
void add(char c, int y, int x)
{
    grid[y][x] = c;
    string s = "";
    s = " " + to_string(y+1) + " " + to_string(x+1) + "\n";
    for(int i = 0; i < mods.size(); i++)
    {
        if(mods[i] == ("x" + s) || mods[i] == ('+' + s))
        {
            mods[i] = c + s;
            return;
        }
    }
    mods.push_back(c + s);
}

void solve()
{
    mods.clear();
    long N,M;
    cin >> N >> M;
    for(int y = 0; y < N; y++)
        for(int x = 0; x < N; x++)
            grid[y][x] = '.';

    vector<int> rooksRows(N);
    vector<int> rooksCols(N);
    vector<int> bishopsForward(2*N-1);
    vector<int> bishopsBack(2*N-1);

    long R,C;
    string model;
    for(int m = 0; m < M; m++)
    {
        cin >> model >> R >> C;
        char c = model[0];
        R -= 1;
        C -= 1;
        grid[R][C] = c;
        if(c == 'x' || c == 'o')
        {
            rooksRows[R] = true;
            rooksCols[C] = true;
        }
        if(c == '+' || c == 'o')
        {
            bishopsForward[R+C] = true;
            bishopsBack[R-C+(N-1)] = true;
        }
    }
    if(N < 20)
    {
        cerr << "Case " << to_string(testcase) << "start \n";
        for(int y = 0; y < N; y++)
        {
            for(int x = 0; x < N; x++)
            {
                cerr << grid[y][x];
            }
            cerr << "\n";
        }
    }

    for(int y = 0; y < N; y++)
    {
        if(rooksRows[y])
            continue;
        for(int x = 0; x < N; x++)
        {
            if(rooksCols[x])
                continue;
            rooksRows[y] = true;
            rooksCols[x] = true;
            if(grid[y][x] == '+')
                add('o',y,x);
            else
                add('x',y,x);
            break;
        }
    }

    auto bishop = [&](int x, int y) {
        int d = y+x;
        int e = y-x + N-1;
        if(bishopsForward[d] || bishopsBack[e])
            return;
        bishopsForward[d] = true;
        bishopsBack[e] = true;
        if(grid[y][x] == 'x')
            add('o',y,x);
        else
            add('+',y,x);
    };

    int x1 = 0, x2 = N-1, y1 = 0, y2 = N-1;
    while(x1 <= x2 && y1 <= y2)
    {
        for(int x = x1; x <= x2; x++)
            bishop(x, y1);
        y1 += 1;
        for(int y = y1; y <= y2; y++)
            bishop(x2, y);
        x2 -= 1;
        for(int x = x2; x >= x1; x--)
            bishop(x, y2);
        y2 -= 1;
        for(int y = y2; y >= y1; y--)
            bishop(x1, y);
        x1 += 1;
    }


    if(N < 20)
    {
        cerr << "Case " << to_string(testcase) << "\n";
        for(int y = 0; y < N; y++)
        {
            for(int x = 0; x < N; x++)
            {
                cerr << grid[y][x];
            }
            cerr << "\n";
        }
    }

    if(N == 1)
        cout << 2 << " " << mods.size() << "\n";
    else
    {
        int score = 0;
        for(int i : rooksRows)
            if(i)
                score += 1;
        for(int i : bishopsForward)
            if(i)
                score += 1;
        cout << score << " " << mods.size() << "\n";
    }
    for(string s : mods)
        cout << s;

}

int main()
{
    cout.precision(10);
    int T;
    cin >> T;
    for(testcase = 1; testcase <= T; testcase++)
    {
        cout << "Case #" << testcase << ": ";
        solve();
    }
    return 0;
}

