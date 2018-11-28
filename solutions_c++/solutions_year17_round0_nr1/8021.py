#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
char input[1001];
int k;
int flip(){
	int count = 0;
	while ( true ){
		bool flag = false;
		for ( int i = 0 ; i < strlen(input) ; i ++ ){
			if ( input[i] == '-'){
				count ++;
				for ( int j = 0 ; j < k ; j ++ ){
					if ( j + i >= strlen(input) ){
						return -1;
					}
					input[i + j] = input[i + j] == '-' ? '+' : '-';
				}
				flag = true;
				break;
			}
		}
		if ( !flag ){
			return count;
		}
	}
	return count;
}
int main(){ 
    ofstream fout("A.out"); 
	int n;
	cin >> n;
	for ( int i = 0 ; i < n ; i ++ ){
		memset(input, 0 , sizeof(input));
		cin >> input;
		cin >> k;
		int temp = flip();
		if ( temp != -1 )
			fout << "Case #" << i + 1 <<": " << temp  <<  endl;
		else 
			fout << "Case #" << i + 1 <<": " << "IMPOSSIBLE" <<  endl;
	}
	
	return 0;
}

