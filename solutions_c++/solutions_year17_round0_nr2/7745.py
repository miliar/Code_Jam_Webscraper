#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>

bool IsTidy(const std::string &str)
{
	for (size_t k = 1; k != str.size(); k++){
		if (str[k -1] > str[k])
			return false;
	}
	return true;
}

std::string ToString(long long N){
	std::string str;
	if (N == 0) {
		str = "0";
		return str;
	}
	while(N){
		str.push_back('0'+(N%10));
		N = N/10;
	}
	std::reverse(str.begin(), str.end());
	return str;
}

long long StrToLL(const std::string &str)
{
	long long N = 0;
	size_t k = 0;
	for (; k != str.size(); k++){
		N = N*10 + (str[k]-'0');
	}
	return N;
}
void solve(int caseNo)
{
	long long N;

	std::cin>> N;
	std::string str = ToString(N);

	int j = str.size()-1;
	while(!IsTidy(str) && j > 0){
		str[j] = '9';
		j--;
		while(str[j] == '0'){
			str[j] = '9';
			j--;
		}
		str[j]--;
	}


	long long tidyN = StrToLL(str);
	
	if (caseNo != 1)
		printf("\n");
	printf("Case #%d: ", caseNo);
	std::cout << tidyN;
}

int main()
{
	int numOfTestCases, i;
	scanf("%d", &numOfTestCases);
	for (i = 0; i < numOfTestCases; i++){
		solve(i+1);
	}
}
