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
		// 위치 지정자를 파일 끝으로 옮긴다.
		in.seekg(0, ios::end);

		// 그리고 그 위치를 읽는다. (파일의 크기)
		int size = in.tellg();

		// 그 크기의 문자열을 할당한다.
		s.resize(size);

		// 위치 지정자를 다시 파일 맨 앞으로 옮긴다.
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