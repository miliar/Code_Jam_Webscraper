#include <iostream>
using namespace std;

char flipChar(char c){
	if (c == '+') return '-';
	if (c == '-') return '+';
}


int main() {
	// your code goes here
	int T;
	cin >> T;
	int caseIndex = 1;
	while(T){
		T--;
//        cout << "T: " << T << "\n";

		string str;
		cin >> str;
//		cout << "str: " << str << "\n";
		int K;
		cin >> K;
//		cout << "K: " << K << "\n";


		// start from left the right, it the remain length is less thatn K, end it
		int start_index = 0;
		int end_index = str.length()-1;

//		cout << "start_index: " << start_index << "\n";
//		cout << "end_index: " << end_index << "\n";

		int result_count = 0;

//        cout << "before flipping: " << str << "\n";
		while( (end_index - start_index + 1) >= K ){
            // 若能進來,代表還可以至少翻一次
//            cout << "start_index: " << start_index << "\n";

            // 從左邊開始,找出最邊邊的'-'
			while(str[start_index] != '-' && (end_index - start_index + 1) >= K){
				start_index++;
			}
            // 若已經找到不能再翻的index,就離開
            if ( (end_index - start_index + 1) < K ){
                break;
            }
            // 現在已經找到最邊邊的'-',開始翻(這邊需要再優化)
			for (int i = start_index; i < start_index + K; i++){
				str[i] = flipChar(str[i]);
			}
			result_count++;
//            cout << "after  flipping: " << str << "\n";

		}// end of inner while

        std::size_t found = str.find('-');
        if (found==std::string::npos){
            cout << "Case #" << caseIndex << ": " << result_count << "\n";
        }else{
            cout << "Case #" << caseIndex << ": " << "IMPOSSIBLE" << "\n";
        }

		caseIndex++;

	}


	return 0;
}
