#include <iostream>
#include <stdio.h>

#include <vector>
#include <set>

#include <cassert>

void PrintCase(int c, int max, int min) {
	std::cout << "Case #" << c << ": " << max << " " << min << std::endl;
}

/// version 1 -> slow for large numbers
class Bathroom {
	private:
		std::vector<bool> stall_occupied;
		std::vector<int> stall_LS;
		std::vector<int> stall_RS;

		void updateDistances();
		void placeUser(int index);

	public:
		Bathroom(int N) :
			stall_occupied(N, false),
			stall_LS(N, 0),
			stall_RS(N, 0) {

			updateDistances();
		}

		void addUser(int& out_max, int& out_min);
};

void Bathroom::updateDistances() {
	int distanceL = 0;
	int distanceR = 0;

	for (size_t i = 0; i < stall_occupied.size(); ++i) {
		int iLeft = i;
		int iRight = stall_occupied.size() - i - 1;

		// check left to right
		if (stall_occupied[iLeft]) {
			distanceL = 0;
			stall_LS[iLeft] = -1;
		} else {
			stall_LS[iLeft] = distanceL;
			distanceL++;
		}

		// check right to left
		if (stall_occupied[iRight]) {
			distanceR = 0;
			stall_RS[iRight] = -1;
		} else {
			stall_RS[iRight] = distanceR;
			distanceR++;
		}
	}
}

void Bathroom::placeUser(int index) {
	assert(stall_occupied[index] == false);
	stall_occupied[index] = true;

	// update neighbors
	const int N = stall_occupied.size();


	for (int i = index + 1; i < N; ++i) {
		if (stall_occupied[i])
			break;

		stall_LS[i] = i - (index + 1);
	}

	int distance = 0;
	for (int i = index - 1; i >= 0; --i) {
		if (stall_occupied[i])
			break;

		stall_RS[i] = distance++;
	}

	//updateDistances();

}

void Bathroom::addUser(int& out_max, int& out_min) {
	const int N = stall_occupied.size();

	// find maximal min(lS,RS) value and remember it
	std::set<int> equal_max;
	int current_max = -1;

	for (int k = 0; k < N; ++k) {
		if (stall_occupied[k])
			continue;

		int value = std::min(stall_LS[k], stall_RS[k]);

		if (value > current_max) {
			current_max = value;
			equal_max.clear();
			equal_max.insert(k);
		} else if (value == current_max) {
			equal_max.insert(k);
		}
	}

	assert(!equal_max.empty());

	// if there is only one match then we found it
	if (equal_max.size() == 1) {
		int index = *equal_max.begin();

		out_max = std::max(stall_LS[index], stall_RS[index]);
		out_min = std::min(stall_LS[index], stall_RS[index]);

		placeUser(index);
		//printf("%d user %d choose %d\n", i, j, index);
		return;
	}

	assert(equal_max.size() > 1);

	// more than one stall -> find max of max(lS, RS)
	current_max = 0;
	int current_max_index = *equal_max.begin();

	for (int index : equal_max) {
		int value = std::max(stall_LS[index], stall_RS[index]);

		if (value > current_max) {
			current_max = value;
			current_max_index = index;
		}
	}

	// now we found the leftmost maximum (leftmost because the std::set is sorted
	int index = current_max_index;

	out_max = std::max(stall_LS[index], stall_RS[index]);
	out_min = std::min(stall_LS[index], stall_RS[index]);

	placeUser(index);
	//printf("%d user %d choose %d\n", i, j, index);
}

/// version 2
class Bathroom2 {
	private:
		std::vector<bool> stall_occupied;
		std::set<int> occupied_index;

		void placeUser(int index);

	public:
		Bathroom2(int N) :
			stall_occupied(N, false),
			occupied_index({-1, N}) {}

		void addUser(int& out_max, int& out_min);
};

void Bathroom2::placeUser(int index) {
	assert(stall_occupied[index] == false);
	stall_occupied[index] = true;

	occupied_index.insert(index);

//	printf("Place user at %d\n", index);
}

struct Position {
	int index;
	int distL;
	int distR;

	bool operator<(const Position& other) const {
		return index < other.index;
	}
};

void Bathroom2::addUser(int& out_max, int& out_min) {
    std::set<Position> largest_distances;
    int largest_distances_distance = -1;

    // iterate over all occupied stalls and find the middles
    for (std::set<int>::const_iterator i = occupied_index.begin(); i != occupied_index.end(); ++i) {
		auto j = i; j++;

		if (j == occupied_index.end())
			break;

		int current = *i;
		int next = *j;

		if (current + 1 == next)
			continue;	// no free stall

		int middle = (next + current) / 2;

		assert(!stall_occupied[middle]);

		int distL = middle - current - 1;
		int distR = next - middle - 1;

		//printf("middle: %d %d %d\n", middle, distL, distR);

		int distMin = std::min(distL, distR);

		if (distMin >= largest_distances_distance) {
			if (distMin > largest_distances_distance) {
				largest_distances.clear();
				largest_distances_distance = distMin;
			}

			largest_distances.insert({middle, distL, distR});

			if (distL + 1 == distR)
				largest_distances.insert({middle + 1, distL + 1, distR - 1});
		}
    }
#if 0
    printf("candidates: (distance %d)\n", largest_distances_distance);
    for (auto c : largest_distances) {
		printf("%d, ", c.index);
    }
    printf("\n");
#endif

    if (largest_distances.size() == 1) {
		Position entry = *largest_distances.begin();

		placeUser(entry.index);
		out_max = std::max(entry.distL, entry.distR);
		out_min = std::min(entry.distL, entry.distR);
		return;
    }

    // find the max of std::max(distL, distR)
    std::set<Position> final_candidates;
    int current_max = -1;

    for (const Position& i : largest_distances) {
		int value = std::max(i.distL, i.distR);

		if (value > current_max) {
			current_max = value;
			final_candidates.clear();
			final_candidates.insert(i);
		} else if (value == current_max) {
			final_candidates.insert(i);
		}
    }

    assert(final_candidates.size() > 0);

    // take the leftmost (smallest)
    Position result = *final_candidates.begin();

    placeUser(result.index);

	out_max = std::max(result.distL, result.distR);
	out_min = std::min(result.distL, result.distR);
}

int main() {
	int N, K;
	int T;

	std::cin >> T;

	for (int i = 0; i < T; ++i) {
		std::cin >> N;
		std::cin >> K;

		assert(K <= N);

		Bathroom2 bathroom(N);

		// iterate over all users
		for (int j = 0; j < K; ++j) {
			bool last_user = j == K - 1;

			int max, min;
			bathroom.addUser(max, min);

			if (last_user)
				PrintCase(i + 1, max, min);

		}

	}

	return 0;
}
