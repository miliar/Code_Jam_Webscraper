#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream in("C-small-2-attempt0.in");
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
	in >> T;

	for (int Case = 1; Case <= T; Case++)
	{
		int K, N;
		in >> N >> K;

		int *num = new int[N + 1];
		for (int i = 0; i <= N; i++)
			num[i] = 0;

		num[N] = 1;

		int cnt = 1;
		for (int i = N; i >= -1; i--)
		{
			if (num[i])
			{
				if (cnt == K)
				{
					if (i % 2)
						printf("Case #%d: %d %d\n",Case, i / 2, i / 2);
					else
					{
						printf("Case #%d: %d %d\n",Case, i / 2, i / 2 - 1);
					}
					break;
				}

				num[i]--;
				cnt++;
				if (i % 2)
					num[i / 2] += 2;
				else
				{
					num[i / 2]++;
					num[i / 2 - 1]++;
				}
				i++;
			}
		}
	}
	return 0;
}