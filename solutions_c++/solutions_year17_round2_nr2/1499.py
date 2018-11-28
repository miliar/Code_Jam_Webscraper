#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

#define REP(i,a,b) for(int i=int(a);i<int(b);i++)

using namespace std;

typedef long long int lli;

int main () {
    int T;
    cin >> T;
    REP (_, 0, T) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        pair<int, char> pic[3];
        pic[0].first = R;
        pic[0].second = 'R';
        pic[1].first = Y;
        pic[1].second = 'Y';
        pic[2].first = B;
        pic[2].second = 'B';
        sort(pic, pic + 3);

        cout << "Case #" << _ + 1 << ": " ;
        if (pic[2].first == N) {
            cout << "IMPOSSIBLE" << endl;
        } else if (pic[0].first == 0) {
            if (pic[1].first == pic[2].first) {
                int temp = 0;
                REP (i, 0, N) {
                    cout << pic[temp + 1].second;
                    temp = 1 - temp;
                }
                cout << endl;
            } else {
                cout << "IMPOSSIBLE" << endl;
            }
        } else {
            if (pic[0].first + pic[1].first < pic[2].first) {
                cout << "IMPOSSIBLE" << endl;
            } else {
                int cnt = 0;
                while (pic[1].first != pic[0].first) {
                    cout << pic[2].second << pic[1].second;
                    pic[2].first--;
                    pic[1].first--;
                    cnt += 2;
                }
                int temp = 0;
                while (cnt < N) {
                    if (pic[2].first) {
                        cout << pic[2].second;
                        pic[2].first--;
                        cnt++;
                    }
                    cout << pic[temp].second;
                    cnt++;
                    temp = 1 - temp;
                }
                cout << endl;
            }
        }

    }
    return 0;
}
