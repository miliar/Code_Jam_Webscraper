#include <cstdio>
#include <iostream>
#include<string>
#include<fstream>
using namespace std;

int main(int argc, char** argv)
{
	freopen("C-small-2-attempt0.in", "r", stdin);
	//freopen("inputc.txt", "r", stdin);
	ofstream outfile("outputc.txt");
	setbuf(stdout, NULL);

	int T;
	int test_case;
	long long int n, k,min,max;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; test_case++) {
		// �� �κп��� �˰��� ���α׷��� �ۼ��Ͻʽÿ�. �⺻ ������ �ڵ带 ���� �Ǵ� �����ϰ� ������ �ڵ带 ����ϼŵ� �˴ϴ�.
		scanf("%lld %lld", &n, &k);
		min = 0; max = 0;
		while(1)
		{
			if (k == 1)
			{
				if (n % 2 == 0)
				{
					max = n / 2;
					min = n / 2 - 1;
				}
				else
				{
					max = n / 2;
					min = n / 2;
				}
				break;
			}
			else
			{	
				int t=n, p=k;
				n = n / 2;
				k = k / 2;
				if (t % 2 == 0 && p % 2 == 1)
				{
					n--;
				}
			
			}
		}

		// �� �κп��� ������ ����Ͻʽÿ�. Codeground �ý��ۿ����� C++������ printf ����� �����ϸ�, cout�� ����ϼŵ� �˴ϴ�.
		printf("Case #%d: ", test_case);
		printf("%lld %lld\n", max, min);
		string ddd = "";
		ddd += "Case #" + to_string(test_case) + ": "+to_string(max)+" "+ to_string(min);
		outfile << ddd << endl;
	}
	outfile.close();
	return 0;   // �������� �� �ݵ�� 0�� �����ؾ� �մϴ�.
}
