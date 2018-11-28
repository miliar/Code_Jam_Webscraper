#include <iostream>
#include <string>

using namespace std;

int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("out.txt","w+",stdout);
	
	string number, max, ans;
	int tc, len, aux;
	bool flag;
	
	max = "999999999999999999999999999";
	
	cin >> tc;
	
	for(int i = 1; i <= tc; i++){
		cin >> number;
		
		len = number.length();
		
		if(len == 1){
			cout << "Case #" << i << ": " << number << "\n";
		}else{
			ans = "";	flag = true;
			for(int j = 1; j < len && flag; j++){
				if(number[j] < number[j - 1]){
					if(number[j - 1] == number[0] || (j - 1 == 0)){
						aux = number[0];
						if(aux > '1')
							ans = (char)--aux;
						ans += max.substr(0, len - 1);
					}else{
						aux = number[j - 1];
						number[j - 1] = (char)--aux;
						ans = number.substr(0, j);
						ans += max.substr(0, len - j);
					}
					cout << "Case #" << i << ": " << ans << "\n";
					flag = false;
				}
			}
			if(flag)
				cout << "Case #" << i << ": " << number << "\n";
		}
	}
	
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}
