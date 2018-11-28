#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

int T;


int main() {
	ifstream fin("C-large.in", ifstream::in);
	ofstream fout("result.out", ofstream::out);
	fin >> T;
	//cin >> T;
	__int64 N, K;
	for(int i = 0; i < T; ++i) {
		fin >> N >> K;
        //cin >> N >> K;
        cout << N << " " << K << endl;  // for debug
        __int64 need_arange = K;
        __int64 space_num = 1;
        __int64 left, right;
        while (need_arange > space_num) {
            need_arange -= space_num;
            space_num *= 2;
        }
        cout << need_arange << " " << space_num << endl;  // for debug
        __int64 remain_stall_num = N - (K - need_arange);
        __int64 space_len = remain_stall_num / space_num;
        __int64 larger_space_num = remain_stall_num - space_len * space_num;
        if (need_arange <= larger_space_num) {
            left = (space_len + 1 - 1) / 2;
            right = space_len + 1 - 1 - left;
        } else {
            left = (space_len - 1) / 2;
            right = space_len - 1 - left;
        }

        fout << "Case #" << (i+1) << ": " << right << " " << left << endl;
        cout << "Case #" << (i+1) << ": " << right << " " << left << endl;
	}

	return 0;
}

