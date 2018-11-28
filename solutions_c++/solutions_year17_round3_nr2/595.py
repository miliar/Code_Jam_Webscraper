#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct myclass {
    bool operator() (unsigned i, unsigned j) {
        return Sc[i] < Sc[j];
    }

    unsigned* Sc;

} myTempObject;

struct myclass2 {
    bool operator() (unsigned i, unsigned j) {
        return Sj[i] < Sj[j];
    }

    unsigned* Sj;

} myTempObject2;

int main() {
	unsigned cases;
	cin >> cases;

	for (unsigned caseIndex = 1; caseIndex <= cases; ++caseIndex) {
        unsigned Ac, Aj;
        cin >> Ac >> Aj;

        unsigned* Sc = new unsigned[Ac];
        unsigned* Ec = new unsigned[Ac];
        unsigned* Sj = new unsigned[Aj];
        unsigned* Ej = new unsigned[Aj];

        for (unsigned i = 0; i < Ac; ++i)
            cin >> Sc[i] >> Ec[i];

        for (unsigned i = 0; i < Aj; ++i)
            cin >> Sj[i] >> Ej[i];

        unsigned freetime = 0;
        unsigned Ctime = 0;
        unsigned Jtime = 0;
        vector<unsigned> CCtime;
        vector<unsigned> JJtime;

        myTempObject.Sc = Sc;
        myTempObject2.Sj = Sj;

        vector<unsigned> c_order;
        vector<unsigned> j_order;

        for (unsigned i = 0; i < Ac; ++i)
            c_order.push_back(i);

        for (unsigned i = 0; i < Aj; ++i)
            j_order.push_back(i);


        sort(c_order.begin(), c_order.end(), myTempObject);
        sort(j_order.begin(), j_order.end(), myTempObject2);

        bool startC = false;
        bool endC = false;

        unsigned exchange = 0;
        if (j_order.empty()) {
            startC = true;
            endC = true;
        } else if (c_order.empty()) {

        } else {
            startC = Sc[c_order.front()] < Sj[j_order.front()];
            endC = Sc[c_order.back()] > Sj[j_order.back()];
        }


        if (startC && endC)
            CCtime.push_back(Sc[c_order.front()] + 1440 - Ec[c_order.back()]);
        else if (!startC && !endC)
            JJtime.push_back(Sj[j_order.front()] + 1440 - Ej[j_order.back()]);
        else if (startC && !endC) {
            ++exchange;
            freetime += Sc[c_order.front()] + 1440 - Ej[j_order.back()];
        } else {
            ++exchange;
            freetime += Sj[j_order.front()] + 1440 - Ec[c_order.back()];
        }

        bool prev_c = startC;
        unsigned prev_index;
        unsigned next_c = 0, next_j = 0;
        if (startC) {
            prev_index = c_order[0];
            Ctime += Ec[prev_index] - Sc[prev_index];
            ++next_c;
        } else {
            prev_index = j_order[0];
            Jtime += Ej[prev_index] - Sj[prev_index];
            ++next_j;
        }

        while (next_c != Ac || next_j != Aj) {
            bool n_c = false;
            if (next_j == Aj) {
                n_c = true;
            } else if (next_c == Ac) {

            } else {
                n_c = Sc[c_order[next_c]] < Sj[j_order[next_j]];
            }


            if (n_c) {
                Ctime += Ec[c_order[next_c]] - Sc[c_order[next_c]];

                if (prev_c) {
                    CCtime.push_back(Sc[c_order[next_c]] - Ec[prev_index]);
                } else {
                    freetime += Sc[c_order[next_c]] - Ej[prev_index];
                    ++exchange;
                }
                prev_index = c_order[next_c];
                ++next_c;
            } else {
                Jtime += Ej[j_order[next_j]] - Sj[j_order[next_j]];

                if (prev_c) {
                    freetime += Sj[j_order[next_j]] - Ec[prev_index];
                    ++exchange;
                } else {
                    JJtime.push_back(Sj[j_order[next_j]] - Ej[prev_index]);
                }
                prev_index = j_order[next_j];
                ++next_j;
            }

            prev_c = n_c;
        }

        unsigned c_total = Ctime;
        for (int i = 0; i < CCtime.size(); ++i)
            c_total += CCtime[i];
        unsigned j_total = Jtime;
        for (int i = 0; i < JJtime.size(); ++i)
            j_total += JJtime[i];

        if (c_total > 720) {
            sort(CCtime.begin(), CCtime.end());
            while (c_total > 720 && !CCtime.empty()) {
                exchange += 2;
                c_total -= CCtime.back();
                CCtime.pop_back();
            }
        } else if (j_total > 720) {
            sort(JJtime.begin(), JJtime.end());
            while (j_total > 720) {
                exchange += 2;
                j_total -= JJtime.back();
                JJtime.pop_back();
            }
        }



        cout << "Case #" << caseIndex << ": " << exchange << "\n";
        delete[] Sc;
        delete[] Ec;
        delete[] Sj;
        delete[] Ej;
	}
}
