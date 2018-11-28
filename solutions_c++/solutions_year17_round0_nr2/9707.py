#include <fstream>
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdint>

static void next_tidy(std::string &tidy)
{
	for (auto i = tidy.size() - 1; i != 0; --i) {
		if (tidy[i] != tidy[i - 1]) {
			tidy[i] -= 1;
			for (auto j = i + 1; j < tidy.size(); ++j) {
				tidy[j] = '9';
			}
			return;
		}
	}

	tidy[0] -= 1;
	for (decltype(tidy.size()) i = 1; i < tidy.size(); ++i) {
		tidy[i] = '9';
	}
}


static std::string solve_case(const std::string &the_case)
{
	const auto N = std::stoull(the_case);
	auto init = the_case;
	for (auto &ch : init) {
		ch = '9';
	}
	while (true) {
		if (std::stoull(init) <= N) {
			return std::to_string(std::stoull(init));
		}
		next_tidy(init);
	}
	return "ERROR";
}

////////////////////////////////////////////////////////////////////////////////
static std::string replace_extension(const std::string &str,
                                     const std::string &ext)
{
	auto dot_idx = str.rfind(".");
	if (dot_idx == std::string::npos) {
		return str + "." + ext;
	} else {
		return str.substr(0, dot_idx) + "." + ext;
	}
}

int main(int argc, char *argv[])
{
	if (argc != 2) {
		std::cerr << "Usage: " << argv[0] << " <in_file>\n";
		return EXIT_FAILURE;
	}

	std::string in_name = argv[1];
	std::string out_name = replace_extension(in_name, "out");

	std::ifstream in(in_name);
	std::ofstream out(out_name);

	if (!in) {
		std::cerr << "Error opening file " << in_name
		          << " for reading\n";
		return EXIT_FAILURE;
	}
	if (!out) {
		std::cerr << "Error opening file " << out_name
		          << " for writing\n";
		return EXIT_FAILURE;
	}

	std::uint64_t case_number = 0;
	for (std::string line; std::getline(in, line);) {
		if (case_number) {
			out << "Case #" << case_number << ": " 
			    << solve_case(line) << "\n";
		}
		++case_number;
	}
}
