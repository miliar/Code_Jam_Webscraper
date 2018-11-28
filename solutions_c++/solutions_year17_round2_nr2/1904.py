#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

typedef long long ll;
#define INF 2000000000
#define MOD 1000000007
#define endl '\n'

string check(string str,int pos,char ch){
	int l=((pos==0)?str.length()-1:(pos-1)),r=((pos==str.length()-1)?0:(pos+1)),i;
	string cpu = str;
	bool flag = false;
	switch(ch){
		case 'R':
			if(str[l] == 'R' || str[r] == 'R' || str[l] == 'O' || str[r] == 'O' || str[l] == 'V' || str[r] == 'V'){
				flag = true;
			}
			break;
		case 'O':
			if(str[l] == 'O' || str[r] == 'O' || str[l] == 'R' || str[r] == 'R' || str[l] == 'Y' || str[r] == 'Y'){
				flag = true;
			}
			break;
		case 'Y':
			if(str[l] == 'Y' || str[r] == 'Y' || str[l] == 'O' || str[r] == 'O' || str[l] == 'G' || str[r] == 'G'){
				flag = true;
			}
			break;
		case 'G':
			if(str[l] == 'G' || str[r] == 'G' || str[l] == 'Y' || str[r] == 'Y' || str[l] == 'B' || str[r] == 'B'){
				flag = true;
			}
			break;
		case 'B':
			if(str[l] == 'B' || str[r] == 'B' || str[l] == 'G' || str[r] == 'G' || str[l] == 'V' || str[r] == 'V'){
				flag = true;
			}
			break;
		case 'V':
			if(str[l] == 'V' || str[r] == 'V' || str[l] == 'R' || str[r] == 'R' || str[l] == 'B' || str[r] == 'B'){
				flag = true;
			}
	}
	//cout << "flag " << l << str[l] << r << str[r] << flag << ch << endl;
	if(flag){
		if(pos == 0)return cpu;
		bool flag = false;
		//cout << "before erase" << str << endl;
		str.erase(str.begin()+pos);
		//cout << "after erase" << str << endl;
		for(i=0;i<pos;++i){
			str.insert(str.begin()+i,ch);
			//cout << "after insert" << str << endl;
			int l=((i==0)?str.length()-1:(i-1)),r=((i==str.length()-1)?0:(i+1));
			flag = false;
			switch(str[i]){
				case 'R':
					if(str[l] == 'R' || str[r] == 'R' || str[l] == 'O' || str[r] == 'O' || str[l] == 'V' || str[r] == 'V'){
						flag = true;
					}
					break;
				case 'O':
					if(str[l] == 'O' || str[r] == 'O' || str[l] == 'R' || str[r] == 'R' || str[l] == 'Y' || str[r] == 'Y'){
						flag = true;
					}
					break;
				case 'Y':
					if(str[l] == 'Y' || str[r] == 'Y' || str[l] == 'O' || str[r] == 'O' || str[l] == 'G' || str[r] == 'G'){
						flag = true;
					}
					break;
				case 'G':
					if(str[l] == 'G' || str[r] == 'G' || str[l] == 'Y' || str[r] == 'Y' || str[l] == 'B' || str[r] == 'B'){
						flag = true;
					}
					break;
				case 'B':
					if(str[l] == 'B' || str[r] == 'B' || str[l] == 'G' || str[r] == 'G' || str[l] == 'V' || str[r] == 'V'){
						flag = true;
					}
					break;
				case 'V':
					if(str[l] == 'V' || str[r] == 'V' || str[l] == 'R' || str[r] == 'R' || str[l] == 'B' || str[r] == 'B'){
						flag = true;
					}
			}
			//cout << i << str << flag << endl;
			if(flag == false)break;
			else{
				str.erase(str.begin()+i);
			}
		}
		if(flag == true){
			return cpu;
		}
	}
	return str;
}


int main(){
	ios::sync_with_stdio(false);
	int t,tc,n,r,o,y,g,b,v,i;
	cin >> t;
	tc = t;
	while(tc--){
		cout << "Case #" << t-tc << ": ";
		cin >> n;
		cin >> r >> o >> y >> g >> b >> v;
		string str;
		str.resize(n);
		i = -1;
		while(n){
			
			if(r >= 1){
				--r;
				--n;
				str[++i] = 'R';
				//check(str,i,'R');
			}
			if(y >= 1){
				--y;
				--n;
				str[++i] = 'Y';
				//check(str,i,'Y');
			}
			if(b >= 1){
				--b;
				--n;
				str[++i] = 'B';
				//check(str,i,'B');
			}
			if(o >= 1){
				--n;
				--o;
				str[++i] = 'O';
				//check(str,i,'O');
			}
			if(v >= 1){
				--n;
				--v;
				str[++i] = 'V';
				//check(str,i,'V');
			}
			if(g >= 1){
				--n;
				--g;
				str[++i] = 'G';
				//check(str,i,'G');
			}
			//cout << str << endl;
		}
		//cout << "Original " << str << endl;
		for(i=str.length()-1;i>=0;--i){
			string cpu = check(str,i,str[i]);
			if(cpu != str){
				str = cpu;
				++i;
			}
			//cout << str << endl;
		}
		for(i=0;i<str.length();++i){
			int l=((i==0)?str.length()-1:i-1),r=((i==str.length()-1)?0:i+1);
			bool flag = false;
			switch(str[i]){
				case 'R':
					if(str[l] == 'R' || str[r] == 'R' || str[l] == 'O' || str[r] == 'O' || str[l] == 'V' || str[r] == 'V'){
						flag = true;
					}
					break;
				case 'O':
					if(str[l] == 'O' || str[r] == 'O' || str[l] == 'R' || str[r] == 'R' || str[l] == 'Y' || str[r] == 'Y'){
						flag = true;
					}
					break;
				case 'Y':
					if(str[l] == 'Y' || str[r] == 'Y' || str[l] == 'O' || str[r] == 'O' || str[l] == 'G' || str[r] == 'G'){
						flag = true;
					}
					break;
				case 'G':
					if(str[l] == 'G' || str[r] == 'G' || str[l] == 'Y' || str[r] == 'Y' || str[l] == 'B' || str[r] == 'B'){
						flag = true;
					}
					break;
				case 'B':
					if(str[l] == 'B' || str[r] == 'B' || str[l] == 'G' || str[r] == 'G' || str[l] == 'V' || str[r] == 'V'){
						flag = true;
					}
					break;
				case 'V':
					if(str[l] == 'V' || str[r] == 'V' || str[l] == 'R' || str[r] == 'R' || str[l] == 'B' || str[r] == 'B'){
						flag = true;
					}
			}
			if(flag == true){
				str = "IMPOSSIBLE";
				break;
			}
		}
		cout << str << endl;
	}
	return 0;
}

