#include <iostream>
#include <string>

using namespace std;

void tidynumber();
string n;

int j;
int main(){
	
	int t = 0;
	cin >> t;
	for(j = 0; j < t; ++j ){
		cin >> n;
		tidynumber();
	}
	
}

void tidynumber(){
	 size_t size = n.length();
	 size_t repos = -1;
	 bool repeated = false;
	 
	 for(size_t i = 0; i < size - 1 ; ++i){
		 
		if(n[i] == n[i + 1] && !repeated){
			repos = i;
			repeated = true;
		}else if((n[i] > n[i + 1]) && !repeated){
			n[i] = n[i] - 1;
			n.replace(i + 1, size - i - 1, size - i - 1, '9');
			break;
		}else if(n[i] > n[i + 1]){
			n[repos] = n[repos] - 1;
			n.replace(repos + 1, size - repos - 1, size - repos - 1, '9');
		}
	 }
	 
	if(n[0] == '0')
		n.erase(0,1);
	cout <<"Case #" << (j + 1) << ": " << n << endl;
}
