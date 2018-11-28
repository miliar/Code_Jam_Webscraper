#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin >> t;
	long long int n;
	for(int j=0;j<t;j++){
		cin >> n;
		long long int x = n;
		vector<int> num;
		while(x>0){
			num.push_back(x%10);
			x /= 10;
		}
		int index = -1;
		for(int i=0;i<num.size()-1;i++){
			if(num[i]<num[i+1]){
				num[i+1] -= 1;
				index = i;
				//cout << index << " " << num[i+1] << endl;
			}
		}
		long long int ans = 0;
		/*cout << "index: " << index << endl;
		for(int i=num.size()-1;i>=0;i--){
			cout << num[i];
		}
		cout << endl;
		cout << "size:" << num.size() << endl;*/
		for(int i=0;i<num.size();i++){
			if(i <= index){
				x = 9;
			}
			else{
				x = num[i];
			}
			ans = ans + (long long int)pow(10,i)*x;
			/*cout << i << ":" << x << endl;
			cout << ans << endl;
			cout << (long long int)pow(10,i)*x << endl;
			cout << endl;*/
		}
		cout << "Case #" << j+1 << ": " << ans << endl;
	}
}