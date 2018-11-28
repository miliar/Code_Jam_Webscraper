#include<iostream>
using std::cin;
using std::cout;
char arr[1024];
int main() {
	int T;
	cin >> T;
	cin.get();
	for (int caseN = 1; caseN <= T; caseN++) {
		int n = 0;
		char ch = ' ';

		long long ans = 0;
		do {
			ch = cin.get();
			switch (ch) {
			case '0':
			case '1':
			case '2':
			case '3':
			case '4':
			case '5':
			case '6':
			case '7':
			case '8':
			case '9':
				ans *= 10;
				ans += ch - '0';
				arr[n] = ch-'0';
				n++;
				ch = 'T';
				break;
			}

		} while (ch == 'T');
		//cin.get();
		//do calc
		for (int i = 1; i < n; i++){
			if (arr[i] < arr[i - 1]){
				//eraser
				if (arr[i] == 0){
					arr[i] = 9;
					arr[i - 1] = arr[i - 1] - 1;
					for (int j = i - 1; j >= 1; j--){
						if (arr[j] < arr[j - 1]){
							arr[j] = 9;
							arr[j - 1] = arr[j - 1] - 1;
						}
						
					}
				}
				else {
					
					arr[i - 1] = arr[i - 1] - 1;
					arr[i] = 9;
					for (int j = i - 1; j >= 1; j--){
						if (arr[j] < arr[j - 1]){
							arr[j] = 9;
							arr[j - 1] = arr[j - 1] - 1;
						}

					}
				}
				for (int j = i + 1; j < n; j++){
					arr[j] = 9;
				}
				break;
			}
		}

		//check for impossible
		cout << "Case #" << caseN << ": ";
		if (arr[0] != 0) cout << int(arr[0]);
		for (int i = 1; i < n; i++){
			cout << int(arr[i]);
		}
		cout << std:: endl;

	}
	//system("PAUSE");
	return 0;
}
/*
2번문제 분석

1에서 1000까지는 노가다(스몰은 이걸로 가능)
라지 도전방법:

1~9는 타이디
0들어가면 안타이디

각 자리수별 구간 정리

11~1 to 19~9
22~2 to 29~9
33~3 to 39~9
44~4 to 49~9
55~5 to 59~9
66~6 to 69~9
77~7 to 79~9
88~8 to 89~9
99~9(1개)
1시작구간 세분
111~1 to 119~9
122~2 to 129~9
133~3 to 139~9
144~4 to 149~9
155~5 to 159~9
166~6 to 169~9
177~7 to 179~9
188~8 to 189~9
199~9(1개)
알고리즘:
우선 첫자리를 읽는다. 이때 x~x보다 작으면 전구간의 y9~9를 리턴
자리수를 보며 앞보다 같거나 크면 계속 옮김
작은애 뜨면: 앞에자리만으로 구성된 수에서 1을 뺌, 그리고 나머지는 9로 채움
이때 주의:앞으로 가면서 다시 작은애 확인 알고리즘 필요

예:1000
1
10(!): 10->9로 채움, 나머지는 9로 변환


11111111110
1
11
1111111111
11111111110(!)
11111111109
11111111099
11111110999
11111109999
11111099999
11110999999
11109999999
11099999999
10999999999
09999999999

1000
0999


11111200000
1111120
11111199999

11122223111
11122223111
11122223099
11122222999
*/