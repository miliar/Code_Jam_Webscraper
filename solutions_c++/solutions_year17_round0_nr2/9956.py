#include <bits/stdc++.h>
#define ll long long 
using namespace std;
 
int main( ) {
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   ll n, num;
   cin >> n;
   for(int i=1; i<=n; i++){
   		cin >> num;
   		cout << "Case #" << i << ": ";
   		int flag = 0;
		while(! flag){
   			stringstream ss;
			ss << num;
			string s = ss.str();
			flag = 1;
			for(int j=s.size()-1; j>0; j--){
				if(s[j] < s[j-1]){
					flag = 0;
					break;
				}
			}
			if(! flag)
				num--;
			else
				cout << num << endl;	
		}
   		
   }
   
   return 0;
}
