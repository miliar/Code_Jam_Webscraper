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
	    int D,N,k,s;
        cin>>D>>N;
        double mt = 0.0;
        for ( int i=0;i<N;i++) {
            cin>>k>>s;
            mt = max( (D-k)/(s+.0), mt );
        }
        printf("Case #%d: %.8f\n", ++cas, D/mt);
	}
	return 0;
}
