#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int cc=0; cc<T; cc++) {
            int D, N;
            cin >> D >> N;
            vector<int> k,s;
            for(int i=0; i<N; i++) {
                    int ki,si;
                    cin >> ki >> si;
                    k.push_back(ki);
                    s.push_back(si);
            }
            double maxT = 0.0;
            for(int i=0; i<N; i++) {
                if((double)(D-k[i])/s[i]>maxT)
                    maxT = (double)(D-k[i])/s[i];
            }
            printf("Case #%d: %.6lf\n",cc+1, (double)D/maxT);
            //cout << "Case #"<< cc+1 << ": "<<(double)D/maxT << endl;
    }
    return 0;
}
