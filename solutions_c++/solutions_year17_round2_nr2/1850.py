#include <iostream>
#include <map>
#include <string>

typedef std::map<char, int> char_int_map;

void put_for_empty_stables(std::string& stables, char_int_map& unicorns) {
	if (unicorns['R'] > 0) {
		stables.push_back('R');
		--unicorns['R'];
	}
	else if (unicorns['Y'] > 0) {
		stables.push_back('Y');
		--unicorns['Y'];
	}
	else if (unicorns['B'] > 0) {
		stables.push_back('B');
		--unicorns['B'];
	}
	else if (unicorns['O'] > 0) {
		stables.push_back('O');
		--unicorns['O'];
	}
	else if (unicorns['G'] > 0) {
		stables.push_back('G');
		--unicorns['G'];
	}
	else if (unicorns['V'] > 0) {
		stables.push_back('V');
		--unicorns['V'];
	}
}

bool is_available_unicorns_for_r(std::string& stables, char_int_map& unicorns) {
	if (unicorns['G'] > 0) {
		stables.push_back('G');
		--unicorns['G'];
		return true;
	}
	else if (unicorns['Y'] > 0 || unicorns['B'] > 0) {
		if (unicorns['Y'] > unicorns['B']) {
			stables.push_back('Y');
			--unicorns['Y'];
			return true;
		}
		else {
			stables.push_back('B');
			--unicorns['B'];
			return true;
		}
	}
	return false;
}

bool is_available_unicorns_for_y(std::string& stables, char_int_map& unicorns) {
	if (unicorns['V'] > 0) {
		stables.push_back('V');
		--unicorns['V'];
		return true;
	}
	else if (unicorns['R'] > 0 || unicorns['B'] > 0) {
		if (unicorns['R'] > unicorns['B']) {
			stables.push_back('R');
			--unicorns['R'];
			return true;
		}
		else {
			stables.push_back('B');
			--unicorns['B'];
			return true;
		}
	}
	return false;
}

bool is_available_unicorns_for_b(std::string& stables, char_int_map& unicorns) {
	if (unicorns['O'] > 0) {
		stables.push_back('O');
		--unicorns['O'];
		return true;
	}
	else if (unicorns['Y'] > 0 || unicorns['R'] > 0) {
		if (unicorns['Y'] > unicorns['R']) {
			stables.push_back('Y');
			--unicorns['Y'];
			return true;
		}
		else {
			stables.push_back('R');
			--unicorns['R'];
			return true;
		}
	}
	return false;
}

bool is_available_unicorns_for_o(std::string& stables, char_int_map& unicorns) {
	if (unicorns['B'] > 0) {
		stables.push_back('B');
		--unicorns['B'];
		return true;
	}
	return false;
}

bool is_available_unicorns_for_g(std::string& stables, char_int_map& unicorns) {
	if (unicorns['R'] > 0) {
		stables.push_back('R');
		--unicorns['R'];
		return true;
	}
	return false;
}

bool is_available_unicorns_for_v(std::string& stables, char_int_map& unicorns) {
	if (unicorns['Y'] > 0) {
		stables.push_back('Y');
		--unicorns['Y'];
		return true;
	}
	return false;
}

bool is_available_unicorns(std::string& stables, char_int_map& unicorns) {
	switch (stables.back())	{
	case 'R': return is_available_unicorns_for_r(stables, unicorns);
	case 'Y': return is_available_unicorns_for_y(stables, unicorns);
	case 'B': return is_available_unicorns_for_b(stables, unicorns);
	case 'O': return is_available_unicorns_for_o(stables, unicorns);
	case 'G': return is_available_unicorns_for_g(stables, unicorns);
	case 'V': return is_available_unicorns_for_v(stables, unicorns);
	default: return false;
	}
	return false;
}

bool is_last_not_conflict_first(std::string const& stables) {
	switch (stables.back()) {
	case 'R': return stables.front() == 'Y' || stables.front() == 'B' || stables.front() == 'G';
	case 'Y': return stables.front() == 'R' || stables.front() == 'B' || stables.front() == 'V';
	case 'B': return stables.front() == 'R' || stables.front() == 'Y' || stables.front() == 'O';
	case 'O': return stables.front() == 'B';
	case 'G': return stables.front() == 'R';
	case 'V': return stables.front() == 'Y';
	}
	return false;
}

std::string arrange_stables(size_t number_of_unicorns) {
	char_int_map unicorns;
	std::cin >> unicorns['R'] >> unicorns['O'] >> unicorns['Y'] >> unicorns['G'] >> unicorns['B'] >> unicorns['V'];
	std::string stables;
	while (stables.length() < number_of_unicorns) {
		if (stables.empty()) {
			put_for_empty_stables(stables, unicorns);				
		}
		else {
			if (!is_available_unicorns(stables, unicorns)) {
				return "IMPOSSIBLE";
			}
		}
	}
	if (!is_last_not_conflict_first(stables)) {
		return "IMPOSSIBLE";
	}
	return stables;
}

int main(void) {
	int total_test_case;
	std::cin >> total_test_case;
	int count = 0;
	while (count < total_test_case) {
		size_t number_of_unicorns;
		std::cin >> number_of_unicorns;
		std::cout << "Case #" << count + 1 << ": " << arrange_stables(number_of_unicorns) << std::endl;
		++count;
	}
}