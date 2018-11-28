//In the name of God
//-----gmmj

#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <ctime>
#include<iomanip>
#include<ctime>

#define Time printf("\nTime : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC);
#define For(J,R,K) for(int J=R;J<K;++J)
#define Rep(I,N) For(I,0,N)
#define MP make_pair
#define ALL(X) (X).begin(),(X).end()
#define SF scanf
#define PF printf
#define pii pair<long long,long long>
#define pdd pair<double , double>
#define Sort(v) sort(ALL(v))
#define Test freopen("a.in","r",stdin);
#define Testout freopen("a.out","w",stdout);
#define pb push_back
#define Set(a,n) memset(a,n,sizeof(a))
#define MAXN 100000+9
#define EPS 1e-15
#define inf 1ll<<62

typedef long long ll;

using namespace std;

bool isOk(string st)
{
    For(i , 1 , (int)st.size())
        if(st[i] < st[i - 1])
            return false;
    return true;
}

string makeGood(string st)
{
    string ans = "";

    for(int i = (int)st.size() - 1 ; i > 0 ; --i)
    {
        if(st[i-1] != 0 && st[i] < st[i-1]){
            For(j , i , (int)st.size() )
                st[j] = '9';
            st[i-1]--;
            break;
        }
    }

    return st;
}

int main()
{
 //   Test;
 //   Testout;

    int tc , cas = 1;
    cin >> tc;
    while(tc--)
    {
        string st;
        cin >> st;


        while(isOk(st) == false)
        {
            st = makeGood(st);
            int ind = 0;
            while(st[ind] == '0')
                ind++;
            string nst = "";
            For(i , ind , (int)st.size())
            {
                nst += st[i];
            }
            st = nst;
        }

        cout << "Case #" << cas++ <<": " << st << endl;


    }
	return 0;
}
