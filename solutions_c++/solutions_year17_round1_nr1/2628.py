#include <bits/stdc++.h>

using namespace std;

int R = 0, C =0;

void
print_val(char arr[25][25], int R, int C)
{
	int itr = 0, itr2 = 0;
	char ch;

	// first iteration
	for (itr = 0; itr < R; itr++)
	{
		for (itr2 = 0; itr2 < C; itr2++)
		{
			if (arr[itr][itr2] != '?') {
				int t_itr = itr2;
				ch = arr[itr][itr2];
				//printf("yes  %c\n",ch);
				t_itr--;

				while(arr[itr][t_itr] == '?' && t_itr >= 0) {
					arr[itr][t_itr] = ch;
					t_itr--;
				}

				t_itr = itr2;
				t_itr++;

				 while(arr[itr][t_itr] == '?' && t_itr < C ) {
                                        arr[itr][t_itr] = ch;
                                        t_itr++;
                                }
			}
		}
	}

	//second iteration
	int temp_ind = 0;
	itr2 = 0;
	int cnt = 0;
	int flag = 0;
	int flag2 = 0;
	for (itr = 0; itr < R; itr++)
	{
		while (arr[itr][0] != '?' && itr < R)
		{
			for(itr2 = 0; itr2 < C; itr2++)
                        {
                                printf("%c", arr[itr][itr2]);
                        }
			printf("\n");
			itr++;
			flag = 1;
		}

		if (itr == R)
			break;

		if (flag == 1)
			temp_ind = itr-1;

		while(arr[itr][0] == '?' && itr < R){
			itr++;
			cnt++;
		}

		if (itr < R) {
			temp_ind = itr;
			itr--;
		}			

		while(cnt > 0)
		{
			for(itr2 = 0; itr2 < C; itr2++)
			{
				printf("%c", arr[temp_ind][itr2]);
			}
			printf("\n");
			cnt--;
		}
		flag = 0;
	}
}

void _main(int TEST)
{
	int itr = 0, itr2 = 0;
	scanf("%d %d", &R, &C);
	char arr[25][25] = {'0'};
	char ele  = 0;
	string str ;
	getline(cin, str);
	
	for ( itr = 0; itr < R; itr++)
	{
		for ( itr2 = 0; itr2 < C; itr2++)
		{
			scanf("%c", &ele);
			arr[itr][itr2] = ele;
		}
		getline(cin, str);
	}

	print_val(arr, R, C);
}

int main()
{
    	freopen("A-small-attempt1.in", "r", stdin);
	//freopen("file.txt", "r", stdin);
    	freopen("A-small.out", "w", stdout);
    	int TEST;
    	scanf("%d", &TEST);
    	for(int i=1; i<=TEST; i++)
    	{
        	printf("Case #%d: \n", i);
        	_main(i);
    	}
    	return 0;
}
