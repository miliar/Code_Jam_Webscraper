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
	freopen("A-large.in", "r", stdin); 
	freopen("output.txt", "w", stdout);
	string str;
	int x, c = 0,t;
	bool f = true;
	cin >> t;
	for (int k = 0; k < t; k++){
		cin >> str >> x;
		for (int i = 0; i < str.size(); i++){
			if (str[i] == '-'){
				if (i + x <= str.size()){
					for (int j = 0; j < x; j++){
						if (str[i + j] == '-')
							str[i + j] = '+';
						else
							str[i + j] = '-';
					}
					c++;
				}
				else{
					f = false;
				}
			}

		}
		cout << "Case #" << k + 1 << ": ";
		if (f == true)
			cout << c << endl;
		else
			cout << "IMPOSSIBLE" << endl;
		c = 0;
		f = true;
	}

}
