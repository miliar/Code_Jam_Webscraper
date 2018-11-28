#include <bits/stdc++.h>
using namespace std;

string part(int& n, int& k, char cn, char ck)
{
    string r = "";
    r.reserve(k*2 + 1);
    if(k <= n)
    {
        for(int i = 0; i < k; ++i)
        {
            r += cn;
            r += ck;
        }
        n -= k;
        k = 0;
    }
    if(n)
    {
        r += cn;
        n -= 1;
    }
    return r;
}

bool check(char a, char b)
{
    if(a == b) return false;
    if(a == 'O' && b != 'B') return false;
    if(b == 'O' && a != 'B') return false;
    if(a == 'V' && b != 'Y') return false;
    if(b == 'V' && a != 'Y') return false;
    if(a == 'G' && b != 'R') return false;
    if(b == 'G' && a != 'R') return false;
    return true;
}

string solve()
{
    int n, r, o, y, g, b, v; cin >> n >> r >> o >> y >> g >> b >> v;
    string rg = part( r, g, 'R', 'G');
    if(rg.length() && rg.back() != 'R')
        return rg.length() == n ? rg :"IMPOSSIBLE";
    string yv = part(y, v, 'Y', 'V');
    if(yv.length() && yv.back() != 'Y')
        return yv.length() == n ? yv :"IMPOSSIBLE";
    string bo = part(b, o, 'B', 'O');
    if(bo.length() && bo.back() != 'B')
        return bo.length() == n ? bo : "IMPOSSIBLE";
    if(rg.length()) r += 1;
    if(yv.length()) y += 1;
    if(bo.length()) b += 1;
    char prev = 0;

    int nn = r, mm = y, kk = b;
    int cn = 'R', cm = 'Y', ck = 'B';

    if(nn < mm)
    {
        swap(nn, mm);
        swap(cn, cm);
    }
    if(nn < kk)
    {
        swap(nn, kk);
        swap(cn, ck);
    }
    if(mm < kk)
    {
        swap(mm, kk);
        swap(cm, ck);
    }
    if(nn > mm + kk)
        return "IMPOSSIBLE";
    string result = "";
    result.reserve(n);
    while(nn)
    {
        result += cn;
        result += cm;
        nn -= 1;
        mm -= 1;
        if(nn < mm + kk)
        {
            result += ck;
            kk -= 1;
        }
        if(kk > mm)
        {
            swap(mm, kk);
            swap(cm, ck);
        }
    }
    if(rg.length()) result.replace(result.find('R'), 1, rg);
    if(yv.length()) result.replace(result.find('Y'), 1, yv);
    if(bo.length()) result.replace(result.find('B'), 1, bo);
    return result;
}

int main()
{
	int t; cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		cout << solve() << endl;
	}
	return 0;
}
