#include <iostream>
#include <fstream>

using namespace std;

typedef long long ll;

ll maxs(ll a) {
    if(a < 0) {
        return 0;
    }
    return a;
}

int main()
{
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    int T;
    fin >> T;
    for(int coun = 0; coun < T; coun++) {
        ll N, K;
        fin >> N >> K;
        ll MA, MI;
        MA = (N-1)/2;
        MI = (N-1)/2;
        if(N%2 == 0) {
            MA++;
        }

        ll smalls = 0;
        ll small;
        ll larges = 0;
        ll large;
        if(N%2 == 0) {
            large = MA;
            small = MI;
            larges = 1;
            smalls = 1;
        } else {
            large = MA;
            small = MA;
            larges = 2;
            smalls = 0;
        }

        ll c = 1;
        ll counter = 1;
        //cout << small << " " << large << '\n';

        while(counter < K) {
            c <<= 1;
            counter += c;
            ll newsmalls = 0;
            ll newlarges = 0;
            if(small % 2 == 0) {
                newsmalls += smalls;
                newlarges += smalls;
            } else {
                newsmalls += 2*smalls;
            }
            if(large %2 == 0) {
                newlarges += larges;
                newsmalls += larges;
            } else {
                newlarges += 2*larges;
            }
            small = (small-1)/2;
            large = large/2;

            smalls = newsmalls;
            larges = newlarges;

            //cout << c <<  " " <<  smalls << " " << larges << '\n';
            //cout << small << " " << large << '\n';
        }

        if(K<= counter-c+larges && larges > c && K <= counter-c+(larges%c)) {
            fout << "Case #" << coun+1 << ": " << large << " " << large << '\n';
        } else if (K<= counter-c+larges) {
            fout << "Case #" << coun+1 << ": " << large << " " << small << '\n';
        } else {
            fout << "Case #" << coun+1 << ": " << small << " " << small << '\n';
        }

     }
}
