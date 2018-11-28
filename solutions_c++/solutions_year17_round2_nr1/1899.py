#include<iostream>

using namespace std;

int main(void)
{
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        int D,N;
        cin >> D;
        cin >> N;
        int res = 0;
        double max_time = 0.0;
        for (int j=0; j<N; j++) {
            int K,S;
            cin >> K;
            cin >> S;
            max_time = max((double)1.0*(D-K)/S, max_time);
        }
        double s = D/max_time;
        //cout << "Case #" << i+1 << ": " << s << endl;
        printf("Case #%d: %f\n", i+1, s);
    }
    return 0;
}
