#include <stdio.h>
#include <algorithm>

using namespace std;

int main(void) 
{
	int test_case = 0;
	long long input_num = 0;
	long long comp_num = 0;
	char str[20];
	char str2[20];
	FILE * f;

	f = fopen("output.txt", "w");

	scanf("%d", &test_case);

	for (int t = 1; t <= test_case; t++) {
		scanf("%lld", &input_num);

		sprintf(str, "%lld", input_num);
		
		int length = 0;
		for (length = 0; str[length] != '\0'; length++);
		//printf("%d", length);

		for (int i = 0; i < length; i++) 
			str2[i] = str[0];
		str2[length] = '\0';


		int start_num = 0;
		while (1) {
			comp_num = atoll(str2);

			if (comp_num < input_num) {
				if (str2[start_num] == '9')
					break;
				for (int i = start_num; i < length; i++)
					str2[i] = str2[i] + 1;
			}

			else if (comp_num > input_num) {
				str2[start_num] = str2[start_num] - 1;
				start_num++;
			}
			else
				break;
		}
	
		comp_num = atoll(str2);
		fprintf(f,"Case #%d: %lld\n",t,comp_num);
	}

	return 0;
}