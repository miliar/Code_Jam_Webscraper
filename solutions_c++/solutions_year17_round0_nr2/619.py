#include <bits/stdc++.h>
using namespace std;
const char* fileIn = "problemB.txt";
const char* fileOut = "problemBOut.txt";
const bool submitting = true;
void solveCase(int caseNumber);
void printCase(int caseNumber, vector<int> answer);
int main()
{
	if(submitting)
	{
		freopen(fileIn, "r", stdin);
		freopen(fileOut, "w", stdout);
	}
	int t;
	scanf("%d", &t);
	for(int caseNumber = 1; caseNumber <= t; caseNumber++)
		solveCase(caseNumber);
	return 0;
}

typedef long long ll;
void solveCase(int caseNumber)
{
	ll n;
	scanf("%lld", &n);
	vector<int> digits;
	while(n)
	{
		digits.push_back(n % 10);
		n /= 10;
	}
	reverse(digits.begin(), digits.end());
	int position = -1;
	for(int i = 0; i < digits.size() - 1; i++)
	{
		if(digits[i] > digits[i + 1])
		{
			position = i;
			break;
		}
	}
	if(position != -1)
	{
		for(int i = position + 1; i < digits.size(); i++) digits[i] = 9;
		digits[position]--;
		for(int i = position; i >= 1; i--)
		{
			if(digits[i] < digits[i - 1])
			{
				digits[i] = 9;
				digits[i - 1]--;
			}
			else break;
		}
	}
	printCase(caseNumber, digits);
}
void printCase(int caseNumber, vector<int> answer)
{
	printf("Case #%d: ", caseNumber);
	for(int i = 0; i < answer.size(); i++)
		if(answer[i] != 0) printf("%d", answer[i]);
	printf("\n");
}