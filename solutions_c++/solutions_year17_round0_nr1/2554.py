#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

char s[1001];

void solve_test_case(int case_num)
{
	int k, l, a = 0;
	scanf("%s %d", s, &k);
	l = strlen(s);

	int i = 0;
	for(int i=0; i<l; i++){
		if (s[i] == '+')
			continue;
		if (l - i < k){
			a = -1;
			break;
		}		
		
		a++;
		for (int j=0; j<k; j++)
			if (s[i + j] == '-') 
				s[i+j] = '+';
			else
				s[i+j] = '-';
	}

	if (a > -1)
		cout << "Case #" << case_num << ": " << a << "\n";
	else 
		cout << "Case #" << case_num << ": " << "IMPOSSIBLE\n";
}

int main()
{
//	std::ios::sync_with_stdio(false);

	int total_cases;
	cin >> total_cases;

	for (int t = 1; t <= total_cases; t++)
		solve_test_case(t);	

	return 0;
}
