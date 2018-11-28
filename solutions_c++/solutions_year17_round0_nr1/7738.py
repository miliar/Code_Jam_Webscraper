#include <iostream>
#include <string>
using namespace std;


int main(){
	int T = 0;
	cin >> T;
	string str;
	int k =0 ;
	for(int i =0; i < T; i ++ ){
		cin >> str;
		cin >> k;
		//cout << str << endl;
		//cout << k <<endl;
		int flips = 0;
		for(int j =0 ; j <= str.size() - k ; j ++ ){
			if(str[j] == '-' ){
				flips++;
				for(int z = j; z < j + k ; z ++){
					str[z] = str[z] == '+' ? '-' : '+';
				}
			}
		}
		int x = str.size() - k;
		while(x < str.size() && str[x] == '+'){
			x++;
		}
		cout<<"Case #" << i+1 <<": " ;
		if(x == str.size() ){
			//good
			cout<<flips<<endl;
			
		}
		else {//bad
			cout<<"IMPOSSIBLE" << endl;
		}
	}
	return 0;
}