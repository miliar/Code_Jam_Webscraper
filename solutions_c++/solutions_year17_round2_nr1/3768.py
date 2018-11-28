#include <iostream>
#include <iomanip>

int T=0;

using namespace std;

int main() {
    cin >> T;

    for (int i=0; i<T; ++i) {
        long D=0;
        int  N=0;
        double maxt = 0;

        cin >> D;
        cin >> N;

        // cerr << "Case #" << (1+i) << ": N=" << N << " D=" << D << endl;

        for (int j=0; j<N; ++j) {
            long k=0;
            long s=0;
            cin >> k;
            cin >> s;

            double t = ((double) (D-k))/((double)s);
            if (maxt < t)
                maxt = t;
            
            // cerr << "Case #" << (1+i) << ": k=" << k << " s=" << s << " t=" << t << endl;
        }

        double maxv = D/maxt;
        // cerr << "Case #" << (1+i) << ": maxt=" << maxt << " maxv=" << maxv << endl;
        cout << "Case #" << (1+i) << ": " << fixed << maxv << endl;
    }

    return 0;
}
