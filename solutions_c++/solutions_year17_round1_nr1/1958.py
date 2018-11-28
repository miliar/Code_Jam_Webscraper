#include <iostream>

#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class process {
public:
	process(vector<string>& data, int cx, int cy) :
		data(data), cx(cx), cy(cy)
	{
		calcRects();
		enlargeRects();
	}
private:
	vector<string>& data;
	int cx, cy;

	struct rect_t {
		int left, top, right, bottom;
		rect_t() :
			left(-1), top(-1), right(-1), bottom(-1) { }
		rect_t(int x, int y) :
			left(x), top(y), right(x), bottom(y) { }
		void add(int x, int y) {
			if (x < left)
				left = x;
			else if (x > right)
				right = x;
			if (y < top)
				top = y;
			else if (y > bottom)
				bottom = y;
		}
	};
	std::unordered_map<char, rect_t> rects;

	void calcRects() {
		for (int y = 0; y < cy; ++y) {
			for (int x = 0; x < cx; ++x) {
				char c = data[y][x];
				if (c == '?')
					continue;
				if (rects.find(c) == rects.end()) {
					rects.insert(make_pair(c, rect_t(x, y)));
				}
				else {
					rects[c].add(x, y);
				}
			}
		}
		// fill
		for (auto &kv : rects) {
			for (int y = kv.second.top; y <= kv.second.bottom; ++y)
				for (int x = kv.second.left; x <= kv.second.right; ++x)
					data[y][x] = kv.first;
		}
	}

	bool tryFillRow(int y, int sx, int dx, char value) {
		for (int x = sx; x <= dx; ++x)
			if (data[y][x] != '?')
				return false;
		for (int x = sx; x <= dx; ++x)
			data[y][x] = value;
		return true;
	}

	bool tryFillColumn(int x, int sy, int dy, char value) {
		for (int y = sy; y <= dy; ++y)
			if (data[y][x] != '?')
				return false;
		for (int y = sy; y <= dy; ++y)
			data[y][x] = value;
		return true;
	}

	void enlargeRects() {
		for (auto &kv : rects) {
			for (; kv.second.left > 0; --kv.second.left)
				if (!tryFillColumn(kv.second.left - 1, kv.second.top, kv.second.bottom, kv.first))
					break;
			for (; kv.second.right < cx - 1; ++kv.second.right)
				if (!tryFillColumn(kv.second.right + 1, kv.second.top, kv.second.bottom, kv.first))
					break;

			for (; kv.second.top > 0; --kv.second.top)
				if (!tryFillRow(kv.second.top - 1, kv.second.left, kv.second.right, kv.first))
					break;
			for (; kv.second.bottom < cy - 1; ++kv.second.bottom)
				if (!tryFillRow(kv.second.bottom + 1, kv.second.left, kv.second.right, kv.first))
					break;
		}
	}
};

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int cy, cx;
		cin >> cy >> cx;

		vector<string> data;
		data.resize(cy);
		for (int j = 0; j < cy; ++j)
			cin >> data[j];

		process(data, cx, cy);

		cout << "Case #" << i << ":" << endl;
		for (int j = 0; j < cy; ++j)
			cout << data[j] << endl;
	}
    return 0;
}
