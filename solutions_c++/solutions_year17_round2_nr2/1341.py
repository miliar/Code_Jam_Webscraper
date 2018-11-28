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


using namespace std;



int main()
{
    freopen("B-small-attempt4.in","r",stdin);
//    freopen("in.txt","r",stdin);
    freopen("out3.txt","w",stdout);

    ios::sync_with_stdio(false); cin.tie(0);
    int T, cnt = 0;
    cin >> T;
    while(T--){
        cnt++;
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        string s;
        s.resize(N, '.');
        vector<int> p = {R,Y,B};
        vector<char> l = {'R','Y','B'};
        char lastc = '.';
        bool suc = true;
        for(int i = 0; i < N; i++){
            int bestn = 0, besti = -1;
            char bestc;
            for(int j = 0; j < 3; j++){
                if(bestn < p[j] && l[j] != lastc){
                    bestn = p[j];
                    bestc = l[j];
                    besti = j;
                }
            }
            if(besti == -1){suc = false; break;}
            p[besti]--;
            s[i] = bestc;
            lastc = s[i];
            //cout << s << endl;
        }
        if(s[0] == s[N-1]) {
            char temp = s[N-1];
            s[N-1] = s[max(0,N-2)];
            s[max(0,N-2)] = temp;
        }

        for(int i = 0; i < N; i++){
            if(s[(i-1+N) % N] == s[i] || s[i] == s[(i+1+N)%N]) suc = false;
        }
        cout << "Case #" << cnt << ": ";
        suc ? cout << s << endl : cout << "IMPOSSIBLE" << endl;

    }
    return 0;
}
