#include"iostream"
#include"cstdio"
#include"vector"
#include"string"
#include"unordered_map"
#include"algorithm"
using namespace std;
class Range
{
public:
	long long Left;
	long long Right;
public:
	Range(const long long L = 0, const long long R = 0)
		:Left(L), Right(R)
	{
	};
	Range(){};

	bool operator<(const Range &R) const
	{
		long long Diff = (Right - Left) - (R.Right - R.Left);
		return Diff == 0 ? (Left > R.Left) : (Diff < 0);
	};

	pair<Range, Range> iSplit()
	{
		if ((Right - Left) == 0) { return make_pair(Range(1,0), Range(1,0)); }

		long long Mid = Left + ((Right - Left) / 2);
		return make_pair(Range(Left, Mid - 1), Range(Mid + 1, Right));
	};

	long long iEmpty()
	{
		return Right < Left;
	};

	long long iRange()
	{
		return max(static_cast<long long>(0), Right - Left);
	};

	long long iMin() { return min(Left, Right); };
	long long iMax() { return max(Left, Right); };
};

class RangeCount : public Range
{
public:
	long long Count;
public:
	RangeCount(const long long L = 0, const long long R = 0, const long long Count = 1)
		:Range(L, R), Count(Count)
	{
	};
	RangeCount(const Range &R, const long long Count = 1)
		:Range(R.Left, R.Right), Count(Count)
	{
	};
	~RangeCount() {};

	bool operator<(const RangeCount &RC) const
	{
		return static_cast<const Range*>(this)->operator<(RC);
	};

	void iAdd() { Count++; };
	void iAdd(long long Val) { Count = Count + Val; };

	void iSub() { Count--; };
	void iSub(long long Val) { Count = Count - Val; };

	bool iIsZero() { return Count <= 0; };
};
void heap_main(long long Item, long long N, long long K)
{
	if (N == K) { ::cout << "Case #" << Item + 1 << ": 0 0" << endl; return; }

	vector<Range> Heap;
	Heap.push_back(Range(0, N - 1));

	make_heap(Heap.begin(), Heap.end());

	for (long long seek = 1; seek < K; seek = seek + 1)
	{
		auto R = Heap.front();

		pop_heap(Heap.begin(), Heap.end());
		Heap.pop_back();

		auto Pair = R.iSplit();

		if (!Pair.first.iEmpty())
		{
			Heap.push_back(Pair.first);
			push_heap(Heap.begin(), Heap.end());
		}

		if (!Pair.second.iEmpty())
		{
			Heap.push_back(Pair.second);
			push_heap(Heap.begin(), Heap.end());
		}
	}

	auto Res = Heap.front().iSplit();

	long long Left = Res.first.iEmpty() ? 0 : Res.first.iRange() + 1;
	long long Right = Res.second.iEmpty() ? 0 : Res.second.iRange() + 1;

	long long Max = max(Left, Right);
	long long Min = min(Left, Right);

	::cout << "Case #" << Item + 1 << ": " << Max << " " << Min << endl;
}
void space_count_main(long long Item, long long N, long long K)
{
	if (N == K) { ::cout << "Case #" << Item + 1 << ": 0 0" << endl; return; }

	vector<RangeCount*> Heap;
	unordered_map<long long, RangeCount*> HashTable;

	auto CompFunc = [](const Range* pR1, const Range* pR2) { return *pR1 < *pR2; };

	Heap.push_back(new RangeCount(0, N - 1));
	HashTable[Heap.front()->iRange()] = Heap.front();

	make_heap(Heap.begin(), Heap.end(), CompFunc);

	for (long long seek = 1; seek < K; seek = seek + 1)
	{
		auto R = *Heap.front();

		Heap.front()->iSub();

		if (Heap.front()->iIsZero())
		{
			HashTable.erase(HashTable.find(R.iRange()));

			auto ptr = Heap.front();

			pop_heap(Heap.begin(), Heap.end(), CompFunc);
			Heap.pop_back();

			delete ptr;
			ptr = nullptr;
		}

		auto Pair = R.iSplit();

		if (!Pair.first.iEmpty())
		{
			auto It = HashTable.find(Pair.first.iRange());
			if ( It != HashTable.end())
			{
				It->second->iAdd();
			}
			else
			{
				Heap.push_back(new RangeCount(Pair.first));
				HashTable[Pair.first.iRange()] = Heap.back();

				push_heap(Heap.begin(), Heap.end(), CompFunc);
			}
		}

		if (!Pair.second.iEmpty())
		{
			auto It = HashTable.find(Pair.second.iRange());

			if (It != HashTable.end())
			{
				It->second->iAdd();
			}
			else
			{
				Heap.push_back(new RangeCount(Pair.second));
				HashTable[Pair.second.iRange()] = Heap.back();

				push_heap(Heap.begin(), Heap.end(), CompFunc);
			}
		}

		int val = 0;
	}

	auto Res = Heap.front()->iSplit();

	long long Left = Res.first.iEmpty() ? 0 : Res.first.iRange() + 1;
	long long Right = Res.second.iEmpty() ? 0 : Res.second.iRange() + 1;

	long long Max = max(Left, Right);
	long long Min = min(Left, Right);

	::cout << "Case #" << Item + 1 << ": " << Max << " " << Min << endl;

	for (auto ptr : Heap)
	{
		delete ptr;
		ptr = nullptr;
	}
}
void space_count_opt_main(long long Item, long long N, long long K)
{
	if (N == K) { ::cout << "Case #" << Item + 1 << ": 0 0" << endl; return; }

	vector<RangeCount*> Heap;
	unordered_map<long long, RangeCount*> HashTable;

	auto CompFunc = [](const Range* pR1, const Range* pR2) { return *pR1 < *pR2; };

	Heap.push_back(new RangeCount(0, N - 1));
	HashTable[Heap.front()->iRange()] = Heap.front();

	make_heap(Heap.begin(), Heap.end(), CompFunc);

	long long seek = 1;
	while (seek < K)
	{
		auto R = *Heap.front();

		if ((seek + R.Count) > K) { break; }

		//Delete
		HashTable.erase(HashTable.find(R.iRange()));

		auto ptr = Heap.front();

		pop_heap(Heap.begin(), Heap.end(), CompFunc);
		Heap.pop_back();

		delete ptr;
		ptr = nullptr;

		//Add seek
		seek = seek + R.Count;

		//Generate
		auto Pair = R.iSplit();

		if (!Pair.first.iEmpty())
		{
			auto It = HashTable.find(Pair.first.iRange());
			if (It != HashTable.end())
			{
				It->second->iAdd(R.Count);
			}
			else
			{
				Heap.push_back(new RangeCount(Pair.first, R.Count));
				HashTable[Pair.first.iRange()] = Heap.back();

				push_heap(Heap.begin(), Heap.end(), CompFunc);
			}
		}

		if (!Pair.second.iEmpty())
		{
			auto It = HashTable.find(Pair.second.iRange());

			if (It != HashTable.end())
			{
				It->second->iAdd(R.Count);
			}
			else
			{
				Heap.push_back(new RangeCount(Pair.second, R.Count));
				HashTable[Pair.second.iRange()] = Heap.back();

				push_heap(Heap.begin(), Heap.end(), CompFunc);
			}
		}

		int val = 0;
	}

	auto Res = Heap.front()->iSplit();

	long long Left = Res.first.iEmpty() ? 0 : Res.first.iRange() + 1;
	long long Right = Res.second.iEmpty() ? 0 : Res.second.iRange() + 1;

	long long Max = max(Left, Right);
	long long Min = min(Left, Right);

	::cout << "Case #" << Item + 1 << ": " << Max << " " << Min << endl;

	for (auto ptr : Heap)
	{
		delete ptr;
		ptr = nullptr;
	}
}
void array_main(long long Item, long long N, long long K)
{
	if (N == K) { ::cout << "Case #" << Item + 1 << ": 0 0" << endl; return; }

	vector<Range> Set(N, Range(0, 0));

	for (long long seek = 0; seek < N; seek = seek + 1)
	{
		Set[seek].Left = seek;
		Set[seek].Right = N - seek - 1;
	}

	for (long long seek = 1; seek < K; seek = seek + 1)
	{
		long long Index = 0;

		for (long long seek_s = 0; seek_s < N; seek_s = seek_s + 1)
		{
			if (Set[seek_s].Left == -1) { continue; }

			if (Set[Index].iMin() > Set[seek_s].iMin()) { continue; }
			if (Set[Index].iMin() == Set[seek_s].iMin())
			{
				if (Set[Index].iMax() >= Set[seek_s].iMax())
				{
					continue;
				}
			}

			Index = seek_s;
		}

		Set[Index] = Range(-1, -1);

		//Set
		long long Begin = Index - 1;
		long long End = Index - 1;

		while ((Begin >= 0) && (Set[Begin].Left != -1)) { Begin--; }
		Begin = Begin + 1;

		for (long long seek_s = Begin; seek_s <= End; seek_s = seek_s + 1)
		{
			Set[seek_s].Left = seek_s - Begin;
			Set[seek_s].Right = End - seek_s;
		}


		Begin = Index + 1;
		End = Index + 1;

		while ((End < N) && (Set[End].Left != -1)) { End++; }
		End = End - 1;

		for (long long seek_s = Begin; seek_s <= End; seek_s = seek_s + 1)
		{
			Set[seek_s].Left = seek_s - Begin;
			Set[seek_s].Right = End - seek_s;
		}

		long long val = 0;
	}


	long long Index = 0;

	for (long long seek_s = 0; seek_s < N; seek_s = seek_s + 1)
	{
		if (Set[seek_s].Left == -1) { continue; }

		if (Set[Index].iMin() > Set[seek_s].iMin()) { continue; }
		if (Set[Index].iMin() == Set[seek_s].iMin())
		{
			if (Set[Index].iMax() >= Set[seek_s].iMax())
			{
				continue;
			}
		}

		Index = seek_s;
	}

	::cout << "Case #" << Item + 1 << ": " << Set[Index].iMax() << " " << Set[Index].iMin() << endl;
}
int main()
{
	long long InputSize;
	::cin >> InputSize;

	for (long long seek_times = 0; seek_times < InputSize; seek_times = seek_times + 1)
	{
		long long N = 0;
		long long K = 0;

		::cin >> N >> K;

		//heap_main(seek_times, N, K);
		//space_count_main(seek_times, N, K);
		space_count_opt_main(seek_times, N, K);
		//array_main(seek_times, N, K);
	}

	return 0;
}