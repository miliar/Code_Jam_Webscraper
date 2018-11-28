#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <map>
#include <cstdio>
#include <random>
#include <numeric>
#include <cstdlib>
#include <cassert>
#include <set>
#include <ctime>
#include <stack>
#include <cstring>
#include<functional>
#include <sstream>
#include <ctype.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
#pragma comment(linker, "/STACK:16777216")
template<typename T> T fac(T a) { return a ? a*fac(a - 1) : 1; }
template<typename T> T power(T a, int p) { return !p ? 1 : (p & 1 ? a*power(a, p - 1) : power(a*a, p >> 1)); }
template<typename T> T gcd(T a, T b) { return b ? gcd(b, a%b) : a; }
template<typename T> T lcm(T a, T b) { return b / gcd(a, b) * a; }
template<typename T> T next() { T _; cin >> _; return _; }
template<> int next<int>() { int _; scanf("%d", &_); return _; }
template<> double next<double>() { double _; scanf("%lf", &_); return _; }
template<> ll next<ll>() { ll _; scanf("%lld", &_); return _; }
template<typename E> vector<E> next(int n) { vector<E> res(n); for (int i = 0; i < n; i++) res[i] = next<E>(); return res; }
template<class C, class E> int count(const C &c, const E &e) { return count(c.begin(), c.end(), e); }
template<class E> bool has(const vector<E> &c, const E &e) { return find(c.begin(), c.end(), e) != c.end(); }
template<class E> int find(const vector<E> &c, const E &e) { return find(c.begin(), c.end(), e) - c.begin(); }
template<class E> bool binary_has(const vector<E> &c, const E &e) { return binary_search(c.begin(), c.end(), e); }
template<class E> int binary_find(const vector<E> &c, const E &e) { return lower_bound(c.begin(), c.end(), e) - c.begin(); }
template<typename T> T dist2(T i1, T j1, T i2, T j2) { return (i1 - i2)*(i1 - i2) + (j1 - j2)*(j1 - j2); }
bool ok(int i, int j, int n, int m) { return 0 <= i&&i<n && 0 <= j&&j<m; }
const double EPS = 1e-9;
const double PI = acos(-1);
bool LE(double a, double b) { return b - a > -EPS; }
bool BE(double a, double b) { return a - b > -EPS; }
bool EQ(double a, double b) { return fabs(a - b) < EPS; }
bool LESS(double a, double b) { return b - a > EPS; }
bool BIGG(double a, double b) { return a - b > EPS; }
typedef long long i64;
typedef unsigned long long u64;

string repeat(int c, string s)
{
    string res = "";
    while(c--)
        res += s;
    return res;
}

int max(int a, int b, int c)
{
    return max(max(a, b), c);
}

int main()
{
    freopen("/Users/ibra/Downloads/B-large (2).in", "r", stdin);
    freopen("/Users/ibra/Downloads/out.txt", "w", stdout);
    
	int t = next<int>();
    for(int test = 1; test <= t; test++)
    {
        int n = next<int>();
        
        int r = next<int>();
        int o = next<int>(); // b
        int y = next<int>();
        int g = next<int>(); // r
        int b = next<int>();
        int v = next<int>(); // y
        
        if(o+b == n)
        {
            if(o==b)
                cout << "Case #" << test << ": " << repeat(o, "OB") << endl; 
            else
                cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
            continue; 
        }
        
        if(g+r == n)
        {
            if(g==r)
                cout << "Case #" << test << ": " << repeat(g, "GR") << endl; 
            else
                cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
            continue; 
        }
        
        if(v+y == n)
        {
            if(v==y)
                cout << "Case #" << test << ": " << repeat(v, "VY") << endl; 
            else
                cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
            continue; 
        }
        
        if(o > 0 && b < o+1) {cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl; continue;}
        if(g > 0 && r < g+1) {cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl; continue;}
        if(v > 0 && y < v+1) {cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl; continue;}
        b -= o;
        r -= g;
        y -= v;
        
        string res = "";
        
        int bb = b;
        int rr = r;
        int yy = y;
        
        if(b == max(b, r, y))
        {
            res = 'B';
            b--;
        }
        else if(r == max(b, r, y))
        {
            res = 'R';
            r--;
        }
        else if(y == max(b, r, y))
        {
            res = 'Y';
            y--;
        } 
        
        while(b+r+y > 0)
        {
            if(res[res.size()-1] == 'B')
            {
                if(r > y || r==y && rr>yy)
                {
                    r--;
                    res += 'R';
                }
                else
                {
                    y--;
                    res += 'Y';
                }
            }
            else if(res[res.size()-1] == 'R')
            {
                if(b > y || b==y && bb>yy)
                {
                    b--;
                    res += 'B';
                }
                else
                {
                    y--;
                    res += 'Y';
                }
            }
            else if(res[res.size()-1] == 'Y')
            {
                if(r > b || r==b && rr>bb)
                {
                    r--;
                    res += 'R';
                }
                else
                {
                    b--;
                    res += 'B';
                }
            }
            else
            {
                res = "IMPOSSIBLE";
                break;
            }
            
            if(r < 0 || y < 0 || b < 0)
            {
                res = "IMPOSSIBLE";
                break;
            }
        }
        
        if(res == "IMPOSSIBLE")
        {
            cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
            continue;
        }
        
        for(int i = 0; i < res.size(); i++)
        {
            int j = (i+1)%res.size();
            if(res[i] == res[j])
            {
                res = "IMPOSSIBLE";
                break;
            }
        }
        
        if(res == "IMPOSSIBLE")
        {
            cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
            continue;
        }
        
        if(o > 0) // b
        {
            int i = 0;
            for(;i<res.size(); i++)
                if(res[i] == 'B')
                    break;
            res = string(res.begin(), res.begin()+i+1) + repeat(o, "OB") + string(res.begin()+i+1, res.end());
        }
        
        if(g > 0) // r
        {
            int i = 0;
            for(;i<res.size(); i++)
                if(res[i] == 'R')
                    break;
            res = string(res.begin(), res.begin()+i+1) + repeat(g, "GR") + string(res.begin()+i+1, res.end());
        }
        
        if(v > 0) // y
        {
            int i = 0;
            for(;i<res.size(); i++)
                if(res[i] == 'Y')
                    break;
            res = string(res.begin(), res.begin()+i+1) + repeat(v, "VY") + string(res.begin()+i+1, res.end());
        }
        
        
        
        
        
        
        cout << "Case #" << test << ": " << res << endl;
    }
    
	return 0;
}
