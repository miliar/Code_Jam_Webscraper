#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>
#include <limits>
#include <cstring>
#include <unordered_set>
#include <stack>
#include <iostream>
#include <unordered_set>
using namespace std;

string lessThan(string str){
	int n = str.size();
	int i = 0,index = 0;
	bool flag = false;
	while (i<n-1&&str[i] <= str[i + 1]){
		if (str[i] == str[i + 1]){
			if (!flag){
				index = i;
				flag = true;
			}
		}
		if (str[i] < str[i + 1]){
			flag = false;
		}
		i++;
	}
	if (i<n-1&&!flag){
		if (str[i] == '0')str[i] == '9';
		else str[i] = str[i] - 1;
		while (i < n){
			i++;
			str[i] = '9';
		}
	}
	if (i<n-1&&flag){
		if (str[index] == '0')str[index] == '9';
		else str[index] = str[index] - 1;
		while (index < n){
			index++;
			str[index] = '9';
		}
	}
	int k = 0;
	while (str[k] == '0')k++;
	return str.substr(k);
}

int main(){
	int T;
	cin>>T;
	int j=1;
	while(T--){
       string str;
       cin>>str;
       string res=lessThan(str);
       printf("Case #%d: ", j++);
       cout<<res<<endl;
	}
}