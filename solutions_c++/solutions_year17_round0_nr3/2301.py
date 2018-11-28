#include <iostream>
#include <string>
#include <fstream>
#include <map>

using namespace std;

int test;
long long n , k;
map <long long , long long> mymap;

int main () {
    freopen("input.txt" , "r" , stdin);
    freopen("output.txt" , "w" , stdout);
    cin >> test;

    for (int t = 1; t <= test; t++) {
        cout << "Case #" << t << ": ";
        cin >> n >> k;
        mymap.clear();

        mymap[n] = 1;

        k--;

        while (k) {
            map <long long , long long> :: iterator it = mymap.end();
            it--;
            long long T = it->first;
            long long val = it->second;

            if (k < val) break;
            k -= val;
            T--;

            mymap[T / 2] += val;
            mymap[T - T / 2] += val;

            mymap.erase(it);
        }

        map <long long , long long> :: iterator it = mymap.end();
        it--;

        long long T = it->first;

        T--;

        cout << T - T / 2 << ' ' << T / 2 << endl;

        cout << endl;
    }
    return 0;
}
