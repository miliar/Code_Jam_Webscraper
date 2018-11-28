#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <iomanip>

#define LL long long
#define LD long double

using namespace std;

const int MAXN = 1001000;

int T;
int D, N;
int K, S;
double max_time;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large_out.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin >> T;
    for(int i=1; i<=T; i++){
        cin >> D >> N;
        max_time = 0;
        for(int j=1; j<=N; j++){
            cin >> K >> S;
            max_time = max(max_time, double( max(0, D-K) ) / double(S) );
        }
        cout << "Case #" << i << ": " << fixed << setprecision(7) << double(D) / max_time << endl;
    }

    return 0;
}
