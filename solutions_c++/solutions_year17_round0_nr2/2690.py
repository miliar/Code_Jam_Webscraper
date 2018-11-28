#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int i,j,k;

#define fi(a,b) for(i=a;i<b;i++)
#define fj(a,b) for(j=a;j<b;j++)
#define fk(a,b) for(k=a;k<b;k++)
#define fr(a,b,c) for(i=a;i<b;i+=c);
#define rf(a,b,c) for(i=a;i>b;i-=c);
#define pb(a) push_back(a);

int main(){
	
	int t;
	string s;
	
	cin >> t;
	
	fi(0,t){
		cin >> s;
		
		for(int z=0;z<s.length();z++){
		
			fj(0,s.length()-1){
				if (s[j] > s[j+1]){
					
					s[j] = static_cast<char>(s[j]-1);
					fk(j+1,s.length()){
						s[k] = '9';
					}
				}
			}
			
		}
		
		bool start = false;
		
		cout << "Case #" << i+1 << ": ";
		
		fj(0,s.length()){
			if (start || s[j] != '0'){
				start = true;
				cout << s[j];
			}
		}
		
		cout << endl;
	}
	
	//cout << static_cast<char>('0'-1);
	
	return 0;
}