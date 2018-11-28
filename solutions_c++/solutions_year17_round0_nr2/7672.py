#include <boost/timer/timer.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/ml/ml.hpp>
#include <vector>
#include <thread>
#include "testhelper.cc"
#include "Matrix.hh"

using namespace std;

int const LEN = 20;
int num[LEN];
long long decs[LEN];

long long f(int pos, int ls, int last){
    if (pos >= LEN)
        return 0;
    long long res=-1000000000000000000LL;
    if (ls){
        for (int i = last; i < 10; i++){
            long long a = f(pos+1, true, i);
            res = max(res, decs[pos]*i + a);
        }

    } else{
        for (int i = last; i < num[pos]; i++){
            long long a = f(pos+1, true, i);
            res = max(res, decs[pos]*i + a);
        }
        if (num[pos] >= last){
            long long b =f(pos+1, false, num[pos]);
            res = max(res, decs[pos]*num[pos] + b);
        }
    }
    return res;
}

void process(int test){
    long long d = 1;
    for (int i = 1; i <= 18; i++){
        decs[LEN - i] = d;
        d *= 10;
    }
    long long N;
    cin >> N;
    for (int i = 0; i < LEN; i++){
        num[i] = N % 10;
        N /= 10;
    }
    reverse(num, num + LEN);
    long long res = f(0, false, 0);

    cout << "Case #" << test << ": ";
    cout << res;
    cout << "\n";
}

int main(int argc, const char **argv) {
    freopen("/home/geka/Development/codejam/B.in", "r", stdin);
    freopen("/home/geka/Development/codejam/B.out", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++){
        process(t+1);
    }
    return 0;
}