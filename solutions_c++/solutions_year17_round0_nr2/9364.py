#include<stdio.h>
#include<string.h>
#include<conio.h>
#include <sstream>

bool check(int);

int main(){
	int t, k;
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		scanf("%d",&k);
		while(1){
			if (check(k)){
				printf("case #%d: %d\n", i + 1, k);
				break;
			}
			else {
				k--;
			}
		}
	}
	_getch();
}

bool check(int x){
	int prev = 10,rem;
	while (x != 0){
		rem = x % 10;
		if (rem > prev){
			return false;
		}
		prev = rem;
		x /= 10;
	}
	return true;
}

/*std::ostringstream strs;
strs << dbl;
std::string strDbl = strs.str();

int lastDigit = strDbl.at(strDbl.length() - 1) - '0';
*/