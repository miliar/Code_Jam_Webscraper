#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;


char sn[20];

void solve_test_case(int case_num)
{
	char* s = sn;
	scanf("%s", s);
	int l = strlen(s);

	int i = 0;
	while (i < l - 1 && s[i] <= s[i + 1])
		i++;

	if (i == l-1){
		cout << "Case #" << case_num << ": " << s << "\n";
		return ;
	}
	
	while ((i > 0 && --s[i] < s[i - 1]) || (i == 0 && --s[i] == '0'))
		if (i > 0)
			i--;

	for (int j = i+1; j < l; j++)
		s[j] = '9';

	int k = 0;
	while (s[k] <= '0')
		s = s + 1;

	cout << "Case #" << case_num << ": " << s << "\n";
}

int main()
{
//	std::ios::sync_with_stdio(false);

	int test_count;
	scanf("%d", &test_count);
	for (int t = 1; t <= test_count; t++)
		solve_test_case(t);

	return 0;
}
