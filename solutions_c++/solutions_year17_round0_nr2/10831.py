#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

bool isTidy(int n) {
    int i = 0;
    int pr;
    while(n > 0) {
        if(i != 0) {
            if(pr < n % 10) {
                return false;
            }
        }
        pr = n % 10;
        n /= 10;
        i++;
    }
    return true;
}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int last[1005];
    int lt;
    for(int i = 1; i <= 1000; i++) {
        if(isTidy(i)) {
            lt = i;
        }
        last[i] = lt;
    }

    ifstream fd("a.txt");
    ofstream fr("b.txt");
    int t;
    fd >> t;
    for(int i = 1; i <= t; i++) {
        int n;
        fd >> n;
        fr << "Case #" << i << ": " << last[n] << endl;
    }
    fd.close();
    fr.close();

    return 0;
}
