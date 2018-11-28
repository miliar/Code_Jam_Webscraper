#include <iostream>
#include <cstdint>
#include <vector>

using namespace std;

//O(log n)

int main() {
    int T;

    ios_base::sync_with_stdio(false);
    cin>>T;

    for (int testCase=1; testCase<=T; ++testCase) {
        uint64_t n, k; cin>>n; cin>>k;

        uint64_t nDone=0;
        uint64_t avPair=(n%2==0)?1:0;
        uint64_t avNoPair=(n%2==1)?1:0;

        while (nDone+avPair+avNoPair<k) {
            uint64_t tmpPair, tmpNoPair;

            if (n%4<=1)      tmpPair=avPair+2*avNoPair, tmpNoPair=avPair;
            else if (n%4>=2) tmpPair=avPair, tmpNoPair=avPair+2*avNoPair;

            nDone+=avPair+avNoPair;
            avPair=tmpPair;
            avNoPair=tmpNoPair;

            n=(n-1)/2;
        }

        //cout<<"1n="<<n<<" avpair="<<avPair<<" avNoPair="<<avNoPair<<" done="<<nDone<<endl;

        if (nDone!=0 && n%2==1 && nDone+avPair>=k) n+=1;
        else if (nDone!=0 && n%2==0 && nDone+avNoPair>=k) n+=1;

        //we are setting last person to block of size n

        uint64_t max, min;
        if (n%2==1) max=min=n/2;
        else if (n%2==0) max=n/2, min=max-1;

        cout<<"Case #"<<testCase<<": "<<max<<" "<<min<<endl;
    }

    return 0;
}
