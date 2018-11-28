#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct SChunk
{
	long long start;
	long long end;

	long long Size() const { return end - start + 1; }
};

long long SelectPos(const SChunk& base, SChunk& left, SChunk& right)
{
	long long baseChunkSize = base.Size();

	long long selectPos = baseChunkSize / 2 + (baseChunkSize % 2);

	left.start = base.start;
	left.end = base.start + selectPos - 2;

	right.start = base.start + selectPos;
	right.end = base.end;

	return base.start + selectPos - 1;
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	long long T;
	in >> T;

	for (long long t = 0; t < T; ++t)
	{
		long long N, K;
		in >> N >> K;

		out << "Case #" << t + 1 << ": ";

		long long level = 0;
		long long levelSize = pow(2, level);
		long long chunkBigSize = N;
		long long chunkSmallSize = N;

		long long evenCount = (N + 1) % 2 ;
		long long oddCount = N % 2;
		long long curIndex = K;

		while (true)
		{
			if (curIndex <= levelSize)
			{
				if (chunkBigSize % 2 == 0) // even are bigger
				{
					if (curIndex <= evenCount) // selectEven (big)
					{
						out << chunkBigSize / 2 << " " << chunkBigSize / 2 - 1 << endl;
						break;
					}
					else // selectOdd (small)
					{
						out << chunkSmallSize / 2 << " " << chunkSmallSize / 2 << endl;
						break;
					}
				}
				else // odd are bigger
				{
					if (curIndex <= oddCount) // selectOdd (big)
					{
						out << chunkBigSize / 2 << " " << chunkBigSize / 2 << endl;
						break;
					}
					else // selectEven (small)
					{
						out << chunkSmallSize / 2 << " " << chunkSmallSize / 2 - 1 << endl;
						break;
					}
				}
			}

			curIndex = curIndex - levelSize;

			level++;
			levelSize = pow(2, level);
			long long oldChunkBigSize = chunkBigSize;
			long long oldChunkSmallSize = chunkSmallSize;
			long long oldEvenCount = evenCount;
			long long oldOddCount = oddCount;

			chunkBigSize = oldChunkBigSize / 2;
			chunkSmallSize = oldChunkBigSize / 2 - 1 * (oldEvenCount > 0 ? 1 : 0);

			evenCount = oldEvenCount; // +2 * oldOddCount * (oldOddChunkSize % 2 == 0 ? 1 : 0); // !
			oddCount = oldEvenCount; // +2 * oldOddCount * (oldOddChunkSize % 2 == 1 ? 1 : 0);

			if (oldChunkBigSize % 2 == 1)
			{
				long long fromOddChunkSize = oldChunkBigSize / 2;
				if (fromOddChunkSize % 2 == 1)
				{
					oddCount += 2 * oldOddCount;
				}
				else
				{
					evenCount += 2 * oldOddCount;
				}
			}
			else if (oldChunkSmallSize % 2 == 1)
			{
				long long fromOddChunkSize = oldChunkSmallSize / 2;
				if (fromOddChunkSize % 2 == 1)
				{
					oddCount += 2 * oldOddCount;
				}
				else
				{
					evenCount += 2 * oldOddCount;
				}
			}
		}


		/*queue<SChunk> Q;
		Q.push(SChunk{ 1, N });
		vector<SChunk> level;

		long long posCount = 0;
		long long minLR = -1;
		long long maxLR = -1;
		while (posCount < K)
		{
			if (Q.empty())
			{
				sort(level.begin(), level.end(), [](const SChunk&lhs, const SChunk& rhs) -> bool {
					if (lhs.Size() != rhs.Size())
					{
						return lhs.Size() > rhs.Size();
					}
					else
					{
						return lhs.start < rhs.start;
					}
				});
				for (long long i = 0; i < level.size(); ++i)
				{
					Q.push(level[i]);
				}
				level.clear();
			}

			SChunk cur = Q.front(); Q.pop();
			SChunk left;
			SChunk right;
			SelectPos(cur, left, right);
			posCount++;
			if (right.Size() > left.Size())
			{
				if (right.Size() > 0)
					level.push_back(right);
				if (left.Size() > 0)
					level.push_back(left);
			}
			else
			{
				if (left.Size() > 0)
					level.push_back(left);
				if (right.Size() > 0)
					level.push_back(right);
			}
			minLR = min(left.Size(), right.Size());
			maxLR = max(left.Size(), right.Size());
		}

		out << maxLR << " " << minLR << endl;*/
	}

	return 0;
}