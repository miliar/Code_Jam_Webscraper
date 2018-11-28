#include <string>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <fstream>
#include <iomanip>


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
     * ...------------------------------400
     *        k2=200        k1=300
     *        s2=?          s1=10km/h
     *  первая дойдёт до финиша (без помех) за t1 = (400-300)/10 = 10h
     *  если вторая (без помех) дойдёт быстрее 10h - то они встретятся по пути и всё равно будет 10h
     *  если вторая (без помех) дольше - например 11h. то она просто не догонит первую. и будет 11 часов наша лошадь идти
     *  и т.д.
     *  значит, просто ищем время максимальное за какое лошади прошли бы без помех
     */
    for (int i = 0; i < T; ++i) {
        double D;
        int N;
        cin >> D >> N;
        double max_time = 0;
        for (int i = 0; i < N; ++i) {
            double km, speed;
            cin >> km >> speed;
            max_time = max(max_time, ((D - km) / speed));
        }

        double result = D / max_time;



        cout << "Case #" << (i + 1) << ": ";
        cout << fixed << setprecision(6) << result << "\n";
    }


    // cout << fixed << result;

//    cin.rdbuf(cinbuf);   //reset to standard input again
    // getchar();

    return 0;
}
