#include<iostream>
#include<string>
using namespace std;

int main(){
	int loop = 0;
	cin >> loop;
	getchar();
	string output[100][25];
	for (int l = 0; l < loop; l++){
		string in[25];
		int R = 0, C = 0;
		cin >> R;
		cin >> C;
		getchar();

		for (int i = 0; i < R; i++){
			cin >> in[i];
			getchar();
		}
		for (int k = 0; k < 25; k++){
			for (int i = 0; i < R; i++){	//ヨコ
				for (int j = 0; j < C; j++){
					if (in[i].at(j) == '?'){
						if (j - 1 >= 0){		//左を参照
							if (in[i].at(j - 1) != '?'){
								in[i].at(j) = in[i].at(j - 1);
							}
						}
					}
				}

				for (int j = 0; j < C; j++){	//ヨコ
					if (in[i].at(j) == '?'){
						if (j + 1 < C){			//右を参照
							if (in[i].at(j + 1) != '?'){
								in[i].at(j) = in[i].at(j + 1);
							}
						}
					}
				}
			}
		}

		for (int k = 0; k < 25; k++){
			for (int i = 0; i < R; i++){
				bool q = false;
				for (int j = 0; j < C; j++){
					if (in[i].at(j) == '?'){
						q = true;
					}
				}
				if (q){
					if (i + 1 < R)
						in[i] = in[i + 1];
				}

			}

			for (int i = 0; i < R; i++){
				bool q = false;
				for (int j = 0; j < C; j++){
					if (in[i].at(j) == '?'){
						q = true;
					}
				}
				if (q){
					if (i - 1 >= 0)
						in[i] = in[i - 1];
				}
			}

		}

		for (int i = 0; i < R; i++){
			output[l][i] = in[i] + "\n";
		}

	}

	for (int i = 0; i < loop; i++){
		cout << "Case #" << i + 1 << ":\n";
		for (int j = 0; j < 25; j++)
			cout << output[i][j];
	}

	getchar();
	getchar();
	return 0;
}