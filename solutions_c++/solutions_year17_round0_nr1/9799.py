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

		string str;
		cin >> str;
		int K;
		cin >> K;

//		cout << "str: " << str << "\n";
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


//		while( (end_index - start_index + 1) >= K){
//			// get the first '-' at the left
//			while(str[start_index] == '+' && start_index <= end_index){
//				start_index++;
//			}
//
//			cout << "start_index: " << start_index << "\n";
//			cout << "end_index: " << end_index << "\n";
//            cout << "curr length: " << end_index - start_index + 1 << "\n";
//
//			if (start_index > end_index){
//                cout << "start_index > end_index" << "\n";
//                break;
//			}else if((end_index - start_index + 1) < K){
//                cout << "(end_index - start_index + 1) < K" << "\n";
//                break;
//			}
//
//            result_count++;
//			for (int i = start_index; i < start_index + K; i++){
//				str[i] = flipChar(str[i]);
//			}
//			cout << "(after)str1: " << str << "\n";
//
//			// get the first '-' at the right
//			while(str[end_index] == '+' && end_index >= start_index){
//				end_index--;
//			}
//
//
//            cout << "start_index: " << start_index << "\n";
//			cout << "end_index: " << end_index << "\n";
//			cout << "curr length: " << end_index - start_index + 1 << "\n";
//
//			if (end_index < start_index){
//                cout << "end_index < start_index" << "\n";
//                break;
//			}else if((end_index - start_index + 1) < K){
//                cout << "(end_index - start_index + 1) < K" << "\n";
//                break;
//			}
//
//            result_count++;
//			for (int i = end_index; i > end_index - K; i--){
//				str[i] = flipChar(str[i]);
//			}
//			cout << "(after)str2: " << str << "\n";
//
//            // 避免有無限一直互相翻的狀況
//            if ((end_index - start_index + 1) == K){
//                break;
//            }
//		}// end of inner while
//        if (result_count != 0){
            std::size_t found = str.find('-');
            if (found==std::string::npos){
                cout << "Case #" << caseIndex << ": " << result_count << "\n";
            }else{
                cout << "Case #" << caseIndex << ": " << "IMPOSSIBLE" << "\n";
            }

//            cout << "Case #" << caseIndex << ": " << result_count << "\n";
//        }else if (result_count == 0){
//            cout << "Case #" << caseIndex << ": " << "IMPOSSIBLE" << "\n";
//        }

		caseIndex++;

	}


	return 0;
}
