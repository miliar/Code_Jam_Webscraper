#include <iostream>
#include <cstring>

using namespace std; 

#define TRUE 1
#define FALSE 0

void bubble_down(char* array, int size);
void downnum(char *num);
void minus1(char *num_ch, int size);

int main(void) {

	int line_num;
	int size[100];
	char array[100][21];
	cin >> line_num;

	for (int i = 0; i < line_num; i++) 
	{
		cin >> array[i];
		size[i] = strlen(array[i]);
	}
	for (int i = 0; i < line_num; i++)
	{
		bubble_down(array[i], size[i]);
		if (array[i][0] == '0') 
		{
			for (int j = 0; array[i][j] != '\0'; j++)
			{
				array[i][j] = array[i][j + 1];
			}
		}

		printf("Case #%d: %s\n", i+1,array[i]);
	}

	return 0;
}

void bubble_down(char* array,int size) 
{
	int i, j;


	for (i = 0; i<size; i++) 
	{
		for (j = 0; array[j+1]!='\0'; j++) 
		{
			while (1) 
			{
				if (array[j] <= array[j + 1])
					break;
				else
					minus1(array,size-1);
			}
		}
	}
}
void downnum(char *num_ch)
{
	long double num;
	num=atoi(num_ch);
	num--;
	sprintf(num_ch, "%lf", num);

}
void minus1(char *num_ch,int size)
{
	int i;
	if (num_ch[size] == '0')
	{
		num_ch[size]='9';
		if (num_ch[size - 1] == '0') {

			for (i = 1; num_ch[size - i] == '0'; i++) {}
			num_ch[size - i]--;
			i--;
			for (; i != 0; i--)
			{
				num_ch[size - i] = '9';
			}
		

				/*
				if (num_ch[size - i] == '0')
				{
					num_ch[size - i] = '9';
					num_ch[size - i - 1]--;
				}
				else
					num_ch[size - i]--;*/

		}
		else
			num_ch[size - 1]--;
	}
	else
	{
		num_ch[size]--;
	}
	//printf("%s\n", num_ch);

}