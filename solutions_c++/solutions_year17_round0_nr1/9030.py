#include <iostream>
using namespace std;
 
char flipChar(char c){
	if (c == '+') return '-';
	if (c == '-') return '+';
}
 
 
int main() {
	int T;
	cin >> T;
	int caseIndex = 1;
	while(T){
		T--;
 
		string str;
		cin >> str;
		int K;
		cin >> K;
		int start_index = 0;
		int end_index = str.length()-1;
		int result_count = 0;
 
		while( (end_index - start_index + 1) >= K){
			while(str[start_index] == '+' && start_index <= end_index){
				start_index++;
			}
 
			result_count++;
			for (int i = start_index; i < start_index + K; i++){
				str[i] = flipChar(str[i]);
			}
			// cout << "(after)str1: " << str << "\n";
 
			// get the first '-' at the right
			while(str[end_index] == '+' && end_index >= start_index){
				end_index--;
			}
 
 
           		if (end_index < start_index){
                            break;
			}else if((end_index - start_index + 1) < K){
                // cout << "(end_index - start_index + 1) < K" << "\n";
                break;
			}
 
            result_count++;
			for (int i = end_index; i > end_index - K; i--){
				str[i] = flipChar(str[i]);
			}
            if ((end_index - start_index + 1) == K){
                break;
            }
		}
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
