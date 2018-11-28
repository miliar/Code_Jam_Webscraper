#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

bool isTidy(int n)
{
    int nw;
    int old = 9;
    while(n>0)
    {
        nw=n%10;
        n/=10;
        if(nw>old)return false;
        old = nw;
    }
    return true;
}

int main() {
    ifstream in;
    in.open("B-small-attempt0.in");
    ofstream out;
    out.open("out.txt");
    int T,n;
    in>>T;
    for(int t=1; t<=T; t++)
    {
        in>>n;
        while(n>0)
        {
            if(isTidy(n))break;
            n--;
        }
        out<<"Case #"<<t<<": "<<n<<endl;
    }
    in.close();
    out.close();
    return 0;
}
