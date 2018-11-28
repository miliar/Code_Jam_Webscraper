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
		// 이 부분에서 알고리즘 프로그램을 작성하십시오. 기본 제공된 코드를 수정 또는 삭제하고 본인이 코드를 사용하셔도 됩니다.
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
		// 이 부분에서 정답을 출력하십시오. Codeground 시스템에서는 C++에서도 printf 사용을 권장하며, cout을 사용하셔도 됩니다.
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
	return 0;	// 정상종료 시 반드시 0을 리턴해야 합니다.
}
