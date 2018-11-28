#include <string>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <fstream>


using namespace std;


int main() {
    ifstream in("../input.txt");
//    streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
    ofstream out("../output.txt");
//    streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    cout.rdbuf(out.rdbuf());

    int T;
    cin >> T;

    /**
     * проходим слева направо. если видим "слом" неубывания - слева уменьшаем на 1, справа заполняем 99..9 :
     * 77|43 -> 7699                - а потом опять идём с самого начала слева направо:
     *          7|699 -> 6999       - опять ВСЁ девятками справа. поэтому результат 6999, а не 6699 !
     *
     * 11012 -> 11|012 -> 10999 -> 1|0999 -> 09999 (end)
     * 22012 -> 22|012 -> 21999 -> 2|1999 -> 19999 (end)
     * 12012 -> 12|012 -> 11999 (end)
     */
    for (int i = 0; i < T; ++i) {
        long long N;
        cin >> N;
        // long long result = 0;

        string str = to_string(N);
        bool flag = false;
        while (!flag) {
            int pos;
            flag = true;
            for (int i = 1; i < str.size(); ++i) {
                if (str[i] < str[i - 1]) {
                    pos = i;
                    flag = false;
                    break;
                }
            }
            if (!flag) {
                str[pos - 1] = str[pos - 1] - 1;
                for (int i = pos; i < str.size(); ++i) {
                    str[i] = '9';
                }
            }
        }
        // и убрать ведущие нули
        int no_zero = 0;
        while (str[no_zero] == '0')
            no_zero++;
        str = str.substr(no_zero);

        // cout << "Case #" << (i + 1) << ": " << result << "\n";
        cout << "Case #" << (i + 1) << ": " << str << "\n";
    }


    // cout << fixed << result;

//    cin.rdbuf(cinbuf);   //reset to standard input again
    // getchar();

    return 0;
}
