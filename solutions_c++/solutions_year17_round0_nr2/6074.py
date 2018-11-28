#include<iostream>
#include<cstring>
using namespace std;

int main(void){
	
	
	int n;
	
	cin >> n;
	
	for(int a = 1; a <= n; a++){
		string word;
		cin >> word;
		
		int i, j;
		for(i = 1; i < word.length(); i++){
			if(word[i] < word[i-1]){
				i--;
				word[i]--;
				for(;i > 0; i--){
					if(word[i] >= word[i-1])
						break;
					else
						word[i-1]--;
				}
				break;
			}
		}
		
		cout << "Case #" << a << ": ";
		
		if(!(word[0] == '0')){
			for(j = 0; j <= i; j++){
				if(j >= word.length())
					break;
				cout << word[j];
			}
				
		} 
			
		for(j = i+1; j < word.length(); j++)
			cout << "9";
		cout << endl;
		
		
	}
	
	
	
	
	return 0;
}
