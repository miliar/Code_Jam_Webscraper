#include <algorithm>
#include <map>
#include <iostream>
#include <set>
#include <tuple>
#include <utility>

using namespace std;

#if 0
struct span
{
	int index;
	int size;

	auto tup() const
	{
		return tie(size, index);
	}

	auto min() const
	{
		return size/2;
	}

	auto max() const
	{
		return size-min();
	}
};

bool operator<(const span &s1, const span &s2)
{
	return s1.tup() < s2.tup();
}

ostream &operator<<(ostream &out, span s)
{
	return out << '{' << s.index << ',' << s.size << '}';
}

int main()
{
	int i;
	cin >> i;
	int c = 0;

	int nstalls;
	int people;
	while (cin >> nstalls >> people)
	{
		++c;
		--people;
		//if (people > nstalls/2+1)
			//cout << "Case #" << c << ": 0 0\n";
		std::set<span> stalls;
		span full{0,nstalls};
		stalls.insert(full);
		while (people--)
		{
			/*
			cout << "\tstalls is";
			for (auto s : stalls)
				cout << ' ' << s;
			cout << '\n';
			*/
			auto s = *prev(stalls.end());
			stalls.erase(prev(stalls.end()));
			auto large_dist = s.size/2;
			auto small_dist = s.size-large_dist-1;
			span s1{s.index, small_dist};
			span s2{s1.index+s1.size+1, large_dist};
			stalls.insert(s1);
			stalls.insert(s2);
			//cout << "\tSplitting " << s << " into " << s1 << " and " << s2 << '\n';
		}
		auto s = *prev(stalls.end());
		cout << "Case #" << c << ": " << (s.min()) << ' ' << (s.max()-1) << '\n';
	}
}
#endif

int main()
{
	int i;
	cin >> i;
	int c = 0;

	uint64_t nstalls;
	uint64_t people;
	while (cin >> nstalls >> people)
	{
		++c;
		std::map<uint64_t, uint64_t, greater<>> spans;
		spans.emplace(nstalls, 1);
		--people;
		while (true)
		{
			/*
			cout << "\tstalls is";
			for (auto &s : spans)
				cout << " {" << s.first << ',' << s.second << '}';
			cout << '\n';
			*/
			auto p=*spans.begin();
			auto n=p.second;
			if (people<n)
				break;
			people-=n;
			auto dist = p.first;
			auto large_dist = dist/2;
			auto small_dist = dist-large_dist-1;
			spans[large_dist] += n;
			spans[small_dist] += n;
			spans.erase(begin(spans));
		}
		/*
			cout << "\tstalls is";
			for (auto &s : spans)
				cout << " {" << s.first << ',' << s.second << '}';
			cout << '\n';
			*/
		auto s = *spans.begin();
		cout << "Case #" << c << ": " << (s.first/2) << ' ' << (s.first-s.first/2-1) << '\n';
	}
}
