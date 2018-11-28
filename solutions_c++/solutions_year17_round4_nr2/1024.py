#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>

#define _USE_MATH_DEFINES

#include <cmath>

using namespace std;

/*
struct myclass {
    bool operator() (int i, int j) {
        if (Ri[i] < Ri[j])
            return true;
        else if (Ri[i] > Ri[j])
            return false;
        else {
            return Hi[i] < Hi[j];
        }
    }

    unsigned* Ri;
    unsigned* Hi;

} myTempObject;
*/

int main() {
	unsigned cases;
	cin >> cases;

	for (unsigned caseIndex = 1; caseIndex <= cases; ++caseIndex) {
        int N, C, M;
        int rides = 0, pros = 0;

        cin >> N >> C >> M;

        int** tickets = new int*[C];
        int* customer_count = new int[C];
        for (int i = 0; i < C; ++i) {
            tickets[i] = new int[N];
            customer_count[i] = 0;
            for (int j = 0; j < N; ++j)
                tickets[i][j] = 0;
        }

        for (int i = 0; i < M; ++i) {
            int p, b;
            cin >> p >> b;
            ++(tickets[b - 1][p - 1]);
            ++customer_count[b - 1];
        }
        if (C == 2) {
            int* conflicts = new int[N];

            int count = 0;
            int index = -1;
            int maxCount = 0;
            for (int i = 0; i < N; ++i) {
                conflicts[i] = min(tickets[0][i], tickets[1][i]);
                count += conflicts[i];
                
                if (conflicts[i] > maxCount) {
                    index = i;
                    maxCount = conflicts[i];
                }
            }

            if (2 * maxCount <= count) {
                rides = max(customer_count[0], customer_count[1]);
            } else {
                rides = max(customer_count[0], customer_count[1]);
                if (index == 0) {
                    int rest0 = customer_count[0] - tickets[0][0];
                    int rest1 = customer_count[1] - tickets[1][0];

                    tickets[0][0] -= rest1;
                    tickets[1][0] -= rest0;
                    int add = min(tickets[0][0], tickets[1][0]);
                    if (add > 0)
                        rides += add;
                } else {
                    int rest0 = customer_count[0] - tickets[0][index];
                    int rest1 = customer_count[1] - tickets[1][index];

                    tickets[0][index] -= rest1;
                    tickets[1][index] -= rest0;
                    int add = min(tickets[0][index], tickets[1][index]);
                    if (add > 0)
                        pros = add;
                }
            }
        }

        cout << "Case #" << caseIndex << ": " << rides << " " << pros << "\n";

        for (int i = 0; i < C; ++i) {
            delete[] tickets[i];
        }
        delete[] tickets;
        delete[] customer_count;
	}
}
