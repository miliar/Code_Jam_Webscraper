#include <iostream>
#include <string>

using namespace std;

int main() {
	int t,k,count,cando;
	string pcakes;
	
	cin >> t;
	
	for(int i=0;i<t;i++){
		cin >> pcakes >> k;
		count=0;
		cando=1;
		for(int j=0;j<pcakes.size()-k+1;j++){
			if(pcakes[j]=='-'){
				for (int l=0;l<k;l++){
					if(pcakes[j+l] == '-') pcakes[j+l]='+';
					else pcakes[j+l]='-';
				}
				count++;
			}
		}
		for(int j=pcakes.size()-k+1; j<pcakes.size();j++)
			if(pcakes[j]=='-') cando=0;
		cout << "Case #" << i+1 << ": " ;
		if(cando==0) cout << "IMPOSSIBLE" << endl;
		else cout << count << endl;
	} 	
return 0;
}
