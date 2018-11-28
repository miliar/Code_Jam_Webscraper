#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
char ss[1000];
char sn[1000];
char sn1[1000];
//insert a character in the end os sn
//

//typdef long long LL;

int balanced() {
	int i = 0, j = 0;
	//LL k = 0;
//	string str1(sn);
	while (sn[i]) {
		if (sn[i + 1] == '\0') return 1;
		while (sn[i] <= sn[i + 1] && i < strlen(sn))
		{
			i++;
		}
		if (i < strlen(sn) - 1)
		{
			sn[i] = sn[i] - 1;
			i++;

			while (sn[i])
			{
				sn[i] = '9';
				i++;
			}
		}
	}
		while (sn[j] && (sn[j] <= sn[j + 1]))
			j++;
		if (j == strlen(sn) - 1) return 1;
			else 
			return balanced();
		}
	
int main() {

	FILE *stream1;
	FILE *stream2;
//	freopen("C:/Users/hardeep.singh/Desktop/Code Jam/codejam2017/input.txt", "r", stdin);
//	freopen("C:/Users/hardeep.singh/Desktop/Code Jam/codejam2017/output.txt", "w", stdout);

	freopen_s(&stream1,"C:/Users/hardeep.singh/Desktop/Code Jam/codejam2017/input.txt", "r", stdin);
	freopen_s(&stream2,"C:/Users/hardeep.singh/Desktop/Code Jam/codejam2017/output.txt", "w", stdout);

	int tt=0, j =0, num, sum = 0, rem = 0, k = 0, x1 = 0;
	string(str);
	//	int arr[10] = { 0,0,0,0,0,0,0,0,0,0 };
	scanf_s("%d", &tt);
	for (int i = 1; i <= tt; i++)
	{
		memset(ss, '\0', sizeof ss);
		memset(sn, '\0', sizeof ss);
		memset(sn1, '\0', sizeof ss);
		printf("Case #%d: ", i);
		scanf("%s", ss);
		strcpy_s(sn, ss);
		balanced();
		for (j = 0; j < strlen(sn); j++)
			if (sn[j] != '0')
				break;
		for (int k = 0; k < strlen(sn) - j; k++)
			sn1[k] = sn[k + j];
		
		printf("%s\n", sn1);
	}
}