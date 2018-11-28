#include <iostream>
#include <string>
using namespace std;

int main()
{
	int N;
	cin >> N;
	for(int i=1;i<=N;i++){
		string str;
		int K;
		cin >> str >> K;
		int flip = 0;
		for(int j=0;j<str.size();j++){
			if(str[j] == '-'){
				flip++;
				for(int k=0;k<K;k++){
					if(j+k >= str.size()){
						flip = -1;
						break;
					}
					else{
						if(str[j+k] == '-')
							str[j+k] = '+';
						else
							str[j+k] = '-';
					}
				}
			}
			if(flip == -1) break;
		}
		cout << "Case #" << i << ": ";
		if(flip != -1)
			cout << flip << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
}