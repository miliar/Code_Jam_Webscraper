#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int x = 1; x <= T; x++){
        int D, N;

        cin >> D;
        cin >> N;

        int K[N];
        int S[N];

        for(int y = 0; y < N; y++){
            cin >> K[y];
            cin >> S[y];
        }

        double slowest = 0;
        for(int i = 0; i < N; i++){
            double total;
            total = D - K[i];
            total /= S[i];

            if(total > slowest){
                slowest = total;
            }
        }

        cout << "Case #" << x << ": " << D/slowest;
        if(x != T)
            cout << endl;

    }
}
