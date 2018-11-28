#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <iomanip>
#include <queue>
#include <iterator>
#include <fstream>
#include <cmath>
using namespace std;

bool okay(long long n) {
    long long int last = 9;
    while(n) {
        if(n%10 > last) {
            return false;
        }
        last = n%10;
        n /= 10;
    }
    return true;
}


int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
#define cin in
#define cout out


    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++) {
        cout<<"Case #"<<cas<<": ";

        long long n;
        cin>>n;
        long long pow10 = 1;
        while(!okay((n/pow10-(pow10>1LL?1LL:0LL))*pow10+pow10-1LL)){
            pow10 *= 10LL;
        }
        cout<<(n/pow10-(pow10>1LL?1LL:0LL))*pow10+pow10-1LL<<endl;
    }

}
