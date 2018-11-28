#include <iostream>
#include <algorithm>
using namespace std;

int HD, AD, HK, AK, B, D;


int M[101][101];




int sim(int buffrem, int debuffrem, bool twist) {
    int hd=HD, hk=HK;
    int ad=AD, ak=AK;
    for (int moves=1; moves<=200; moves++) {
        if ((!debuffrem && hd <= ak || debuffrem && hd <= max(0, ak-D)) && hk > ad) {
            hd=HD;// cure
        }
        else if (twist && debuffrem) {
            ak -= D;
            if (ak<0) ak=0;
            debuffrem--;
        }
        else if (buffrem) {
            ad += B;
            buffrem--;
        }
        else if (!twist && debuffrem) {
            ak -= D;
            if (ak<0) ak=0;
            debuffrem--;
        }
        else {
            hk -= ad;
        }
        if (hk <= 0) return moves;
        
        hd -= ak;
    }
    return 999;
}


int main() {
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        cin>>HD>>AD>>HK>>AK>>B>>D;
        int res = 999;
        for (int i=0; i<=100; i++) {
            for (int j=0; j<=100; j++) {
                res = min(res, sim(i, j, true));
                res = min(res, sim(i, j, false));
            }
        }
        cout<<"Case #"<<t<<": ";
        if (res != 999)
            cout<<res<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}