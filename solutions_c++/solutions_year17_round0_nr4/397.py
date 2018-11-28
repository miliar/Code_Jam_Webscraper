#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <fstream>

struct item_t {
	item_t(char v, int x, int y) : v(v), x(x), y(y) {}

	char v;
	int x;
	int y;
};

struct edge_t {
	edge_t(int a, int b) : a(a), b(b) {}

	int a;
	int b;
};

struct input_t {
	int n;
	int m;
	vector <item_t> items;
};

void remove(vector<edge_t> &v, const item_t &item);

void prepare_result_merge_our(vector<item_t> &v);

void prepare_result_up_input(vector<item_t> &vv, const vector<item_t> &inp);

unsigned long long calc_score(const vector<item_t> &v);

string solve(const input_t & inp) {

	vector <item_t> result;

	std::stringstream sr;

	// Rooks.
	unordered_set <int> horiz;
	unordered_set <int> vert;

	for(int i = 1; i <= inp.m; ++i) {
		horiz.insert(i);
		vert.insert(i);
	}

	// Bishops.
	vector <edge_t> diags;
	for(int i = 1; i <= inp.m; ++i) {
		for(int j = 1; j <= inp.m; ++j) {
			diags.push_back(edge_t(i+j,i-j));
		}
	}

	// remove initial.
	for(int i = 0; i < inp.n; ++i) {
		if ((inp.items[i].v == 'x') || (inp.items[i].v == 'o')) {
			horiz.erase(inp.items[i].x);
			vert.erase(inp.items[i].y);
		}
		if ((inp.items[i].v == '+') || (inp.items[i].v == 'o')) {
			remove(diags, inp.items[i]);
		}
	}

	// put Rooks
	auto ih = horiz.begin();
	for(auto iv: vert) {
		result.push_back(item_t('x', *ih, iv));
		++ih;
	}

	// put Bishops.
	while(!diags.empty()) {
		// find min left & right

		// key - diag value, value - quantity
		unordered_map <int, int> left;
		unordered_map <int, int> right;

		for(auto e:diags) {
			if (left.find(e.a) == left.end()) {
				left[e.a]=1;
			}
			else ++left[e.a];

			if (right.find(e.b) == right.end()) {
				right[e.b]=1;
			}
			else ++right[e.b];
		}

		int min_left_pos = (int)1e7;
		int min_left_value = (int)1e7;
		for(auto l: left) {
			if (l.second < min_left_value) {
				min_left_value = l.second;
				min_left_pos = l.first;
			}
		}

		int min_right_pos = (int)1e7;
		int min_right_value = (int)1e7;
		for(auto l: right) {
			if (l.second < min_right_value) {
				min_right_value = l.second;
				min_right_pos = l.first;
			}
		}

		if (min_left_value <= min_right_value) {
			// min is on the left
			for(auto e:diags) {
				if (e.a == min_left_pos) {
					// put here (a,b).
					item_t item('+', (e.a+e.b)/2, (e.a-e.b)/2);
					result.push_back(item);
					remove(diags, item);
					break;
				}
			}
		}
		else {
			// min is on the right
			for(auto e:diags) {
				if (e.b == min_right_pos) {
					// put here (a,b).
					item_t item('+', (e.a+e.b)/2, (e.a-e.b)/2);
					result.push_back(item);
					remove(diags, item);
					break;
				}
			}
		}
	}

	auto score = calc_score(inp.items) + calc_score(result);

	prepare_result_merge_our(result);
	prepare_result_up_input(result, inp.items);

	sr << score << " " << result.size() << "\n";

	for(auto r: result) {
		sr << r.v << " " << r.x << " " << r.y << "\n";
	}

	return sr.str();
}

unsigned long long int calc_score(const vector<item_t> &v) {
	unsigned long long result = v.size();
	for(auto i:v)
	{
		if (i.v == 'o')
			++result;
	}
	return result;
}

void prepare_result_up_input(vector<item_t> &vv, const vector<item_t> &inp) {
	for(int i = 0; i < vv.size(); ++i) {
		for(int j = 0; j < inp.size(); ++j) {
			if ((vv[i].x == inp[j].x) && (vv[i].y == inp[j].y)) {
				vv[i].v = 'o';
			}
		}
	}
}

void prepare_result_merge_our(vector<item_t> &v) {
	vector<item_t> r;

	for(int i = 0; i < v.size(); ++i) {
		bool found = false;
		if (v[i].v == ' ') continue;
		for(int j = i+1; j < v.size(); ++j) {
			if ((v[i].x == v[j].x) && (v[i].y == v[j].y)) {
				found = true;
				r.push_back(item_t('o', v[i].x, v[i].y));
				v[j].v = ' ';
			}
		}
		if (!found)
			r.push_back(v[i]);
	}
	v = r;
}

void remove(vector<edge_t> &v, const item_t &item){
	const int aa = item.x + item.y;
	const int bb = item.x - item.y;

	vector<edge_t> v_new;
	for(auto i:v) {
		if ((i.a != aa) && (i.b != bb)){
			v_new.push_back(i);
		}
	}
	v = v_new;
}

int main() {
//	std::ofstream f("out", std::ios::out);
	int n;
	cin >> n;
	string x;
	getline(cin, x);
	for (int i = 1; i <= n; ++i) {
		input_t inp;
		getline(cin, x);
		stringstream ss(x);
		ss >> inp.m >> inp.n;
		for(int i = 0; i < inp.n; ++i) {
			getline(cin, x);
			char v = x[0];
			stringstream ss(x.substr(2));
			int x, y;
			ss >> x >> y;
			inp.items.push_back(item_t(v,x,y));
		}
		stringstream str;
		str << "Case #" << i << ": " << solve(inp);
		cout << str.str();

//		f << str.str();
	}
	return 0;
}