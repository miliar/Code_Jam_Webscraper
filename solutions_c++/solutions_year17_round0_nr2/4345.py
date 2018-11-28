#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>
#include<unordered_map>
#include<set>
#include<unordered_set>
#include<cstring>
#include<queue>
#include<deque>
#include<stack>
#include<algorithm>
#include<climits>
#include<string>
#include<sstream>
#include<cmath>
#include<cctype>
#include<iomanip>
#include<list>
#include<conio.h>

using namespace std;

typedef pair <int, int> PII;
typedef pair <int, double> PID;
typedef pair <double, double> PDD;
typedef vector <int> VI;
typedef vector <double> VD;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define MP make_pair
#define PB push_back
#define PPB pop_back
#define PF push_front
#define PPF pop_front
#define EL endl
#define CO cout

bool isTidy(string x){
	if(x.size() == 0) return false; //No string input
	for(int i = 1;i < x.size();i++){
		if(x[i - 1] > x[i]) return false;
	}
	return true;
}

void solve(){
	string str;
	cin >> str;
	while(true){
		if(isTidy(str)){
			cout << str <<endl;
			return;
		}else{  //Not Tidy   *** i.e. len(str) >= 2
			int index = 0;
			for(int i = 1;i < str.size();i++){
				if(str[i] < str[i-1]){
					index = i - 1;
					break;
				}
			}
			str[index]--;
			if((index == 0) && (str[index] == '0')){
				for(int i = 0;i < str.size() - 1;i++){
					cout << '9';
				}
				cout << endl;
				return;
			}else{
				for(int i = index + 1;i < str.size();i++){
					str[i] = '9';
				}
			}	
		}
	}
}

int main() {
   	freopen("a.in","r",stdin);
   	freopen("a.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
        solve();
	}
	getch();
	return 0;
}
