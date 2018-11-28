#include<iostream>
#include<cstring>
using namespace std;

int main(void){
	
	
	int n;
	
	cin >> n;
	
	for(int a = 1; a <= n; a++){
		string word;
		
		int k, count = 0;
		bool check = false;
		cin >> word >> k;
		
		for(int i = 0; i < word.length(); i++){
			if(word[i] == '-')
				check = false;
			if(i < word.length()-k+1){
				if(word[i] == '-'){
					for(int j = 0; j < k; j++){
						if(word[j+i] == '-')
							word[j+i] = '+';
						else
							word[j+i] = '-';
					}		
					count++;
				}
				check = true;
			}
		}
		
		cout << "Case #" << a << ": ";
		
		if(!check)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << count << endl;
	}
	
	
	
	
	return 0;
}
