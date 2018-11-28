#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int istidy(int n) {
    if(n < 10) return 1;
    if(((n % 100) / 10) <= (n % 10))
        return istidy(n / 10);
    else
        return -1;
}

int findmaxtidy(int n) {
    if(istidy(n) > 0)
        return n;
    else
        return findmaxtidy(n-1);
}

int main() {
    int t;
    int n;
    int answer;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        //algorithm here
        cout << "Case #" << i << ": " << findmaxtidy(n) << endl;

    }
    return 0;
}

