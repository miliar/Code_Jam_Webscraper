#include <boost/timer/timer.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/ml/ml.hpp>
#include <vector>
#include <thread>
#include "testhelper.cc"
#include "Matrix.hh"

using namespace std;
const int MAX = 1010;

void process(int test){
    char s[MAX];
    int k;
    cin >> s >> k;
    int res = 0;
    int l = strlen(s);
    for (int i = 0; i <= l - k; i++)
        if (s[i] == '-'){
            res++;
            for (int j = i; j < i + k; j++)
                if (s[j] == '+')
                    s[j] = '-';
                else
                    s[j] = '+';
        }
    bool ok = true;
    for (int i = 0; i < l ;i++)
        if (s[i] == '-')
            ok = false;
    cout << "Case #" << test << ": ";
    if (ok)
        cout << res;
    else
        cout << "IMPOSSIBLE";
    cout << "\n";
}

int main(int argc, const char **argv) {
    freopen("/home/geka/Development/codejam/A.in", "r", stdin);
    freopen("/home/geka/Development/codejam/A.out", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++){
        process(t+1);
    }
    return 0;
}