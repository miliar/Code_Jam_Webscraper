#include <cstdio>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

// bool check(int n) {
//     vector<int> v;
//     while(n) {
// 	v.push_back(n%10);
// 	n /= 10;
//     }
//     for (int i = 0; i < v.size()-1; i++) {
// 	if (v[i] < v[i+1]) return false;
//     }
//     return true;
// }
// int find(int n) {
//     for (int i = n; i > 0; i--) {
// 	if (check(i)) return i;
//     }
//     return -1;
// }


bool check(string n) {
    int len = n.length();
    for (int i = 0; i+1 < len; i++) {
	if (n[i] > n[i+1]) return false;
    }
    return true;
}

int main() {
    int TC;

    cin >> TC;
    for(int tc = 1; tc <= TC; tc++) {
	string n;
	cin >> n;
	while(!check(n)) {
	    int len = n.length();
	    for (int i = 0; i+1 < len; i++) {
		if (n[i] > n[i+1]) {
		    n[i] = '0' + ((n[i]-'0')-1);
		    for (int j = i+1; j < len; j++) n[j] = '9';
		    if (i == 0 && n[i] == '0')  n = n.substr(1);
		    break;
		}
	    }
	}
	printf("Case #%d: %s\n", tc, n.c_str());
    }

    return 0;
}
