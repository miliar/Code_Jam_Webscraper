#include <cstdio>
#include <map>

using namespace std;

int main() {
	char buf[1024];
	int T;
	int i, j, k;

	memset(buf, 0x00, sizeof(buf));
	fgets(buf, 1024, stdin);

	sscanf(buf, "%d", &T);

	for (i = 0; i < T; ++i) {
		memset(buf, 0x00, sizeof(buf));
		fgets(buf, 1024, stdin);

		_int64 K, N;

		sscanf(buf, "%I64d %I64d", &N, &K);

		map<_int64, _int64> lengths;
		lengths.insert(make_pair(N, 1i64));

		_int64 res = -1;
		_int64 ended = 0;
		while (res < 0) {
			map<_int64,_int64>::iterator i1 = lengths.end();
			--i1;

			if (ended + i1->second >= K) {
				//printf("end: %I64d %I64d %I64d\n", ended, i1->second, K);
				res = i1->first;
				break;
			}

			_int64 newlen1;
			_int64 newlen2;

			if (i1->first % 2 == 0) {
				newlen1 = i1->first / 2;
				newlen2 = i1->first / 2 - 1;
			} else {
				newlen1 = i1->first / 2;
				newlen2 = newlen1;
			}

			_int64 val = i1->second;

			//printf("%I64d -> %I64d %I64d %I64\n", i1->first, newlen1, newlen2, val);

			lengths.erase(i1);

			lengths[newlen1] += val;
			lengths[newlen2] += val;

			ended += val;
		}

		if (res % 2 == 0)
			printf("Case #%d: %I64d %I64d\n", i + 1, res / 2, res / 2 - 1);
		else
			printf("Case #%d: %I64d %I64d\n", i + 1, res / 2, res / 2);
	}

	return 0;
}