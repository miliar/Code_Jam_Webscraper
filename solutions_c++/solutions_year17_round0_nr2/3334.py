#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=int(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=int(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=int(n)-1;i>=(int)(s);i--)

#define all(c) (c).begin(),(c).end()

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

const string IMPOSSIBLE = "X";

string calc(char minDigit, string number)
{
    if (number.empty()) return "";
    else if (number[0] < minDigit) return IMPOSSIBLE;
    else
    {
        string rest = calc(number[0], number.substr(1));
        if (rest != IMPOSSIBLE)
            return number[0] + rest;
        else if (number[0]-1 < minDigit)
            return IMPOSSIBLE;
        else
            return char(number[0]-1) + string(number.size()-1, '9');
    }
    
}

// LOS LEADING ZEROS!!!!!

string stripLeadingZeros(string s)
{
    int i = 0;
    while (i < int(s.size()) && s[i] == '0') i++;
    return s.substr(i);
}

int main()
{
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        tint N; cin >> N;
        string res = stripLeadingZeros(calc('0', to_string(N)));
		cout << "Case #" << caso + 1 << ": " << res << endl;
		cerr << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}
