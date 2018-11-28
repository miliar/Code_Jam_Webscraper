#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <queue>
#include <map>

using namespace std;
int main()
{
    freopen( "in.txt", "r", stdin);
    freopen( "out.txt", "w", stdout);
	int T, cas = 0;
	cin>>T;
	while ( T -- )
	{
	    priority_queue<unsigned long long> da;
	    map< unsigned long long , unsigned long long > M;
	    unsigned long long mx, mn, n ,k;
	    cin >> n >> k;
        k--;
        M.clear();
        da.push( n );
        M[n] = 1;
        while (!da.empty()) {
            unsigned long long x = da.top();
            da.pop();
            unsigned long long c = M[x];
     //       cout <<x << " " << c << endl;
            if ( c <= k ) {
                k -= c;
                x --;
                if (x & 1) {
                    if (!M.count(x/2)) da.push(x/2);
                    M[x/2] += c;
                    if (!M.count(x/2+1)) da.push(x/2+1);
                    M[x/2+1] += c;
                }
                else {
                    if (!M.count(x/2)) da.push(x/2);
                    M[x/2] += c + c;
                }
            }
            else
            {
                x --;
                mx = (x + 1) / 2;
                mn = x/2;
                break;
            }
        }
        printf( "Case #%d: ", ++cas);
        cout << mx << " " << mn << endl;
	}
	return 0;
}
