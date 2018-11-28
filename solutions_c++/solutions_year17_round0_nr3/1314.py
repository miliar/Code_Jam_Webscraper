#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

const string path = "/Users/mac/Documents/cpp/Code Jam/";

const string IMPOSSIBLE = "IMPOSSIBLE";

vector<long long> a;
vector<long long> t;

void add(long long number, long long amount) {
//    cout << "add: " << number << " x " << amount << endl;
    a.push_back(number);
    t.push_back(amount);
}

void sortThem() {
    for (int i = 0; i < a.size(); i ++)
        for (int j = i + 1; j < a.size(); j ++)
            if (a[i] == a[j]) {
                t[i] += t[j];
                a[j] = 0;
            }
    
    for (int i = 0; i < a.size(); i ++)
        for (int j = i + 1; j  < a.size(); j ++)
            if (a[i] < a[j]) {
                swap(a[i], a[j]);
                swap(t[i], t[j]);
            }
}

int main() {
    freopen("/Users/mac/Documents/cpp/Code Jam/in", "r", stdin);
    freopen("/Users/mac/Documents/cpp/Code Jam/out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int CT = 1;  CT <= T; CT ++) {
        long long n, k;
        scanf("%lld%lld", &n, &k);
        printf("Case #%d: ", CT);
        
        a.clear();
        t.clear();
        
        a.push_back(n);
        t.push_back(1);
        
        long long r = 999;
        while (k > 0) {
            sortThem();
            long long s = a[0];
            long long c = t[0];
            
            a[0] = 0;
            t[0] = 0;
            
//            cout << s << " " << c << endl;
            
            r = s;
            k -= c;
            
            if (s % 2 == 1) {
                add((s - 1) / 2, 2 * c);
            } else {
                long long half = (s - 1) / 2;
                long long rem = s - 1 - half;
                
                add(half, c);
                add(rem, c);
            }
        }
        
        r --;
        printf("%lld %lld\n", (r + 1) / 2, r - (r + 1) / 2);
    }
    
    
    return 0;
}
