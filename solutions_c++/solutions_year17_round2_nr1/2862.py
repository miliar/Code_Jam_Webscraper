

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <cstring>
#include <math.h>
#include <fstream>
#include <iomanip>


using namespace std;

typedef long long int lli;
typedef double ld;

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ifstream in("ALarge.in");
    ofstream out;

    out.open("ALargeOut.txt");

    int t;
    in >> t;
    //cin >> t;
    for(int k=1;k<=t;k++)
    {

        lli n,d;
        in >> d >> n;

        ld max_time=0;

        while(n--)
        {
            ld a,b;
            in >> a >> b;
            ld time = (ld)((d-a)/b);

            if(time>max_time) max_time=time;
        }

        ld ans = (ld)(d/max_time);

        out << "Case #" << k << ": "  << std::fixed << std::setprecision(6) << ans << endl;

    }

    out.close();
    in.close();

    return 0;
}


