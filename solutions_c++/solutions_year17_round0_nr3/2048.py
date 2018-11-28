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
     * пусть N = 12. каждый пытается зайти в середину самого большого отрезка (последовательности незанятых)
     * после 1-го станет два отрезка : {5,6} (разделил 12 на 5 и 6)
     * после 2-го : {2,3,5} (разделил 6 на 2 и 3)
     * после 3-го : {2,2,2,3} (разделил 5 на 2 и 2)
     * после 4-го : {1,1,2,2,2} (разделил 3 на 1 и 1)
     * далее в отрезках трижды максимумами является "2". это значит, что следующие три человека будут делить 2 на подотрезки
     * => надо хранить map из <длина_отрезка, число таких отрезков>
     * отрезки максимальной длины резать и правильно считать, сколько человек смогут так нарезать
     */
    for (int i = 0; i < T; ++i) {
        long long N, K;
        cin >> N >> K;

        map<long long, long long> data;     // <длина_отрезка, число таких отрезков>
        data.insert(make_pair(N, 1));
        pair<long long, long long> max_segment;
        pair<long long, long long> new_segment_1;
        pair<long long, long long> new_segment_2;

//        long long max_data_size = 1;        // ДЛЯ ИНТЕРЕСА - подсчёт сколько максимум будет размер map-ы на протяжении вычислений

        long long count_man = 0;            // считаем зашедших людей
        while (count_man < K) {
            max_segment = *data.rbegin();               // отрезок максимальной длины - это key в самой правой позиции map-ы
            new_segment_1 = make_pair(max_segment.first / 2, max_segment.second);
            new_segment_2 = make_pair(max_segment.first - new_segment_1.first - 1, max_segment.second);
            count_man += max_segment.second;
            data.erase((++data.rbegin()).base());                   // стираем максимальный отрезок
            data[new_segment_1.first] += new_segment_1.second;      // добавляем количество 1-х новых отрезков (сработает даже если не было такого ключа)
            data[new_segment_2.first] += new_segment_2.second;      // добавляем количество 2-х новых отрезков (сработает даже если не было такого ключа)

//            if (data.size() > max_data_size)      // ХАХАХА!!! оказалось, что хватает всего ТРЁХ элементов
//                max_data_size = data.size();
        }

        cout << "Case #" << (i + 1) << ": " << max(new_segment_1.first, new_segment_2.first) << " ";
        cout << min(new_segment_1.first, new_segment_2.first) << "\n";
    }


    // cout << fixed << result;

//    cin.rdbuf(cinbuf);   //reset to standard input again
    // getchar();

    return 0;
}
