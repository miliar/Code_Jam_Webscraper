#include<iostream>
#include<string>

using namespace std;

int t;

string n;

int j;

int main(){
	ios_base::sync_with_stdio(0);
	
	cin >> t;
	
	for(int test = 1; test <= t; test++){
		cin >> n;
		
		for(int i = 0; i < (n.size() - 1); i++){
			if(n[i] > n[i+1]){
				j = i;
				while(j > 0 && n[j-1] == n[i]){
					j--;
				}
				n[j]--;
				for(int i = (j+1); i < n.size(); i++){
					n[i] = '9';
				}
				if(n[0] == '0'){
					n = n.substr(1);
				}
				break;
			}
		}
		
		
		cout << "Case #"<<test<<": "<<n<<"\n";
	}
	cout << endl;
	
	return 0;	
}