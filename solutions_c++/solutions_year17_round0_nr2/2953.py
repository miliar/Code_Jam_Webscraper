#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 5;

#define st first
#define nd second
#define make(a,b) make_pair(a,b)

typedef pair<int,int> pun;
typedef long long ll;

ll newt[100][100];

string test() {
	string number;
	cin >> number;
	bool change = true;
	while(change) {
		change = false;
		for (int i = 0; i + 1 < number.size(); i ++) {
			if (number[i] > number[i + 1]) {
				number[i] --;
				change = true;
				for (int j = i + 1; j < number.size(); j ++) {
					number[j] = '9';
				}
			}
		}
	}
	bool wypisz = false;
	string res;
	for (int i = 0; i < number.size(); i ++) {
		if (number[i] > '0' || i == number.size() - 1) wypisz = true;
		if (wypisz) res += number[i];
	}
	return res;
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++) {
		cout << "Case #" << i <<": " << test() << "\n";
	}
}
