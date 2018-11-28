#include<iostream>
#include<vector>

using namespace std;

int main(void)
{
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        if (R*2 > N || Y*2 > N || B*2 > N) {
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
            continue;
        }
        vector<pair<int, char> > vp;
        if (R > 0) vp.push_back(make_pair(R, 'R'));
        if (Y > 0) vp.push_back(make_pair(Y, 'Y'));
        if (B > 0) vp.push_back(make_pair(B, 'B'));
        sort(vp.begin(), vp.end());
        reverse(vp.begin(), vp.end());
        string res(N, '.');
        for (int i=0,j=0; i<N&&j<vp[0].first; i+=2,j++) {
            res[i] = vp[0].second;
        }
        if (vp.size() == 2)
            for (int i=1; i<N; i+=2)
                res[i] = vp[1].second;
        else {
            int idx = 0;
            for (int i=N-1, j=vp[1].first; i>0&&j>0; i-=2, j--) {
                if (res[i] != '.') i--;
                res[i] = vp[1].second;
            }
            for (int i=0; i<N; i++)
                if (res[i] == '.') res[i] = vp[2].second;
        }
        cout << "Case #" << i+1 << ": " << res << endl;
        for (int i=0; i<res.size(); i++) {
            if (res[i] == 'R') R--;
            if (res[i] == 'Y') Y--;
            if (res[i] == 'B') B--;
        }
        if (R != 0 || Y!= 0 || B != 0) {
            cerr << "ERROR:" << i << ':' << R << ' ' << Y << ' ' << B << endl;
            exit(1);
        }
    }
    return 0;
}
