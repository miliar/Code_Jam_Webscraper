#include <cstdio>
#include <iostream>
#include<string>
#include<fstream>
using namespace std;

int main(int argc, char** argv)
{
	freopen("A-large.in", "r", stdin);
	ofstream outfile("outputa.txt");
	setbuf(stdout, NULL);

	int T;
	int test_case;

	scanf("%d", &T);
	for (test_case = 1; test_case <= T; test_case++) {
		// 이 부분에서 알고리즘 프로그램을 작성하십시오. 기본 제공된 코드를 수정 또는 삭제하고 본인이 코드를 사용하셔도 됩니다.
		char c[1002];
		int k;
		int count = 0;
		scanf("%s %d", c, &k);
		for (int i = 0; i < strlen(c) - k + 1; i++)
		{
			if (c[i] == '-')
			{
				count++;
				int t = i + k;
				for (int j = i; j < t; j++)
				{
					if (c[j] == '+')
						c[j] = '-';
					else
						c[j] = '+';
				}
			}
		}
		string p = "";

		// 이 부분에서 정답을 출력하십시오. Codeground 시스템에서는 C++에서도 printf 사용을 권장하며, cout을 사용하셔도 됩니다.
		printf("Case #%d\n", test_case);
		p += "Case #" + to_string(test_case)+": ";
		int flag = 0;
		for (int i = strlen(c); i > strlen(c) - k; i--)
		{
			if (c[i] == '-')
			{
				
				flag = 1;
			}
		}
		if (flag == 0)
		{
			printf("%d\n", count);
			p += to_string(count);
		}
		else
		{
			printf("IMPOSSIBLE\n");
			p += "IMPOSSIBLE";
		}
		outfile << p << endl;
	}
	outfile.close();
	return 0;   // 정상종료 시 반드시 0을 리턴해야 합니다.
}