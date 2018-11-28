#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct myLen {
    int llen, rlen;
};
myLen minorLen(const myLen Len1, const myLen Len2) {
    if (Len1.llen<Len2.llen)
        return Len1;
    else if (Len1.llen==Len2.llen) {
        if (Len1.rlen<Len2.rlen)
            return Len1;
        else
            return Len2;
    }
        return Len2;
}

myLen calLen(const int n, const int k) {
    if (k == 0) {
        myLen LenReturn;
        LenReturn.llen = n;
        LenReturn.rlen = n;
        return LenReturn;
    }
    else if (k == 1) {
        myLen LenReturn;
        LenReturn.llen = n/2;
        LenReturn.rlen = (n-1)/2;
        return LenReturn;
    }
    else
        return minorLen(calLen(n/2,k/2), calLen((n-1)/2,(k-1)/2));
}

int main()
{
    int T;
    cin >> T;
    int N, K;
    myLen LenOutput;

    for (int Tidx=0; Tidx<T; Tidx++) {
       cin >> N >> K;
       LenOutput = calLen(N,K);
       cout << "Case #" << Tidx+1 << ": ";
       cout << LenOutput.llen << ' ' << LenOutput.rlen;
       cout << endl;
    }

    return 0;
}
