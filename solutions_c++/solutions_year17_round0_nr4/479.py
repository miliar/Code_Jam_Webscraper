//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
#pragma comment(linker,"/STACK:33554432") /*32Mb*/

#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <cmath>
#include <list>
#include <iomanip>
#include <set>
#include <map>
#include <sstream>
#include <fstream>
#include <sstream>
#include <iterator>
#include <unordered_map>
using namespace std;


typedef  long long LL;
typedef  unsigned long long ULL;
typedef  long double LD;
typedef  pair<long long, long long> PII;
typedef vector<int> VI;

#define FOR(i,a,b) for(int (i)=(a);i<(b);++(i))
#define RFOR(i,a,b) for(int (i)=(a)-1;(i)>=(b);--(i))
#define MP make_pair
#define SZ(a) (int)a.size()
#define MOD 1000000007
#define mod 1000000000
#define INF 1000000000
#define PB push_back
#define y0 kihrbdb
#define y1 ugvrrtgtrg
#define x first
#define y second


const int MAXV = 100*100;

map<LL,LL> F;
int t;
LL n, k;
char s[777][777];
vector< pair<char, PII> > ans;

int main()
{
    freopen("/Users/Taras/Downloads/D-small-attempt2.in.txt","r",stdin);
    freopen("/Users/Taras/Downloads/out.txt","w",stdout);
    cin >> t;
    FOR (tst,0,t)
    {
        cin >> n >> k;
        //cerr<<n<<" "<<k<<endl;
        ans.clear();
        FOR (i,0,n)
        FOR (j,0,n) s[i][j] = '.';
        FOR (i,0,k)
        {
            int a, b;
            char ch;
            cin >> ch >> a >> b;
            a--; b--;
            //cerr << "*\n";
            //swap(a,b);
            s[a][b] = ch;
        }
        //if (tst != 17) continue;
        //FOR (i,0,n) reverse(s[i],s[i]+n);
        int score = 0;
        FOR (i,0,n)
        FOR (j,0,n)
        {
            //if (i == 0 || i == n-1)
            {
                int m = 3;
                FOR (k,0,n)
                    if (k != j && s[i][k] != '.' && s[i][k] != '+') m &= 1;
                FOR (k,0,n)
                    if (k != i && s[k][j] != '.' && s[k][j] != '+') m &= 1;
                FOR (x,0,n)
                {
                    int y = i+j-x;
                    if (x != i && y >= 0 && y < n)
                        if (s[x][y] != '.' && s[x][y] != 'x') m &= 2;
                }
                FOR (x,0,n)
                {
                    int y = j-i+x;
                    if (x != i && y >= 0 && y < n)
                        if (s[x][y] != '.' && s[x][y] != 'x') m &= 2;
                }
                char ch = s[i][j];
                if (m&1 && (i == 0 || i == n-1)) s[i][j] = '+';
                if (m&2) s[i][j] = 'x';
                if (m == 3 && (i == 0 || i == n-1)) s[i][j] = 'o';
                if (ch != s[i][j])
                    ans.PB(MP(s[i][j],MP(i,j)));
            }
            if (s[i][j] == '+' || s[i][j] == 'x') score++;
            if (s[i][j] == 'o') score+=2;
        }
        /*FOR (i,0,n)
        {
            FOR (j,0,n) cout << s[i][j]<<" ";
            cout << endl;
        }*/
        cout << "Case #"<<tst+1<<": "<< score<<" "<<ans.size()<<endl;
        FOR (i,0,ans.size())cout << ans[i].first<<" "<<ans[i].second.first+1<<" "<<ans[i].second.second+1<<"\n";
    }
    
}


//cout << s.ind<<endl;
//for(set< Segm > :: iterator it = E.begin(); it != E.end(); it++)
//       cout << it->ind<<" ";
//cout << "end"<<endl;
//cout << E.size() <<" "<<s.ind<<" * "<<it->ind<<endl;