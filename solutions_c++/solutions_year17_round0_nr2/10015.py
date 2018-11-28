#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int T;
long long N;
char num[20];
string number;
vector<long long> ans;

long long getnum(long long no) {
	number = to_string(no);	
	int len = number.length();
	int l_index=len-1;
	int index;
	long long sum = 0;
	for (int i = 0; i < len -1; i++) {

			if (number[l_index - i] < number[l_index - i - 1]) {
				index = l_index - i;
				if (number[index - 1] != 0)
					number[index - 1] = number[index - 1] - 1;
				else
					number[index - 1] = '9';
				for (int j = 0; j < i+1; j++)
					number[index + j] = '9';
			}
	}
	strcpy(num, number.c_str());

	//printf("%s\n", num);

	//for (int i = 0; i < len; i++) {


	//}
	long long ret;
	sscanf(num, "%lld", &ret);

	return ret;




}

int main(void) {

	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		long long num=0;
		scanf("%lld", &num);
		ans.push_back(getnum(num));
	}

	for (int i = 0; i < ans.size(); i++) {
		printf("Case #%d: %lld\n",i+1, ans[i]);
	}


	return 0;
}