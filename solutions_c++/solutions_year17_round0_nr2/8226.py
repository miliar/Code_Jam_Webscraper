#include <bits/stdc++.h>

using namespace::std;

int get_untidy_index(string N) {
    int size_of_N = N.size();
    for(int i=0; i<size_of_N-1; i++) {
        if (N[i] > N[i+1]) {
           return i;
        }
    }
    return -1;
}

void tidy_the_number(string& N, int size_of_N, int start) {
    N[start] = N[start]-1;
    for (int j = start + 1; j < size_of_N; j++) {
        N[j] = '9';
    }
}

void smallest_tidy_no(string N, const int caseno) {
    int size_of_N = N.size();
    if (size_of_N == 1) {
        cout << "Case #" << caseno << ": " << N << endl;
        return;
    } 

    int index = -1;
    while((index = get_untidy_index(N)) != -1) {
        tidy_the_number(N, size_of_N, index);
    }

    //trim leading zeros
    N.erase(0, N.find_first_not_of('0'));
    cout << "Case #" << caseno << ": " << N << endl;
}

int main() {
    int T;
    string N;
    int caseno = 1;

    freopen("tidy_numbers_large.in", "r", stdin);
    cin >> T;
    while(cin >> N) {
        smallest_tidy_no(N, caseno);
        caseno++;
    }

    return 0;
}