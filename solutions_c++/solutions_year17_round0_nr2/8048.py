#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<string.h>
#include<sstream>
#include<iomanip>
#include<cmath>
#include<set>
#include<cctype>
#include<bitset>
#include<map>
#include<queue>
using namespace std;

#define lp(i,n)        for(int i=0;i<n;i++)
#define veci				vector<int>
#define vecl				vector<long long>

typedef long long         ll;
typedef long double         ld;
int main()
{
	freopen("B-large.in", "r", stdin); 
	freopen("output.txt", "w", stdout);
	int t;
	string str;
	cin >> t;
	for (int i = 0; i < t; i++){
		cin >> str;
		for (int j = 1; j < str.size(); j++){
			if (str[j] < str[j - 1]){
				for (int k = j; k < str.size(); k++){
					str[k] = '9';
				}
				str[j - 1]--;
				if (j>1)
					j-=2;
			}
		}
		cout << "Case #" << i+1 << ": ";
		for (int j = 0; j < str.size(); j++){
			if (str[j] != '0')
				cout << str[j];
		}
		cout << endl;
		
	}

}
