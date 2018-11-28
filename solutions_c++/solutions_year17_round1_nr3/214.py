#include <iostream>
using namespace std;

const int INF=2000000000;
int HD,AD,HK,AK,B,D;

int doit2(int AK, int b, int H) {
    int A = AD + b*B;
    int ret=0;
    int K = HK;
    for(;;) {
        //cout << "?doit2 b=" << b << " A=" << A << " " << " H=" << H << " AK=" << AK << " b=" << b << " HD=" << HD << " K=" << K << " " << ret+1 << endl;
        if(A >= K) {
            //cout << "doit2 b=" << b << " A=" << A << " " << " H=" << H << " AK=" << AK << " b=" << b << " HD=" << HD << " K=" << K << " " << ret+1 << endl;
            return ret+1;
        }
        if(AK >= H) {
            ret++;
            H=HD-AK;
            if(AK >= H)
                return INF;
        } else {
            H-=AK;
            K-=A;
            ret++;
        }
    }
    return INF;
}

int doit(int d, int H) {
    int A = max(0, AK-d*D);
    int ret=doit2(A, 0, H);
    int cur=0;
    if(B) {
        for(int b=1; ; b++) {
            if(A >= H) {
                cur++;
                H = HD-A;
                if(A >= H)
                    break;
            }
            H -= A;
            cur++;
            ret = min(ret, cur + doit2(A, b, H));
            if(AD+b*B >=HK) break;
        }
    }
    //cout << "doit " << d << " " << H << " " << ret << endl;
    return ret;
}

int main(void) {
    int T; cin >> T;
    for(int ts=1; ts<=T; ts++) {
        cin >> HD >> AD >> HK >> AK >> B >> D;
        cout << "Case #" << ts << ": ";
        //cout << endl;
        int H=HD;
        int turns=0;
        int ret = doit(0, H);
        if(AD >= HK) {
            cout << "1" << endl;
            continue;
        }
        if(D) {
            for(int d=1; d<=(AK+D-1)/D; d++) {
                if(AK-d*D >= H) {
                    turns++;
                    H=HD-max(0, AK-(d-1)*D);
                    if(AK-d*D >= H) {
                        break;
                    }
                }
                H -= max(0, AK-d*D);
                turns++;
                ret = min(ret, turns + doit(d, H));
                //cout << turns << " turns to debuff " << d << endl;
            }
        }
        if(ret==INF) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ret << endl;
        }
    }
}
