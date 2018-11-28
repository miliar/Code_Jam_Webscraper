#include "iostream"
#include "fstream"
#include "map"
#include "utility"
using namespace std;

long long n;
long long k;
int t;

class Bathroom {

public:

    map<long long, long long> vacancies;
    Bathroom(long long n) {
        vacancies[n] = 1;
    }

    pair<long long, long long> addPerson() {
        pair<long long, long long> vacancy = pair<long long, long long>(vacancies.rbegin()->first, vacancies.rbegin()->second);
        if (vacancy.second == 1) {
            vacancies.erase(--vacancies.end());
        } else {
            vacancies.rbegin()->second = vacancies.rbegin()->second - 1;
        }
		long long rightDist= (vacancy.first - 1) / 2;
		long long leftDist = vacancy.first - 1 - rightDist;
        if (vacancies.count(leftDist) != 0) {
            vacancies[leftDist] = vacancies[leftDist] + 1;
        } else {
            vacancies[leftDist] = 1;
        }
        if (vacancies.count(rightDist) != 0) {
            vacancies[rightDist] = vacancies[rightDist] + 1;
        } else {
            vacancies[rightDist] = 1;
        }
        return pair<long long, long long>(leftDist, rightDist);
    }

	pair<long long, long long> addPersons(long long k) {
		pair<long long, long long> vacancy = pair<long long, long long>(vacancies.rbegin()->first, vacancies.rbegin()->second);
		if (vacancy.second >= k) {
			long long rightDist = (vacancy.first - 1) / 2;
			long long leftDist = vacancy.first - 1 - rightDist;
			return pair<long long, long long>(leftDist, rightDist);
		}
		else {
			long long rightDist = (vacancy.first - 1) / 2;
			long long leftDist = vacancy.first - 1 - rightDist;
			vacancies.erase(--vacancies.end());
			if (vacancies.count(leftDist) != 0) {
				vacancies[leftDist] = vacancies[leftDist] + vacancy.second;
			}
			else {
				vacancies[leftDist] = vacancy.second;
			}
			if (vacancies.count(rightDist)) {
				vacancies[rightDist] = vacancies[rightDist] + vacancy.second;
			}
			else {
				vacancies[rightDist] = vacancy.second;
			}
			return addPersons(k - vacancy.second);
		}
	}
};

int main() {

    //freopen("lin.txt", "r", stdin);
    freopen("C-large.in", "r", stdin);
    //freopen("B-large.in", "r", stdin);
    freopen("large.txt", "w", stdout);

    cin >> t;

    for (int testCase = 1; testCase <= t; testCase++) {

        cin >> n;
        cin >> k;

        Bathroom bathroom(n);

        pair<long long, long long> lastDists = bathroom.addPersons(k);
        cout << "Case #" << testCase << ": " << lastDists.first << " " << lastDists.second << endl;

    }

    return 0;

}
