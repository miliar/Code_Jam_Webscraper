#include <bits/stdc++.h>
using namespace std;
const char* fileIn = "problemA.txt";
const char* fileOut = "problemAOut.txt";
const bool submitting = true;
void solveCase(int caseNumber);
void printCase(int caseNumber, int answer);
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

const int MAXN = 1010;
char s[MAXN];
bool closes[MAXN];
void solveCase(int caseNumber)
{
	int k;
	scanf("%s %d", s, &k);
	for(int i = 0; i < MAXN; i++)
		closes[i] = false;
	bool open = true;
	int ans = 0;
	int n = strlen(s);
	for(int i = 0; i + k - 1 < n; i++)
	{
		bool value = s[i] == '+';
		open ^= closes[i];
		if(open != value)
		{
			open = !open;
			ans++;
			closes[i + k] = true;
		}
	}
	bool allRight = true;
	for(int i = n - k + 1; i < n; i++)
	{
		open ^= closes[i];
		bool value = s[i] == '+';
		if(open != value)
			allRight = false;
	}
	if(allRight) printCase(caseNumber, ans);
	else printCase(caseNumber, -1);
}
void printCase(int caseNumber, int answer)
{
	printf("Case #%d: ", caseNumber);
	if(answer == -1) printf("IMPOSSIBLE\n");
	else printf("%d\n", answer);
}