#include <chrono>
#include <fstream>
#include <sstream>
#include <queue>
#include <iostream>

auto read_input(const char* filename){
	std::vector<std::pair<std::string, int>> dataset;
	std::ifstream dataset_file(filename, std::ios::in);

	int test_num;
	dataset_file >> test_num;

	while(!dataset_file.eof()){
		std::string table;
		unsigned int pan_size;
		dataset_file >> table >> pan_size;
		if(table.length())
			dataset.push_back({table, pan_size});
	}
	return dataset;
}

auto solve_1(std::string table, unsigned int pan){
	int flips = 0;
	for(int i = 0; i <= std::max(0ull, table.length() - pan); ++i){
		//std::cout << table << '\n';

		if(table[i] == '-'){
			for(unsigned int f = i; f < i + pan; ++f){
				table[f] = table[f] == '-' ? '+' : '-';
			}
			flips++;
		}
	}

	for(int i = table.length() - 1; i > std::max(table.length() - pan - 1, (pan - 1ull)); --i){
		//std::cout << table << '\n';

		if(table[i] == '-'){
			for(unsigned int f = i; f < i - pan; --f){
				table[f] = table[f] == '-' ? '+' : '-';
			}
			flips++;
		}
	}
	//std::cout << table << '\n';

	if(std::find(table.begin(), table.end(), '-') == table.end())
		return flips;
	else return -1;
}

auto solve_2(std::string table, unsigned int pan){
	std::queue<int> flips;
	int moves = 0;

	for(int i = 0; i <= std::max(0ull, table.length()); ++i){
		if(flips.size() % 2)
			table[i] = table[i] == '-' ? '+' : '-';

		if(i <= (table.length() - pan) && table[i] == '-'){
			table[i] = '+';
			flips.push(i + pan - 1);
			moves++;
		}

		if(flips.size() && flips.front() == i)
			flips.pop();
	}

	for(int i = table.length() - 1; i > std::max(table.length() - pan - 1, (pan - 1ull)); --i){
		if(table[i] == '-'){
			for(unsigned int f = i; f < i - pan; --f)
				table[f] = table[f] == '-' ? '+' : '-';

			moves++;
		}
	}

	if(std::find(table.begin(), table.end(), '-') == table.end())
		return moves;
	else return -1;
}

int main(){
	auto dataset = read_input("A-large.in");
	std::stringstream results;

	int case_num = 0;
	for(auto d : dataset){
		auto result = solve_2(d.first, d.second);
		results << "Case #" << ++case_num << ": ";
		if(result == -1) results << "IMPOSSIBLE" << '\n';
		else results << result << '\n';
	}

	std::fstream file_out("out cpp.txt", std::ios::out);
	file_out << results.str();
	file_out.close();
}

