#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <queue>
#include <cmath>

using namespace std;

string itos(int i) {
	ostringstream s;
	s << i;
	return s.str();
}

int N, M;

string INITIAL[105][105], B_plus[105][105],B_cross[105][105], FINAL[105][105];
int POSSIBLE[105][105];

int countR[105], countC[105];
vector<int> userbleR, userbleC;

int ans1, ans2;
vector<string> ans_str;

void REP_INITIAL(void) {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cout << INITIAL[i][j];
		}
		cout << endl;
	}
}

void REP_B_plus(void) {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cout << B_plus[i][j];
		}
		cout << endl;
	}
}

void REP_B_cross(void) {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cout << B_cross[i][j];
		}
		cout << endl;
	}
}

void REP_FINAL(void) {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cout << FINAL[i][j];
		}
		cout << endl;
	}
}

void REP_POSSIBLE(void) {
	for(int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (POSSIBLE[i][j] == -1) { std::cout << "N"; }
			else { std::cout << "."; }
		}
		std::cout << endl;
	}

}

void PLACE(int i, int j) { // (i,j)に"+"を配置したときに斜め方向に不可になることを記録
	for (int p = 0; p <= N; p++) {
		if (i - p >= 1 && j - p >= 1) { POSSIBLE[i - p][j - p] = -1; }
		if (i + p <= N && j + p <= N) { POSSIBLE[i + p][j + p] = -1; }
		if (i - p >= 1 && j + p <= N) { POSSIBLE[i - p][j + p] = -1; }
		if (i + p <= N && j - p >= 1) { POSSIBLE[i + p][j - p] = -1; }
	}

}
int diag_check(int i, int j) { //対角方向を見て"+"がないかどうか判断

	for(int p=1;p<=N;p++){
		if (i - p >= 1 && j - p >= 1) { if (B_plus[i-p][j-p]!=".") { return -1; }  }
	}

	for (int p = 1; p <= N; p++) {
		if (i + p <= N && j + p <= N) { if (B_plus[i + p][j + p] !=".") { return -1; } }
	}

	for (int p = 1; p <= N; p++) {
		if (i - p >= 1 && j + p <= N) { if (B_plus[i - p][j + p] !=".") { return -1; } }
	}

	for (int p = 1; p <= N; p++) {
		if (i + p <= N && j - p >= 1) { if (B_plus[i + p][j - p] !=".") { return -1; } }
	}
	
	return 1;

}

int check_devide(int i, int j) { //分裂できるかどうかのチェック
	
	for (int p = 1; p <= N; p++) {
		if (i - p >= 1 && j - p >= 1) { if (POSSIBLE[i - p][j - p] ==-1) { return -1; } }
	}

	for (int p = 1; p <= N; p++) {
		if (i + p <= N && j + p <= N) { if (POSSIBLE[i + p][j + p] ==-1) { return -1; } }
	}

	for (int p = 1; p <= N; p++) {
		if (i - p >= 1 && j + p <= N) { if (POSSIBLE[i - p][j + p] == -1) { return -1; } }
	}

	for (int p = 1; p <= N; p++) {
		if (i + p <= N && j - p >=1) { if (POSSIBLE[i + p][j - p] ==-1) { return -1; } }
	}

	return 1;

}

void ASSIGN_PLUS(void) { // +を割り当てる

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {


			if (B_plus[i][j] == ".") { //　空いた場所
				int sign1, sign2;
				sign1 = diag_check(i, j);
				sign2=check_devide(i, j);
				//cout << "(" << i << "," << j << ")  sign1= " << sign1 <<" sign2= " <<sign2<< endl;
				if (sign1 == -1) { continue; } //置けない場合
				else {  //分裂できる可能性を調べる
					if (i + j <= N + 1 && i >= j && POSSIBLE[i - j + 1][1] == 0 && POSSIBLE[i + j - 1][1] == 0) { B_plus[i - j + 1][1] = "+"; PLACE(i - j + 1, 1);  B_plus[i + j - 1][1] = "+";  PLACE(i + j - 1, 1); continue; }
					if (i + j <= N + 1 && i < j  && POSSIBLE[1][j - i + 1] == 0 && POSSIBLE[1][j + i - 1] == 0) { B_plus[1][j - i + 1] = "+"; PLACE(1, j - i + 1);  B_plus[1][j + i - 1] = "+"; PLACE(1, j + i - 1); continue; }
					if (i + j > N + 1 && i >= j  && POSSIBLE[N][j - N + i] == 0 && POSSIBLE[N][N - i + j] == 0) { B_plus[N][j - N + i] = "+"; PLACE(N, j - N + i);  B_plus[N][N - i + j] = "+"; PLACE(N, N - i + j); continue; }
					if (i + j > N + 1 && i < j   && POSSIBLE[i + N - j][N] == 0 && POSSIBLE[i - N + j][N] == 0) { B_plus[i + N - j][N] = "+"; PLACE(i + N - j, N); B_plus[i - N + j][N] = "+"; PLACE(i - N + j, N); continue; }
					B_plus[i][j] = "+"; PLACE(i, j);
				}
				
			}
		}
	}

}

void DERIVE_FINAL(void) {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (B_plus[i][j] == "+" && B_cross[i][j] == "x") { FINAL[i][j] = "o"; }
			else if (B_plus[i][j] == "+" && B_cross[i][j] == ".") { FINAL[i][j] = "+"; }
			else if (B_plus[i][j] == "." && B_cross[i][j] == "x") { FINAL[i][j] = "x"; }
			else { FINAL[i][j] = "."; }

		}
	}
}

void COMPARE_INITIAL_AND_FINAL(void) {
	ans1 = 0; ans2 = 0; ans_str.clear(); // 初期化

	string temp;

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (FINAL[i][j] == "o") { ans1 += 2; }
			else if (FINAL[i][j] == "+") { ans1++; }
			else if (FINAL[i][j] == "x") { ans1++; }

			if (INITIAL[i][j] != FINAL[i][j]) { ans2++;
			temp = FINAL[i][j] + " " + itos(i) + " " + itos(j);
			ans_str.push_back(temp);
			}
		}
	}
}

int main()
{
	ifstream ifs("D-small-attempt0.in");
	ofstream ofs("answer_D_small");

	int T;
	ifs >> T; cout << "T= " << T << endl;

	for (int t = 0; t<T; t++) {  // test cases
		ifs >> N; cout << "N= " << N << endl;
		ifs >> M; cout << "M = " <<M<<endl;

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				INITIAL[i][j] = "."; B_plus[i][j] = "."; B_cross[i][j] = "."; //初期化
			}
		}
		for(int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				POSSIBLE[i][j] = 0;
			}
		}

		

		for (int i = 1; i <= N; i++) { countR[i] = 0; } //初期化
		for (int j = 1; j <= N; j++) { countC[j] = 0; } //初期化
		userbleR.clear(); userbleC.clear();

		string str; int R, C;
		for (int i = 0; i < M; i++) {
			ifs >> str;  ifs >> R; ifs >> C;
			INITIAL[R][C] = str; 
			if (str == "+" || str == "o") { B_plus[R][C] = "+";  PLACE(R, C); /* REP_POSSIBLE(); */} // +の扱い
			if (str == "x" || str == "o") { B_cross[R][C] = "x";  
			countR[R] = 1;  countC[C] = 1;
			           } // xの扱い
		}

		for (int i = 1; i <= N; i++) { if (countR[i] == 0) { userbleR.push_back(i); } }
		for (int j = 1; j <= N; j++) { if (countC[j] == 0) { userbleC.push_back(j); } }

		while (int(userbleR.size()) > 0) {
			int R = userbleR[int(userbleR.size()) - 1];
			int C = userbleC[int(userbleC.size()) - 1];
			B_cross[R][C] = "x";
			userbleR.pop_back();
			userbleC.pop_back();
		}

		// cout << "INITIAL : " << endl;  REP_INITIAL();

		//REP_B_cross();

		//cout << "元" << endl;  REP_B_plus();

	

		ASSIGN_PLUS();

		//cout << "割り当て後" << endl; REP_B_plus();

		DERIVE_FINAL();

	//	cout << "FINAL : " << endl;  REP_FINAL();

		COMPARE_INITIAL_AND_FINAL();


		cout << "Case #" << t + 1 << ": " <<ans1 <<" " << ans2<< endl;
	//	for (int i = 0; i<int(ans_str.size()); i++) { cout << ans_str[i] << endl; }
		ofs << "Case #" <<t+1<<": " << ans1 << " " << ans2 << endl;
		for (int i = 0; i<int(ans_str.size()); i++) { ofs << ans_str[i] << endl; }

	} // end of test cases

	system("pause");

	return 0;
}