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
		// 이 부분에서 알고리즘 프로그램을 작성하십시오. 기본 제공된 코드를 수정 또는 삭제하고 본인이 코드를 사용하셔도 됩니다.
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

		// 이 부분에서 정답을 출력하십시오. Codeground 시스템에서는 C++에서도 printf 사용을 권장하며, cout을 사용하셔도 됩니다.
		printf("Case #%d: ", test_case);
		printf("%lld %lld\n", max, min);
		string ddd = "";
		ddd += "Case #" + to_string(test_case) + ": "+to_string(max)+" "+ to_string(min);
		outfile << ddd << endl;
	}
	outfile.close();
	return 0;   // 정상종료 시 반드시 0을 리턴해야 합니다.
}
