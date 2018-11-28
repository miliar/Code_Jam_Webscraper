#include <bits/stdc++.h>

#define For(n) for (int i = 0; i < n; ++i)
#define Forv(i, n) for (int i = 0; i < n; ++i)

using namespace std;
int case_number;

inline void print_answers(int count, int result)
{
	cout << "Case #" << count << ": " << result << endl;
}
inline void print_impossible(int count)
{
	cout << "Case #" << case_number << ": IMPOSSIBLE" << endl;
}

inline void print_answers(string s)
{

	cout << s << endl;
}

inline void print_answers(int pos, string s)
{
    cout << "Case #" << case_number << ": ";
    for (int i = pos; i < s.length(); i++)
        cout << s[i];
    cout << endl;
}

bool is_correct(string s)
{
	for (int i = 0; i < s.length() - 1; i++)
	{
		if (s[i] > s[i+1]) return false;
	}
	return true;
}

void calculate(string s)
{
	int length = 0;
	int i;

	while (!is_correct(s))
	{
		if (s[s.length() - 1] > '0') s[s.length() - 1] -= 1;
		else
		{
			i = s.length() - 1;
			while(i > length && s[i] == '0')
			{
				s[i] = '9'; i--;
			}

			s[i] -= 1;
			if (i == length && s[i] == '0') length++;
		}
	}

	print_answers(length, s);
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	// freopen("input.txt", "r", stdin);

	int number_of_tests;
	cin >> number_of_tests;
	string s;

	for (case_number = 1; case_number <= number_of_tests; ++case_number)
	{
		cin >> s;
		calculate(s);
	}

	return 0;
}
