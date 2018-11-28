#include <iostream>
#include <string>
#include <vector>

using namespace std;

using i64 = long long int;

// 132 -> 129

i64 get_tidy(i64 num) {

    i64 base = 10;
    i64 next_base = 100;

    while (num / base) {
        int a = (num % base) / (base / 10);
        int b = (num % next_base) / (next_base / 10);
        if (b > a) {
            num -= (num % base + 1);  //(a + 1) * base / 10;
            base *= 10;
        } else if (b == a) {
            next_base *= 10;
        } else if (b < a) {
            next_base *= 10;
            base *= 10;
        }
    }

    return num;

}



int main(int argc, char* argv[]) {
    int test_num = 0;
    cin >> test_num;
    for (int i = 0; i < test_num; ++i) {
        string str;
        i64 num = 0;
        cin >> num;
        cout << "Case #" << i + 1 << ": ";
        cout << get_tidy(num);
        cout << endl;
    }
    return 0;
}
