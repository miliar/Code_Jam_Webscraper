#define _SCL_SECURE_NO_WARNINGS
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <ctime>
#include <cmath>
#include <map>
#include <unordered_map>
#include <list>
#include <set>
#include <random>
#include <stack>
#include <sstream>
#include <iterator>
#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;



stack <time_t> time_stack;
void startTimer()
{
    time_stack.push(clock());
}
double stopTimer()
{
    double time = clock() - time_stack.top();
    time_stack.pop();
    return time / double(CLOCKS_PER_SEC);
}



#define MAXN 2000
#define MAXM 10010
#define MAXQ 901
#define MAXK 100
#define MAXL 2001
#define INF int(2e9)
#define LLINF ll(1e18)
#define MOD 1000000000
#define EPS double(1e-9)
#define LAM double(1e-6)
#define PI double(3.14159265359)
#define mp make_pair
#define CUBE(x) (x) * (x)
#define SQ(x) (x) * (x)
#define MP(x, y) make_pair((x), (y))
#define X first
#define Y second

double sqr(double x)
{
    return x*x;
}




int main() {
    startTimer();
    ios::sync_with_stdio(false);
#ifdef _HOME_
    ifstream cin("input.txt");
    ofstream out("output.txt");
//    ofstream cout("output.txt");
    //freopen("output.txt", "w", stdout);
#else
    //ifstream cin("input.txt");
//    ofstream cout("output.txt");
    string TASK = "sum";
//    ifstream cin(TASK + ".in");
//    ofstream cout(TASK + ".out");
    //freopen("dfsongrid.out", "w", stdout);
#endif
    cout.precision(16); cout << fixed;

    int T;
    cin >> T;
    for (int test = 0; test < T; test++)
    {
        string s;
        cin >> s;
        reverse(s.begin(), s.end());

        while (true)
        {
            int n = s.size();

            bool cool = true;
            for (int i = 1; i < n && cool; i++)
                if (s[i] > s[i - 1])
                {
                    s[i]--;
                    for (int j = 0; j < i; j++)
                        s[j] = '9';

                    cool = false;
                }

            while (s.back() == '0')
                s.pop_back();

            if (cool)
                break;
        }

        reverse(s.begin(), s.end());


        out << "Case #" << test + 1 << ": " << s << endl;
    }



    cout << endl;
#ifdef _HOME_
    cout.precision(3);
    cout << endl << fixed << stopTimer() << "s\n";
    //system("pause");
#endif

    return 0;
}