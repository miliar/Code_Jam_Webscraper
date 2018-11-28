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
#include <iomanip>


using namespace std;

unsigned long long gcd(unsigned long long a, unsigned long long b) {    // Наибольший общий делитель
    return b == 0 ? a : gcd(b, a % b);
}

unsigned long long lcm(unsigned long long a, unsigned long long b) {    // Наименьшее общее кратное
    return (a*b) / gcd(a,b);
}

// =================================================================

struct sort_cake_desc {  // сортируем ПО УБЫВАНИЮ сначала по first. если first равны, то по second
    bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
        if (left.first != left.second) {
            return left.first > right.first;
        } else {
            return left.second > right.second;
        }

    }
};

void problem() {
    double N, K;
    cin >> N >> K;

    vector<pair<double, double>> data(N);       // radius / height
    for (int i = 0; i < N; ++i) {
        double r, h;
        cin >> r >> h;
        data[i] = make_pair(r, h);
    }

    sort(data.begin(), data.end(), sort_cake_desc());   // сортируем ПО УБЫВАНИЮ сначала по R. если R равны, то по H

    /**
     *  pi*R*R + 2*pi*R*H = pi*R*(R + 2*H)
     *  но состовляющая по радиусам зависит только от _нижнего_ блина
     *  значит перебором рассмотри каждого как первый блин. а на него наваливаем K-1 (но их радиусы тоже влияют на составляющцю высот!!!)
     */
    // т.к. мы хитро отсортировали - достаточно будет рассмотреть только первые N-K+1 блинов в качестве первых
    /**
     *  K-1 надо набирать просто беря максимальные произведения 2*pi*R*H (среди всех с радиусом не большим, чем нижний блин) -
     *  действительно, ведь раз их радиусы не больше, то их можно будет ну хоть как-то навалить сверху
     */
    vector<double> data_side_surface(N);    // боковые площади заранее подсчитаем для каждого
    for (int i = 0; i < N; ++i) {
        data_side_surface[i] = 2 * M_PI * data[i].first * data[i].second;
    }

    double result = 0;

    for (int i = 0; i < (N - K + 1); ++i) {
        double sub_result = 0;
        sub_result += M_PI * data[i].first * (data[i].first + 2 * data[i].second);      // от нижнего блина
        vector<double> side_copy;           // боковые площади у тех, кто может лежать сверху данного блина
        for (int j = i + 1; j < N; ++j) {
            side_copy.push_back(data_side_surface[j]);
        }
        sort(side_copy.begin(), side_copy.end(), std::greater<double>());       // по убыванию
        for (int j = 0; j < K - 1; ++j) {
            sub_result += side_copy[j];         // добавим лучших K-1
        }
        result = max(result, sub_result);
    }

    cout << fixed << setprecision(9) << result << "\n";
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
