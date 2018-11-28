#include <string>
#include <fstream>
#include <iostream>

// problem a: oversized pancake flipper.
/*int main(int argc, char **argv)
{
	if (argc == 3) {
		std::ifstream in(argv[1]);
		std::ofstream out(argv[2]);

		if (in.is_open() && out.is_open()) {
            auto tdata = std::size_t(0);
			auto line = std::string("");

			// get total number of data sets.
			std::getline(in, line);
			tdata = std::stoul(line);

			// loop through data sets and solve.
			auto ndata = std::size_t(1);
			auto width = std::size_t(0);
			auto data = std::string("");
			while (std::getline(in, line)) {
				// separate data from width.
				const auto pos = line.find(" ");
				if (pos != std::string::npos) {
					data = line.substr(0, pos);
					width = std::stoul(line.substr(pos));
				}
				// solve.
				auto done = true;
				//auto flips = std::size_t(1);
				auto result = std::string("");

				if (width > data.length()) {
					result = impossible;
				} else {
					// check if all '+'.
					for (const auto& ch : data) {
						if (ch == '-') {
							done = false;
							break;
						}
					}
					if (!done) {
						// check for overlap.
						const auto toverlap = int((width * 2) - data.length());
						if (toverlap > 1) {
							// get overlapped data.
							const auto overlap_data = data.substr(width - toverlap, width - 1);
							if (overlap_data.length() != toverlap) {
								//result = "ERROR";
								//done = true;
							} else {
								// check if all overlapped data is the same char.
								auto pancake = ' ';
								for (const auto ch : overlap_data) {
									if (pancake == ' ') {
										pancake = ch;
									} else {
										if (ch != pancake) {
											result = impossible;
											done = true;
											break;
										}
									}
								}
							}
						}
						if (!done) {
							auto cdata = data;
							auto failed1 = false;
							auto flips_front = 0;
							auto tmp_width = width;
							auto flipping = false;
							auto finished = false;

							// flip bits from left to right.
							for (;;) {
								for (auto i = 0; i < cdata.length(); ++i) {
									if (flipping) {
										if (cdata[i] == '-')
											cdata[i] = '+';
										else
											cdata[i] = '-';
	
										if (--tmp_width == 0) {
											++flips_front;
											tmp_width = width;
											flipping = false;
											break;
										}

									} else {
										if (cdata[i] == '-') {
											if ((cdata.length() - i) >= width) {
												cdata[i] = '+';
												if (width > 1) {
													flipping = true;
													--tmp_width;
												} else {
													++flips_front;
												}
											} else {
												finished = true;
												break;
											}
										}
									}
									if (finished)
										break;
									if (i == (cdata.length() - 1))
										finished = true;
								}
								if (finished) {
									break;
								}
							}
							for (const auto& ch : cdata) {
								if (ch == '-') {
									failed1 = true;
									break;
								}
							}

							// flip bits from right to left.
							auto flips_back = 0;
							auto failed2 = false;
							cdata = data;
							tmp_width = width;
							flipping = false;
							finished = false;
							for (;;) {
								for (auto i = cdata.length() - 1; i >= 0; --i) {
									if (flipping) {
										if (cdata[i] == '-')
											cdata[i] = '+';
										else
											cdata[i] = '-';
	
										if (--tmp_width == 0) {
											++flips_back;
											tmp_width = width;
											flipping = false;
											break;
										}

									} else {
										if (cdata[i] == '-') {
											if (i >= (width - 1)) {
												cdata[i] = '+';
												if (width > 1) {
													flipping = true;
													--tmp_width;
												} else {
													++flips_back;
												}
											} else {
												finished = true;
												break;
											}
										}
									}
									if (finished)
										break;
									if (i == 0)
										finished = true;
								}
								if (finished) {
									break;
								}
							}
							for (const auto& ch : cdata) {
								if (ch == '-') {
									failed2 = true;
									break;
								}
							}

							if (!done) {
								if (failed1 && failed2) {
									result = impossible;
								} else {
									auto flips = -1;
									if (failed1 && !failed2) {
										flips = flips_back;
									} else if (failed2 && !failed1) {
										flips = flips_front;
									} else {
										if (flips_front >= flips_back)
											flips = flips_front;
										else
											flips = flips_back;
									}
									result = std::to_string(flips);
								}
							}
						}

					} else {
						result = "0";
					}
				}
				if (result.compare("ERROR") == 0) {
					std::cerr << "\nERROR\n" << std::endl;
					break;
				} else {
					out << "Case #" + std::to_string(ndata) + ": " + result + "\n";
					++ndata;
				}
			}
		}
		out.close();
		in.close();

	} else {
		std::cerr << "usage: <prog> [infile] [outfile]" << std::endl;
	}
	return 0;
}*/

/*auto result(long unsigned int data) -> std::size_t
{
	if(data >= 10)
		result(data / 10);
	return (data % 10);
}*/

// problem b: tidy numbers
int main(int argc, char **argv)
{
	// count backwards from input dataset and find the next 'tidy' number.
	// starting from the left side:
	//		- if there's a single number, that is the output.
	//		- if there's more than a single number, the next number must be >= the previous number.

	if (argc == 3) {
		std::ifstream in(argv[1]);
		std::ofstream out(argv[2]);

		if (in.is_open() && out.is_open()) {
            auto tdata = std::size_t(0);
			auto line = std::string("");

			// get total number of data sets.
			std::getline(in, line);
			tdata = std::stoul(line);

			// loop through data sets and solve.
			auto result = std::string("");
			auto ndata = std::size_t(1);
			auto data = std::size_t(0);
			auto done = false;
			while (std::getline(in, line)) {
				data = std::stoul(line);
				if (data < 10) {
					result = std::to_string(data);
					done = true;
				} else {
					char last = ' ';
					auto next = data;
					auto failed = false;
					for (;;) {
						for (const auto digit : std::to_string(next)) {
							//std::cout << digit - '0' << std::endl;
							//std::cin.get();
							if (last == ' ') {
								last = digit;
	
							} else if (((digit - '0') >= (last - '0'))) {
								last = digit;
							} else {
								failed = true;
								break;
							}
						}
						if (failed) {
							last = ' ';
							failed = false;
							--next;
						} else {
							const auto test = std::to_string(next);
							if (test[0] == 0 - '0') {
								last = ' ';
								failed = false;
								--next;
							} else {
								result = std::to_string(next);
								break;
							}
						}
					}
					done = true;
				}
				if (done) {
					out << "Case #" + std::to_string(ndata) + ": " + result + "\n";
					++ndata;
				}
			}
		}
		in.close();
		out.close();
	}
	return 0;
}
