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
		// �� �κп��� �˰��� ���α׷��� �ۼ��Ͻʽÿ�. �⺻ ������ �ڵ带 ���� �Ǵ� �����ϰ� ������ �ڵ带 ����ϼŵ� �˴ϴ�.
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

		// �� �κп��� ������ ����Ͻʽÿ�. Codeground �ý��ۿ����� C++������ printf ����� �����ϸ�, cout�� ����ϼŵ� �˴ϴ�.
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
	return 0;   // �������� �� �ݵ�� 0�� �����ؾ� �մϴ�.
}