#include<stdio.h>
#include<string.h>
using namespace std;

int main(void) {
	int T; //1~100
	char S[1003]; //2~1000
	int K; //2~S

	int i, j, j2;
	int Slen;
	int res = 0;
	int minus;
	int minushere;
	bool flag;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &T);
	for (i = 1; i <= T; i++)
	{
		//fgets(S, sizeof(S), stdin);
		scanf("%s", S);
		scanf("%d", &K);
		Slen = strlen(S);
		res = 0;
		flag = true;


		//printf("K=%d, %d�� ����, res=%d, flag=%d\n", K, Slen, res, flag);
		for (j = 0; j < Slen && flag; j++)
		{
			if (S[j] == '+');
			else//S[j]=='-'���
			{
				minus = 1;
				minushere = j;//j���� ī��Ʈ�� �Ѵ�
				while (minus < K && flag)
				{
					if (S[minushere + 1] == '-') {
						minus++;
						minushere++;
					}
					else//S[minushere+1]�� '+'���
					{
						//������ �� ���� ���
						if (minushere + K >= Slen)
						{
							flag = false; break;
						}
						//������ �� �ִ� ��� �����´�
						res++;
						for (j2 = minushere + 1; j2 <= minushere + K; j2++)
						{
							if (S[j2] == '-') S[j2] = '+';
							else S[j2] = '-';
						}
					}
				}
				if (!flag) break;
				res++;
				for (j2 = j; j2 < j + K; j2++)//�����´�
				{
					if (S[j2] == '-') S[j2] = '+';
					else S[j2] = '-';
				}
				j = j2 - 1;

			}
		}
		if (flag) printf("Case #%d: %d\n", i, res);
		else printf("Case #%d: IMPOSSIBLE\n", i);
	}
}