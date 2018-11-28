#include <iostream>
#include <cstdio>
#include <string>
#define ll long long
using namespace std;

ll bg(string& A, string& B){
	int i;
	for(i = 0; i < A.size(); i++){
		if(B[i] > A[i]) return 0;
		else if(A[i] > B[i])	return 1;
	}
	return 0;
}

ll tidy(string& A){
	int i;
	for(i = 1; i < A.size(); i++){
		if(A[i] < A[i-1])
			return 0;
	}
	return 1;
}

int main(){
	//freopen("inputla.in", "r", stdin);
	//freopen("outputlarge.out", "w", stdout);
	ll T, it, N, i, iit, jjt, j, k;
	cin >> T;
	string str, ptr;
	for(it = 1; it <= T; it++){
		cin >> str;
		if(str.size() <= 1){
			cout << "Case #" << it << ": " << str << "\n";
			continue;
		}
		ptr = str;
		for(i = 0; i < ptr.size(); i++){
			ptr[i] = '1';
		}
		if(tidy(str)){
			cout << "Case #" << it << ": " << str << "\n";
			continue;
		}
		if(bg(ptr, str)){
			ptr.clear();
			for(i = 0; i < str.size()-1; i++){
				ptr.push_back('9');
			}
			cout << "Case #" << it << ": " << ptr << "\n";
			continue;
		}
		iit = 0;
		for(i = 0; i < str.size(); i++){
			j = 9;
			while(1){
				for(k = iit; k < str.size(); k++){
					ptr[k] = '0'+j;
				}
				if(bg(str,ptr)){
					break;
				}
				j--;
			}
			iit++;
		}
		cout << "Case #" << it << ": " << ptr << "\n";
	}
}
