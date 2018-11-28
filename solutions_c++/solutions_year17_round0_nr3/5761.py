#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <utility>
#include <set>

struct Candidate {
	long idx;
	long left;
	long right;

	Candidate(const long& idx_ = 0, const long& left_ = 0, const long& right_ = 0)
		: idx(idx_), left(left_), right(right_) {}

	bool operator<=(const Candidate& oth) {
		if (mn(*this) == mn(oth)) {
			if (mx(*this) == mx(oth)) {
				return idx <= oth.idx;
			}
			return mx(*this) > mx(oth);
		}
		return mn(*this) > mn(oth);
	}

	bool operator>(const Candidate& oth) {
		return !(*this <= oth);
	}

	static long mn(const Candidate& c) {
		return std::min(c.idx - c.left, c.right - c.idx);
	}

	static long mx(const Candidate& c) {
		return std::max(c.idx - c.left, c.right - c.idx);
	}
};

inline Candidate get_candidate(long left, long right) {
	const long s = (left + right) / 2;
	return Candidate(s, left, right);
}

Candidate find_next_stall(std::set<long> stalls) {
	Candidate mn;
	// for (int i = 1; i < stalls.size(); ++i) {
	for (auto it = std::next(stalls.begin(), 1); it != stalls.end(); ++it) {
		const long& left = *std::prev(it, 1);
		const long& right = *it;
		Candidate c = get_candidate(left, right); // stalls[i-1], stalls[i]);
		if (c <= mn) {
			mn = c;
		}
	}
	return mn;
}

std::pair<long, long> last_stall(const long& N, long K) {
	std::set<long> stalls{1, N+2};
	Candidate c;
	while (K-- > 0) {
		c = find_next_stall(stalls);
		stalls.insert(c.idx);
	}
	return std::make_pair(Candidate::mx(c) - 1, Candidate::mn(c) - 1);
}

int main(int argc, char** argv) {
        std::ifstream fin(argv[1], std::ifstream::in);

        int t;
        fin >> t;

        for (int i = 1; i <= t; i++) {
                long N, K;
                fin >> N >> K;
		std::pair<long, long> p = last_stall(N, K);
                std::cout << "Case #" << i << ": " << p.first << " " << p.second << std::endl;
        }

        return 0;
}

