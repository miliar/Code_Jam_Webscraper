#include "stdio.h"

int main()
{
	int t;
	scanf("%d", &t);
	for (int tc = 0; tc < t; tc++)
	{
		printf("Case #%d: ", tc+1);
		char cstring[20] = { 0 };
		scanf("%s", cstring);

		char output[20] = { 0 };
		char before = '0';
		int length = 0;
		bool AutoNine = false;
		while (cstring[length])
		{
			if (AutoNine == false)
			{
				if (before <= cstring[length])
				{
					output[length] = cstring[length];
				}
				else
				{
					output[length] = cstring[length];

					for (int j = length; j > 0; j--)
					{
						if (output[j-1] <= output[j])
							break;
						output[j-1]--;
						output[j] = '9';
					}
					AutoNine = true;
				}
			}
			if (AutoNine == true)
			{
				output[length] = '9';
			}
			before = output[length];
			length++;
		}
		bool isOn = false;
		for (int i = 0; i < length; i++)
		{
			if (output[i] != '0')
				isOn = true;
			if (isOn)
				printf("%c", output[i]);
		}
		printf("\n");
	}
	
}