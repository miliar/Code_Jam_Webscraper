#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;
typedef unsigned long long LL;
const int MAXN = 100010;

struct bign{
	int d[40];
	int len;
	bign(){
		memset(d, 0, sizeof(d));
		len = 0;
	}
};

bign change(string str){
	bign a;
	a.len = str.size();
	for(int i = 0; i < a.len; i++){
		a.d[i] = str[a.len - 1 - i] - '0';
	}
	return a;
}

int compare(bign a, bign b){
	if(a.len > b.len) return 1;
	else if(a.len < b.len) return -1;
	else{
		for(int i = a.len - 1; i >= 0; i--){
			if(a.d[i] > b.d[i]) return 1;
			else if(a.d[i] < b.d[i]) return -1;
		}
		return 0;
	}
}

bign sub(bign a, bign b){
	bign c;
	for(int i = 0; i < a.len || i < b.len; i++){
		if(a.d[i] < b.d[i]){
			a.d[i + 1]--;
			a.d[i] += 10;
		}
		c.d[c.len++] = a.d[i] - b.d[i];
	}
	while(c.len - 1 >= 1 && c.d[c.len - 1] == 0){
		c.len--;
	}
	return c;
}

bool check(bign num){
	for(int i = num.len - 1; i >=0; i--){
		for(int j = i - 1; j >= 0; j--){
			if(num.d[i] > num.d[j]) return false;
		}
	}
	return true;
}

void print(bign a){
	for(int i = a.len - 1; i >= 0; i--){
		cout << a.d[i];
	}
}

int main(){
	int t;
	string str;
	string base = "1";
	//string s1;
	//string s2;
	//cin >> s1 >> s2;
	//print(sub(change(s1), change(s2)));
	while(cin >> t){
		for(int i = 1; i <= t; i++){
			cin >> str;
			cout << "Case #" << i << ": ";
			bign num = change(str);
			//print(num);
			//cout << endl;
			//print(sub(num, change(base)));
			while(compare(num, change(base)) > 0){
				//cout << "num: ";
				//print(num);
				//cout << endl;
				if(check(num)){
					print(num);
					cout << endl;
					break;
				}
				num = sub(num, change(base));
			}
			//for(num = (bign)change(str); compare(num, change(base)) > 0; num = sub(num, change(base))){
			//	if(check(num)){
			//		print(num);
			//	}
			//}
		}
	}
	return 0;
}














/*
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;
typedef unsigned long long LL;
const int MAXN = 100010;

struct bign{
	int d[40];
	int len;
	bign(){
		memset(d, 0, sizeof(d));
		len = 0;
	}
};

bign change(string str){
	bign a;
	a.len = str.size();
	for(int i = 0; i < a.len; i++){
		a.d[i] = str[a.len - 1 - i] - '0';
	}
	return a;
}

int compare(bign a, bign b){
	if(a.len > b.len) return 1;
	else if(a.len < b.len) return -1;
	else{
		for(int i = a.len - 1; i >= 0; i--){
			if(a.d[i] > b.d[i]) return 1;
			else if(a.d[i] < b.d[i]) return -1;
		}
		return 0;
	}
}

bign sub(bign a, bign b){
	bign c;
	for(int i = 0; i < a.len || i < b.len; i++){
		if(a.d[i] < b.d[i]){
			a.d[i + 1]--;
			a.d[i] += 10;
		}
		c.d[c.len++] = a.d[i] - b.d[i];
	}
	while(c.len - 1 >= 1 && c.d[c.len - 1] == 0){
		c.len--;
	}
	return c;
}

bool check(bign num){
	for(int i = num.len - 1; i > 0; i--){
		if(num.d[i] < num.d[i - 1]) return false;
	}
	return true;
}

void print(bign a){
	for(int i = a.len - 1; i >= 0; i--){
		cout << a.d[i];
	}
}

bool checkNum(LL num){
	int index = 0;
	int seq[20] = {-1};
	do{
		seq[index++] = num % 10;
		num /= 10;
	}while(num != 0);
	//for(int i = index - 1; i >= 0; i--){
	//	cout << seq[i];
	//}
	cout << endl;
	for(int i = 0; i < index ; i++){
		for(int j = i; j < index; j++){
			if(seq[i] > seq[j]) return false;
		}
	}
	return true;
}

int main(){
	int t;
	string str;
	string base = "1";
	//string s1;
	//string s2;
	//cin >> s1 >> s2;
	//print(sub(change(s1), change(s2)));
	while(cin >> t){
		for(int i = 1; i <= t; i++){
			LL num;
			cin >> num;
			cout << "Case #" << i << ": ";
			for(LL j = num; j > 1; j--){
				if(checkNum(j)){
					cout << j << endl;
				}
				break;
			}
		//	cout << endl;
		}
	}
	return 0;
}
*/



