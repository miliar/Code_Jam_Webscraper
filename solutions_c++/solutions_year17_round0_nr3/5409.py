#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;

struct Seat {
	long long ls;
	long long rs;
	long long min;
	long long max;
	bool is_occupied() const { return ls == -1 ? true : false; }
};


inline void update(std::vector<Seat> &seats) {
	for (size_t i = 0; i != seats.size(); ++i) {
		if (!seats[i].is_occupied())
		{
			seats[i].ls = seats[i - 1].ls + 1;
		}
	}
	for (size_t i = seats.size() - 1; i != -1; --i) {
		if (!seats[i].is_occupied())
		{
			seats[i].rs = seats[i + 1].rs + 1;
		}
	}
	for (auto &i : seats) {
		if (!i.is_occupied()) {
			i.min = i.ls < i.rs ? i.ls : i.rs;
			i.max = i.ls > i.rs ? i.ls : i.rs;
		}
	}
}

int main()
{
	unsigned T;
	cin >> T;
	cin.get();
	for (unsigned case_num = 1; case_num <= T; ++case_num) {
		long long seats_num;
		long long people_num;
		cin >> seats_num >> people_num;

		const Seat occupied = { -1, -1, -1, -1 };
		std::vector<Seat> seats(seats_num + 2, { 0, 0, 0, 0 });
		seats[0] = seats[seats_num + 1] = occupied;

		Seat res = { 0 };
		for (long long i = 0; i != people_num; ++i) {
			update(seats);

			////DEBUG
			//for (auto i : seats)
			//	cout << "LS: " << i.ls << " RS: " << i.rs << " Max: "
			//	<< i.max << " Min: " << i.min << endl;

			Seat *curr = nullptr;
			for (auto &seat : seats) {
				if (curr == nullptr) {
					if (!seat.is_occupied())
						curr = &seat;
				}
				else if (!seat.is_occupied()) {
					if (curr->min < seat.min ||
						(curr->min == seat.min && curr->max < seat.max)) {
						curr = &seat;
					}
				}
			}
			if (i != people_num - 1) {
				*curr = occupied;
			}
			else {
				res = *curr;
			}
		}

		cout << "Case #" << case_num << ": " << res.max << ' ' << res.min;

		cout << endl;
	}
	return 0;
}
