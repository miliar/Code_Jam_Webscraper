#include <cstdio>
#include <iostream>
#include<fstream>
#include<string>
using namespace std;

int main(int argc, char** argv)
{
	freopen("B-large.in", "r", stdin);
	ofstream outfile("output.txt");

	setbuf(stdout, NULL);

	int T;
	int test_case;
	long long int num;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; test_case++) {
		// �� �κп��� �˰��� ���α׷��� �ۼ��Ͻʽÿ�. �⺻ ������ �ڵ带 ���� �Ǵ� �����ϰ� ������ �ڵ带 ����ϼŵ� �˴ϴ�.
		scanf("%lld", &num);
		int baeyeol[20];
		for (int i = 0; i < 20; i++)
			baeyeol[i] = -1;
		string str = to_string(num);
		string p="";
		for (int i = 0; i < str.length(); i++)
		{//string to int*
			baeyeol[i] = str.at(i)-'0';
		}
		int flag;
		while (true)
		{
			flag = 1;
			for (int i = 0; i < str.length() - 1; i++)
			{
				if (baeyeol[i] > baeyeol[i + 1])
				{
					flag = 0;
					baeyeol[i] -= 1;
					for (int j = i + 1; j < str.length(); j++)
						baeyeol[j] = 9;
				}
			}
			if (flag == 1)
				break;
		}
		// �� �κп��� ������ ����Ͻʽÿ�. Codeground �ý��ۿ����� C++������ printf ����� �����ϸ�, cout�� ����ϼŵ� �˴ϴ�.
		printf("Case #%d\n", test_case);
		p += "Case #" + to_string(test_case) + ": ";
		for (int i = 0; baeyeol[i]!=-1; i++)
		{
			if (i == 0 && baeyeol[i] == 0)
				continue;
			p += to_string(baeyeol[i]);
			printf("%d", baeyeol[i]);
		}
		printf("\n");
		outfile << p<<endl;
	}
	outfile.close();
	return 0;	// �������� �� �ݵ�� 0�� �����ؾ� �մϴ�.
}
