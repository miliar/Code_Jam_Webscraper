#include <algorithm>
#include <iostream>
#include <istream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <streambuf>
#include <string>
#include <vector>

using namespace std;

int main(){
	
	int i, j, t, T, K;
	string S;

	cin>>T;
	for(t=1; t<=T; t++){
		cin>>S>>K;
		
		int nFlips = 0;
		int n = S.length();
		for(i=0; i<n; i++){
			if(S.at(i) == '-'){
				int end = i+K - 1;// min K pancakes have to be flipped
				if(end < n){
					for(j=i; j<=end; j++){
						if(S.at(j) == '+'){
							S.replace(j, 1, 1, '-');
							
						}else{
							S.replace(j, 1, 1, '+');
						}
					}
					//cout<<S<<endl;
					nFlips++;
				}else{
					// check if there are no '-'. 
					// if '-' then it can never be made '+'
					break;
				}
			}
		}

		for(j=i; j<n; j++){
			if(S.at(j) == '-'){
				nFlips = -1; 
				break;
			}
		}

		if(nFlips == -1){
			cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
		}else{
			cout<<"Case #"<<t<<": "<<nFlips<<endl;
		}
		
	}
	
	return 0;
}