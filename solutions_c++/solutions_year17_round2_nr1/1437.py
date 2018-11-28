#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <map>
#include <sstream>
#include <stack>
#include <cctype>
#include <bitset>
#include <queue>
using namespace std;

#define INF (1LL << 60)

typedef pair<int,int> pii;

using namespace std;

double pi = acos(-1);

int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("out.txt","w",stdout);

    ios::sync_with_stdio(false); cin.tie(0);
    int64_t T, cnt = 0;
    cin >> T;
    while(T--){
        cnt++;
        int64_t D, N;
        cin >> D >> N;
        double endtime = 0;
        for(int i = 0; i < N; i++){
            int64_t K, S;
            cin >> K >> S;
            endtime = max( endtime,((double)(D-K)/(double)S));
        }
        cout << "Case #" << cnt << ": " <<  setprecision(10) << (double)(D) / (double)endtime << endl;
    }

    return 0;
}
