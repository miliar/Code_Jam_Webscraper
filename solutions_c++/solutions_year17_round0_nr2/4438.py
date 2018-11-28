#include <iostream>
#include <string>
using namespace std;

int main() {
int t;
string nbr;

cin >> t ;
	
for(int i=0; i<t; i++){
	cin >> nbr ; 
	for(int j=nbr.size()-1; j>0; j--){
		if(nbr[j] < nbr[j-1]){
			nbr[j]='9';
			for(int k=j-1; k>=0; k++){
				if (nbr[k]-'0' == 0 ) nbr[k]='9';
				else nbr[k]--;break;
			}
		if( k+1 < nbr.size() && nbr[k+1] == '9')
			for(int l = k + 2; l < nbr.size(); l++)
				nbr[l] = '9';
		}
	}	
	nbr.erase(0,nbr.find_first_not_of('0'));
	cout << "Case #" << i+1 << ": " << nbr << endl; 
}
return 0;
}
