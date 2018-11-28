#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    for(int i = 1; i <= t; i++){
        cout<<"Case #"<<i<<": ";
        string a;
        cin>>a;
		for(int j = a.size()-1; j>=1; j--){
			if(a[j] < a[j-1]){
				for(int k = j; k< (int)a.size(); k++){
					a[k] = '9';
				}		
				a[j-1]--;
			}
		}

        string res;
        bool first = false;
        for(int j = 0; j < (int)a.size(); j++){
			if(a[j] != '0'){
				first = true;
			}
			if(first){
				res += a[j];
			}
        }
        cout<<res<<endl;
    }
	return 0;
}
