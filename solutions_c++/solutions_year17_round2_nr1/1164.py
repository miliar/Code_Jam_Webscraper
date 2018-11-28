#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int cs=1; cs<=T; cs++) {
        int D,N;

        cin >> D >> N;

        double t=0.;
        for(int i=0;i<N;i++) {
            int k,s;
            cin >> k >> s;
            t = max(t, (D-k)*1./s);
        }

        printf("Case #%d: %.6f\n", cs, D/t);
    }

    return 0;
}
