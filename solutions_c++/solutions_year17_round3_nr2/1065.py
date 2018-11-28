#include <string>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <fstream>
#include <cmath>
#include <stack>


using namespace std;

unsigned long long gcd(unsigned long long a, unsigned long long b) {    // Наибольший общий делитель
    return b == 0 ? a : gcd(b, a % b);
}

unsigned long long lcm(unsigned long long a, unsigned long long b) {    // Наименьшее общее кратное
    return (a*b) / gcd(a,b);
}

// =================================================================

void problem() {
    int Ac, Aj;
    cin >> Ac >> Aj;

    vector<pair<int, int>> data_Cam(Ac);
    vector<pair<int, int>> data_Jam(Aj);
    for (int i = 0 ; i < Ac; ++i) {
        int start, end;
        cin >> start >> end;
        data_Cam[i] = make_pair(start, end);
    }
    for (int i = Ac; i < Ac + Aj; ++i) {
        int start, end;
        cin >> start >> end;
        data_Jam[i - Ac] = make_pair(start, end);
    }

    int result = 0;

    // ONLY for SMALL DATASET :
    /**
     * Small dataset - на двоих неболее двух активностей
     * если это по одному у каждого - то ровно 2 смены - где-то посередине между активностями и через 12 часов
     * если на двоих всего одна активность - тоже ровно 2 смены
     * если обе активности у одного родителя - если начало одной и конец другой отстоят на <=12h (УЧЕСТЬ ПЕРЕХОД ЧЕРЕЗ СУТКИ!!!), то 2 смены, иначе 4 смены
     */
    // ONLY for SMALL DATASET :
    if ((Ac == 1 && Aj == 1) || (Ac + Aj == 1)) {
        result = 2;
    } else {    // если обе активности у одного родителя...
        pair<int, int> pair_1;
        pair<int, int> pair_2;
        if (Ac == 2) {
            pair_1 = data_Cam[0];
            pair_2 = data_Cam[1];
        } else {
            pair_1 = data_Jam[0];
            pair_2 = data_Jam[1];
        }
        if (pair_1.first > pair_2.first) {
            swap(pair_1, pair_2);               // сортируем, чтобы pair_1 была слева
        }

        if ((pair_2.second - pair_1.first <= 720) ||
                (pair_1.second + 1440 - pair_2.first <= 720)) {
            result = 2;
        } else {
            result = 4;
        }
    }
    cout << result << "\n";
}

int main() {
    ifstream in("../input.txt");
    cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
    ofstream out("../output.txt");
    cout.rdbuf(out.rdbuf());

    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cout << "Case #" << i + 1  << ": ";
        problem();
    }


    return 0;
}
