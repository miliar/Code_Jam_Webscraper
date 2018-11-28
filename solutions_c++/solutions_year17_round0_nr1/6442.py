#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(){
	int n, d;
	string s;
	cin>>n;
	for(int i = 0; i<n; i++){
		cin>>s>>d;
		int counter = 0;
		int pointer = 0;
		int happy = 0;

		for(int j=0; j<s.length(); j++){
			if(s[j] == '-')
				happy++;
		}

		while(counter <= 100000){
			if(s[pointer] == '-'){
				if(pointer + d <= s.length()){
					//switch to the right
					
					for(int k=0; k<d; k++){
						if(s[k+pointer] == '-'){
							s[pointer+k] = '+';
							happy--;
						} else{
							s[pointer+k] = '-';
							happy++;
						}
					}
				} else{
					//backward and switch to the right

					//+++-+ 3 - (5 - 3) = 1

					int dif = d - (s.length() - pointer);
					pointer -= dif;
					
					for(int k=0; k<d; k++){
						if(s[k+pointer] == '-'){
							s[pointer+k] = '+';
							happy--;
						} else{
							s[pointer+k] = '-';
							happy++;
						}
					}
				}
				counter++;
			}
			if(pointer == s.length())
				pointer = 0;
			else
				pointer++;
			//cout<<counter<<" "<<s<<" "<<happy<<endl;

			//stopping criteria
			if(happy == 0)
				break;
		}

		cout<<"Case #"<<(i+1)<<": ";
		if(happy == 0){
			cout<<counter<<endl;
		} else{
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}