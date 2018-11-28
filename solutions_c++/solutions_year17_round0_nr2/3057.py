//#define _CRT_SECURE_NO_WARNINGS
//#include <Windows.h>

#include <map>
#include <string>
#include <stdio.h>
#include <vector>
#include <sstream>
#include <stack>
#include <bitset>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <float.h>


using namespace std;


void decreaseToTidy(string& s){
	for (int i = s.size() - 1; i >= 1; i--){
		if (s[i - 1] > s[i]){
			for (int j = i; j < s.size(); j++){
				s[j] = '9';
			}
			s[i - 1] -= 1;
		}
	}
	int i = 0;
	while (i < s.size() && s[i] == '0')
		i++;

	s.erase(0, i);
}


int main(){
	/*freopen("B-large.in", "r", stdin);
	freopen("result", "w", stdout);*/
	int t;
	
	scanf("%d", &t);

	for (int i = 1; i <= t; i++){
		string n;
		cin >> n;
		decreaseToTidy(n);
		printf("Case #%d: %s\n", i, n.c_str());
	}
	
}
