#include <iostream>
#include <set>
#include <cmath>
#include <queue>

using namespace std;

set<unsigned long long> ocupados;

int main(int argc, char* argv[]) {

	int testCases = 0;
	cin >> testCases;

	unsigned long long stalls = 0, people = 0;
	for (int i = 0; i < testCases; i++) {

		cin >> stalls >> people;

		if (stalls == people) {
			cout << "Case #" << i + 1 << ": 0 0" << endl;
			continue;
		}

		priority_queue<unsigned long long> pq;
		pq.push(stalls);

		// Voy ocupando para todas las personas
		for (int i = 0; i < people - 1; ++i) {

			unsigned long long maxIntervalEmpty = pq.top();
			pq.pop();

			//cout << "Saco " << maxIntervalEmpty << " de la cola" << endl;

			maxIntervalEmpty--; // Ocupo el lugar

			//cout << "Ocupo lugar y quedan " << maxIntervalEmpty << " stalls vacíos para partir" << endl;

			if (maxIntervalEmpty != 0) {

				if (maxIntervalEmpty == 1) {
					//cout << "Pusheo el unico stall vacío que queda en este intervalo" << endl;
					pq.push(1);
				} else {
					unsigned long long firstInterval = (unsigned long long) floor(maxIntervalEmpty / ((float) 2));
					unsigned long long secondInterval = (unsigned long long) ceil(maxIntervalEmpty / ((float) 2));
					//cout << "Pusheo " << firstInterval << " como primer intervalo y " << secondInterval << " como segundo intervalo" << endl;
					pq.push(firstInterval); // Lado izq
					pq.push(secondInterval); // Lado der
				}
			}
		}

		// Calculo el último
		unsigned long long lastIntervalEmpty = pq.top(), ls, rs;
		//cout << "Saco " << lastIntervalEmpty << " de la cola" << endl;
		lastIntervalEmpty--;

		ls = (unsigned long long) floor(lastIntervalEmpty / ((float) 2));
		rs = (unsigned long long) ceil(lastIntervalEmpty / ((float) 2));

		cout << "Case #" << i + 1 << ": " << rs << " " << ls << endl;

	}
}