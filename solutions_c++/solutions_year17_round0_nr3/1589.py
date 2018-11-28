#include <iostream>
#include <fstream>
using namespace std;

typedef long long ll;

int main()
{
    ifstream cin("C.in");
    ofstream cout("C.out");
    int T;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        ll N, K;
        cin >> N >> K;
        ll A = N; ll Ac = 1;
        ll B = 0; ll Bc = 0;
        while(Ac + Bc < K)
        {
            //cerr << Ac << " gaps of size " << A << ", " << Bc << " of size " << B << endl;
            //cerr << K << " cuts left" << endl;
            A--; B--;
            ll a2 = A/2;
            ll b2 = A/2 + 1;
            ll ac2 = 0; ll bc2 = 0;
            if (A%2 == 0)
            {
                ac2 += 2*Ac;
            }
            else
            {
                ac2 += Ac;
                bc2 += Ac;
            }
            if (B%2 == 0)
            {
                bc2 += 2*Bc;
            }
            else
            {
                ac2 += Bc;
                bc2 += Bc;
            }
            K -= (Ac+Bc);
            if (K == 0)
            {
                cout << "Case #" << t+1 << ": " << A/2 + A%2 << " " << A/2 << endl;
            }
            A = a2;
            B = b2;
            Ac = ac2;
            Bc = bc2;
        }
        //cerr << Ac << " gaps of size " << A << ", " << Bc << " of size " << B << endl;
            //cerr << K << " cuts left" << endl;
        if (K == 0)
            continue;
        else if (K <= Bc)
        {
            B--;
            cout << "Case #" << t+1 << ": " << B/2 + B%2 << " " << B/2 << endl;
        }
        else
        {
            A--;
            cout << "Case #" << t+1 << ": " << A/2 + A%2 << " " << A/2 << endl;
        }
    }
}
