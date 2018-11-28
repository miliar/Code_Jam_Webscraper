#include <fstream>
#include <cstring>

using namespace std;

ifstream cin("date.in");
ofstream cout("date.out");

int v[101];

int main() {
    int t, nrt = 0;
    cin>>t;
    while (t){
        ++nrt;
        --t;
        cout<<"Case #"<<nrt<<": ";
        long long n;
        cin>>n;
        memset(v, 0, sizeof(v));
        int k = 0;
        while (n) {
            v[++k] = n % 10;
            n /= 10;
        }
        int w = -1;
        for (int i = 1; i <= k; ++i) {
            if (v[i] < v[i + 1]) {
                w = i;
                v[i + 1]--;
            }
        }
        if (v[k] == 0) {
            --k;
        }
        for (int i = k; i >= 1; --i) {
            if (i > w) {
                cout<<v[i];
            } else {
                cout<<"9";
            }
        }
        cout<<"\n";
    }
    return 0;
}
