#include <fstream>
#include <string>
#include <set>

bool is_happy(const std::string &s) {
	int len = s.length();

	for (int i = 0; i < len; i++) {
		if (s[i] == '-') return false;
	}

	return true;
}

void limpa_stack(std::string &stack, const int &flipper, int &count) {
	int i, j;
	int len = stack.length() - flipper;

	bool break_i;

	for (i = 0; i <= len; i++) {
		break_i = false;
		for (j = 0; j < flipper; j++) {
			if (stack[i + j] != '-') {
				break_i = true;
				break;
			}
		}
		
		if (break_i) continue;

		for (int j = 0; j < flipper; j++) {
			stack[i + j] = '+';
		}
		i += flipper - 1;
		count++;
	}
}

int max_sequence(std::string &s, const int &flipper) {
	int i, j, aux_count, max_seq_i = -1, max_seq_count = 0;
	int len = s.length();

	for (i = 0; i < len; i++) {
		aux_count = 0;
		j = i;
		while (j < len && s[j] == '-') {
			aux_count++;
			j++;
		}

		if (aux_count > max_seq_count) {
			max_seq_i = i;
			max_seq_count = aux_count;
		}

		i = j;
	}

	return max_seq_i;
}

void flip_max(std::string &stack, const int &flipper, int &count) {
	int begin = max_sequence(stack, flipper);
	
	if (begin < 0)
		return;

	if (begin > stack.length() - flipper)
		begin = stack.length() - flipper;

	int len = begin + flipper;

	for (; begin < len; begin++) {
		if (stack[begin] == '-') stack[begin] = '+';
		else stack[begin] = '-';
	}
	count++;
}

std::string eval_pancakes(std::string &stack, int &flipper) {
	int count = 0;
	std::set<std::string> seen;
	seen.insert(std::string(stack));

	while (!is_happy(stack)) {
		limpa_stack(stack, flipper, count);
		
		flip_max(stack, flipper, count);
		if (!std::get<1>(seen.insert(stack))) return "IMPOSSIBLE";
	}

	return std::to_string(count);
}

int main() {
	std::string name = "A-small-attempt1";
	std::ifstream fin(name + ".in");
	std::ofstream fout(name + ".out");
	
	if (!fin.is_open() || !fout.is_open())
		return -2;

	int N; fin >> N;
	fin.ignore(1000, '\n');

	std::string stack;
	int flipper;
	for (int i = 1; i <= N; i++) {
		std::getline(fin, stack, ' ');
		fin >> flipper;
		fin.ignore(1000, '\n');
		fout << "Case #" << i << ": " << eval_pancakes(stack, flipper);
		if (i < N) fout << std::endl;
	}

	return 0;
}