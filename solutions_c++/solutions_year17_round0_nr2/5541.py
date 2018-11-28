//#include <bits/stdc++.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <bitset>
#include <utility>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long lol;
typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pf printf
#define sf scanf
#define pause system("pause")
#define pmin int,vector<int>,greater<int>
#define checkBit(n,p) (bool)(n&(1<<p))
#define setBit(n,p) (n|=(1<<p))
#define resetBit(n,p) (n&=~(1<<p))
#define toggleBit(n,p) (n^=1<<p)
#define mp make_pair
#define pb push_back
#define PI acos(-1.0)
#define sqr(x) (x*x)
#define gcd(x,y) __gcd((lol)abs(x),(lol)abs(y))
#define lcm(x,y) abs(x)/__gcd((lol)abs(x),(lol)abs(y))*abs(y)
#define logB(val,base) log(val)/log(base)

int dirK[8][2] = {{-2,1},{-1,2},{1,2},{2,1},{2,-1},{-1,-2},{1,-2},{-2,-1}};
int dir8[8][2] = {{-1,0},{0,1},{1,0},{0,-1},{-1,-1},{1,1},{1,-1},{-1,1}};
int dir4[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};
int month[] = {31,28,31,30,31,30,31,31,30,31,30,31};

/*============================================================================//
                                   send nudes
//============================================================================*/

vector<string> v;

bool check(string line)
{
    for(int i=1;i<line.length();i++)
    {
        if(line[i]<line[i-1])
        {
            return false;
        }
    }
    return true;
}

void print(string line)
{
    bool found = false;
    for(int i=0;i<line.length();i++)
    {
        if(line[i]=='0'&&found)
        {
            cout << line[i];
        }
        else if(line[i]!='0')
        {
            cout << line[i];
            found = true;
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    freopen("00_input.txt","r",stdin);freopen("00_output.txt","w",stdout);
    //pf("Hello World\n");
    int t,i,j,k;
    string line,nxt;
    //sf("%d",&t);
    //getchar();
    cin  >> t;
    for(i=0;i<t;i++)
    {
        v.clear();
        cin >> line;
        v.pb(line);
        for(j=0;j<line.length();j++)
        {
            if(line[j]=='0')
            {
                continue;
            }
            nxt = line;
            for(k=j+1;k<nxt.length();k++)
            {
                nxt[k] = '9';
            }
            while(nxt[j]!='0')
            {
                nxt[j]--;
                v.pb(nxt);
            }
        }
        sort(v.begin(),v.end());
        for(j=v.size()-1;j>=0;j--)
        {
            if(check(v[j]))
            {
                cout << "Case #" << i+1 << ": ";
                print(v[j]);
                cout << endl;
                break;
            }
        }
    }
}
