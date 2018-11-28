#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void func(int i, int *num, int len)
{
	if (i == len)return;

	if (num[i] >= num[i - 1])
	{
		func(i + 1, num, len);
	}
	else
	{
		if (num[i - 1] > 0)
		{
			num[i - 1]--;
			for (int j = i; j < len; j++)
				num[j] = 9;
			func(i - 1, num, len);
		}
		else
		{
			func(i - 1, num, len);
		}
	}
}

int main()
{
	ifstream in("B-large.in");
	string s;

	if (in.is_open()) {
		// ��ġ �����ڸ� ���� ������ �ű��.
		in.seekg(0, ios::end);

		// �׸��� �� ��ġ�� �д´�. (������ ũ��)
		int size = in.tellg();

		// �� ũ���� ���ڿ��� �Ҵ��Ѵ�.
		s.resize(size);

		// ��ġ �����ڸ� �ٽ� ���� �� ������ �ű��.
		in.seekg(0, ios::beg);
	}
	else
	{
		printf("Not File\n");
	}

	int T;
	//scanf("%d", &T);
	in >> T;

	for (int Case = 1; Case <= T; Case++)
	{
		char N[20];
		int num[20];

		//scanf("%s", N);
		in >> N;

		for (int i = 0; i < strlen(N); i++)
			num[i] = N[i] - 48;

		func(1, num, strlen(N));

		printf("Case #%d: ",Case);

		bool chk = 0;
		for (int i = 0; i < strlen(N); i++)
		{
			if (num[i] > 0)chk = 1;
			if (chk)	printf("%d", num[i]);
		}
		printf("\n");
	}
	return 0;
}