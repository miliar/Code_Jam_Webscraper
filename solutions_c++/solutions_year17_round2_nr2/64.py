#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<complex>
#include<ctime>
#include<functional>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vi::iterator vit;
typedef set<ll> si;
typedef si::iterator sit;
typedef vector<pii> vpi;
typedef pair<int, char> pci;
typedef vector<pci> vpci;

#define sq(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
//#define LL "%I64d"
#define LL "%lld"
#define RLL(x) scanf(LL,&(x))

int colors[6];
vector<string> rgb[3];
string res;
int n;
char prior;

string templ = "ROYGBV";

bool prepare()
{
    for(int i = 0; i < 6; i += 2)
    {
        if(colors[i] < colors[(i+3) % 6])
            return false;
        if(colors[i] == 0)
            continue;
        if(colors[i] == colors[(i+3) % 6])
        {
            if(colors[i] * 2 == n)
            {
                string tmp;
                for(int j = 0; j < colors[i]; ++j)
                {
                    tmp.push_back(templ[i]);
                    tmp.push_back(templ[(i + 3) % 6]);
                }
                rgb[i / 2].push_back(tmp);
                return true;
            }
            else
            {
                return false;
            }
        }
        string tmp;
        for(int j = 0; j < colors[(i + 3) % 6]; ++j)
        {
            tmp.push_back(templ[i]);
            tmp.push_back(templ[(i + 3) % 6]);
        }
        tmp.push_back(templ[i]);
        rgb[i / 2].push_back(tmp);
        tmp.clear();
        tmp.push_back(templ[i]);
        for(int j = colors[(i + 3) % 6] + 1; j < colors[i]; ++j)
            rgb[i / 2].push_back(tmp);
    }
    return true;
}

void test(int T)
{
    scanf("%d", &n);
    for(int i = 0; i < 6; ++i)
    {
        scanf("%d", colors + i);
    }
    res.clear();
    for(int i = 0; i < 3; ++i)
        rgb[i].clear();
    if(!prepare())
        res = "IMPOSSIBLE";
    else
    {
        char last = 'Z';
        prior = 'Z';
        while(true)
        {
            int maxv = 0;
            int pos = -1;
            bool have = false;
            for(int i = 0; i < 3; ++i)
            {
                if(!rgb[i].empty())
                {
                    have = true;
                    if(rgb[i][0][0] != last && (maxv < rgb[i].size() ||
                                                (maxv == rgb[i].size() && rgb[i][0][0] == prior)))
                    {
                        maxv = rgb[i].size();
                        pos = i;
                    }
                }
            }
            if(pos > -1)
            {
                res += rgb[pos].back();
                if(last == 'Z')
                    prior = rgb[pos].back()[0];
                last = rgb[pos].back()[0];
                rgb[pos].pop_back();
            }
            else
            {
                if(have)
                    res = "IMPOSSIBLE";
                break;
            }
        }
    }
    if(res[0] == res.back())
        res = "IMPOSSIBLE";
    printf("Case #%d: %s\n", T, res.c_str());
    
}

int main()
{
    freopen("/Users/olpet/Downloads/GCJ/b.in", "r", stdin);
    freopen("/Users/olpet/Downloads/GCJ/b.out", "w", stdout);
    int n;
    cin>>n;
    for(int i = 0; i < n; ++i)
        test(i+1);
    return 0;
}
