#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int t,i,index,k=1;
	//int *arr;
	string s;
	bool is_asc=true;
	char maxi;
	cin >> t;
	while(k<=t){
		cin >> s;
		is_asc=true;
		maxi='0';
		index=0;
		for(i=0;i<s.length()-1;i++){
			if(s[i] > s[i+1]){
				is_asc=false;
				if(s[i] == maxi){
					--s[index];
					break;
				}
				--s[i];
				index=i;
				break;

			}
			if(s[i] > maxi){
				maxi = s[i];	
				index = i;
			} 
		}
		i=0;
		if(s[0] == '0') i++;
		cout << "Case #" << k << ": ";
		while(i<s.length()){
			if(!is_asc && i > index) cout << 9;
			else cout << s[i];
			i++;
		}
		cout << endl;
		k++;
	}
	return 0;
}