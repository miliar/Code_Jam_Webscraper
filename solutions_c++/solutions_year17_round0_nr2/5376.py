#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

int getDigitAt(int pos, ull n) {
    ull base = pow(10,pos);
    return (n/base)%10;
}

ull solve(ull n) {
    int dnum = floor(log10(n))+1;
    int predig = getDigitAt(dnum-1, n);
    for(int i=dnum-2; i>=0; i--){
        int nowdig = getDigitAt(i, n);
        if(nowdig<predig) {
            ull prebase = pow(10,i);
            n/=prebase;
            n*=prebase;
            n--;
            return solve(n);
        }
        predig = nowdig;
    }
    return n;
}

int main(int argc, char *argv[])
{
    int Q;
    ifstream infile;
    ofstream outfile;
    infile.open("input.txt");
    outfile.open("output.txt");
    infile>>Q;
    for(int i=1;i<=Q;i++) {
        ull n;
        infile>>n;
        ull ans = solve(n);
        outfile<<"Case #"<<i<<": "<<ans<<endl;
    }

    return 0;
}
