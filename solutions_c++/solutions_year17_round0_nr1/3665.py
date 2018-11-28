#include<iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>
#include <iostream>

using namespace std;

int dfs(string &s, int k) {
	int n = s.length();
	int flag = -1;
	for (int i = 0; i<n; i++) {
		if (s[i] == '-') {
			flag = i;
			break;
		}
	}
	if (flag == -1) return 0;
	if (flag>n - k) return -1;
	for (int i = flag; i<flag + k; i++) {
		s[i]=(s[i] == '-'? s[i] = '+': s[i] = '-') ;
	}
	int res = dfs(s, k);
	if (res == -1) return -1;
	return res + 1;
}

int main() {
	int n;
    //ofstream file;
	//file.open("1.out");
	scanf("%d", &n);
	string casepancake;
	int casek;
	for (int i = 0; i<n; i++) {
		cin >> casepancake>>casek;
        int res = dfs(casepancake, casek);
		cout<<"Case #"<<i+1<<": ";
		if (res == -1) cout<<"IMPOSSIBLE"<<endl;
			else cout<<res<<endl;
	}
    return 0;
}
