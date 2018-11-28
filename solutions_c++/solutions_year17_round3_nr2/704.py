#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int Ctime[1441];
int Jtime[1441];
int memo[721][721][2][2];

int go(int Ct, int Jt, int who, const int& st)
{
    int cur = Ct+Jt;
    if(Jt == 720 && Ct == 720) return (st != who ? 1 : 0);
    if(Jt > 720 || Ct > 720) {
        return 987654321;
    }
    int &ret = memo[Ct][Jt][who][st];
    if (ret != -1) return ret;
    if(Ctime[cur] != -1) {
        return ret = (go(Ct, Jt+Ctime[cur], 1,st) + (who != 1 ? 1 : 0));
    } else if(Jtime[cur] != -1) {
        return ret = (go(Ct+Jtime[cur], Jt, 0,st) + (who != 0 ? 1 : 0));
    } else {
        return ret = (min(go(Ct+1, Jt, 0,st) + (who != 0 ? 1 : 0), go(Ct, Jt+1, 1,st) + (who != 1 ? 1 : 0)));
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    int Testcase;
    cin >> Testcase;
    for(int tc=1;tc<=Testcase;tc++) {
        cout << "Case #" << tc << ": ";
        int Ac, Aj;
        cin >> Ac >> Aj;
        for(int i=0;i<=1440;++i) {
            Jtime[i] = -1;
            Ctime[i] = -1;
        }
        for(int i=0;i<=720;++i){
            for(int j=0;j<=720;++j) {
                for(int k=0;k<2;++k) {
                    memo[i][j][k][0] = memo[i][j][k][1] = -1;
                }
            }
        }
        for(int i=0;i<Ac;++i) {
            int st, ed;
            cin >> st >> ed;
            Ctime[st] = ed-st;
        }
        for(int i=0;i<Aj;++i) {
            int st, ed;
            cin >> st >> ed;
            Jtime[st] = ed-st;
        }
        int ans = 987654321;
        if(Ctime[0] != -1) {
            ans = go(0, Ctime[0], 1, 1);
        } else if(Jtime[0] != -1) {
            ans = go(Jtime[0], 0, 0, 0);
        } else {
            ans = min(go(1,0,0,0), go(0,1,1,1));
        }
        cout << ans << '\n';
    }
    return 0;
}
