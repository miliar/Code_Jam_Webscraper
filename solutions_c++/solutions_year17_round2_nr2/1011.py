#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>

using namespace std;

typedef unsigned long long ull;
typedef signed long long ll;

int main()
{
    int T;
    cin >> T;

    for(int t = 1; t <= T; t++)
    {
        int N;
        cin >> N;

        int R, O, Y, G, B, V;
        cin >> R >> O >> Y >> G >> B >> V; // only R, B, Y

        string imp = "IMPOSSIBLE";
        string res = "";
        
        if(R > 0) { res = res + 'R'; R--; }
        else if(B > 0) { res = res + 'B'; B--; }
        else { res = res + 'Y'; Y--; }

        while(--N > 0)
        {
            if(res[res.length() - 1] == 'R')
            {
                if(B == 0 && Y == 0) break;

                if(B >= Y)
                {
                    res = res + 'B';
                    B--;
                }
                else
                {
                    res = res + 'Y';
                    Y--;
                }
            }
            else if(res[res.length() - 1] == 'B')
            {
                if(R == 0 && Y == 0) break;

                if(R >= Y)
                {
                    res = res + 'R';
                    R--;
                }
                else
                {
                    res = res + 'Y';
                    Y--;
                }
            }
            else if(res[res.length() - 1] == 'Y')
            {
                if(B == 0 && R == 0) break;

                if(R >= B)
                {
                    res = res + 'R';
                    R--;
                }
                else
                {
                    res = res + 'B';
                    B--;
                }
            }

        }

        if(N > 0 || res[0] == res[res.length() - 1]) res = imp;

        cout << "Case #" << t << ": " << res << endl;
    }

    return 0;
}