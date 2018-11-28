#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;


int main()
{
    int T;
    cin >> T;
    for (int t=1; t<=T; t++)
    {
        unsigned long D; int N;
        cin >> D >> N;
        vector<unsigned long> K(N), S(N);
        for (int i=0; i<N; i++) cin >> K[i] >> S[i];
        int ndx=0;
        for (int i=1; i<N; i++)
        {
            if (S[i]*(D-K[ndx]) < S[ndx]*(D-K[i])) ndx = i;
        }
        unsigned long A, B, C, C1, C2;
        A = D*S[ndx]*1000000L;
        B = D - K[ndx];
        C = A/B;
        C1 = C/1000000L; C2 = C%1000000L;
        char ss[8];
        sprintf(ss, "%06d", int(C2));
        cout << "Case #" << t << ": " << C1 << "." << ss << endl;
    }
    return 0;
}
